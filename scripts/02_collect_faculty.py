#!/usr/bin/env python3
"""Collect verified candidate faculty for selected CSRankings schools.

Input:
- data/schools_verified.csv

Output:
- data/faculty_raw.csv

This script is intentionally conservative. It only emits rows for schools in
the verified list, uses live CSRankings data to identify faculty with
publications in target areas, and keeps a row only when the faculty affiliation
can be supported by an official university page or a page that clearly looks
like an official lab page.
"""

from __future__ import annotations

import argparse
import csv
import html
import io
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research_pipeline.config import get_config_value
from research_pipeline.csv_utils import parse_csv_file, parse_csv_text
from research_pipeline.http import get_http_client
from research_pipeline.cli import add_input_output_args, build_parser


BASE_URL = "https://csrankings.org"
JS_URL = f"{BASE_URL}/csrankings.js"
AUTHOR_INFO_URL = f"{BASE_URL}/generated-author-info.csv"
AUTHOR_URL = f"{BASE_URL}/csrankings.csv"

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "schools_verified.csv"
OUTPUT_PATH = ROOT / "data" / "faculty_raw.csv"

TARGET_PARENT_AREAS = set(
    get_config_value("faculty_collection.target_parent_areas", ["ai", "vision", "mlmining", "nlp", "bio"])
)
LAB_KEYWORDS = ("lab", "group", "center", "centre", "institute")
HTTP_CLIENT = get_http_client()


class FacultyCollectionError(RuntimeError):
    """Raised when the faculty collection pipeline cannot be validated safely."""


@dataclass(frozen=True)
class VerifiedSchool:
    school_name: str
    rank: int
    verified_source_url: str
    department: str
    institutional_root: str


@dataclass(frozen=True)
class CandidateFaculty:
    school_name: str
    rank: int
    professor_name: str
    department: str
    faculty_url: str
    lab_url: str
    source_type: str
    notes: str


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._in_anchor = False
        self._anchor_href = ""
        self._anchor_text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href") or ""
        self._in_anchor = True
        self._anchor_href = href
        self._anchor_text_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_anchor:
            self._anchor_text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or not self._in_anchor:
            return
        text = " ".join(part.strip() for part in self._anchor_text_parts if part.strip())
        self.links.append((self._anchor_href, text.strip()))
        self._in_anchor = False
        self._anchor_href = ""
        self._anchor_text_parts = []


def fetch_text(url: str) -> str:
    return HTTP_CLIENT.fetch_text(url)


def parse_csv_rows(path_or_text: str | Path, required_columns: Iterable[str], source_label: str) -> list[dict[str, str]]:
    try:
        if isinstance(path_or_text, Path):
            return parse_csv_file(path_or_text, required_columns)
        return parse_csv_text(path_or_text, required_columns, source_label)
    except RuntimeError as exc:
        raise FacultyCollectionError(str(exc)) from exc


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def html_to_text(html_text: str) -> str:
    cleaned = re.sub(r"(?is)<script.*?>.*?</script>", " ", html_text)
    cleaned = re.sub(r"(?is)<style.*?>.*?</style>", " ", cleaned)
    cleaned = re.sub(r"(?s)<[^>]+>", " ", cleaned)
    return normalize_whitespace(html.unescape(cleaned))


def extract_title(html_text: str) -> str:
    match = re.search(r"(?is)<title[^>]*>(.*?)</title>", html_text)
    if not match:
        return ""
    return normalize_whitespace(html_to_text(match.group(1)))


def extract_h1(html_text: str) -> str:
    match = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", html_text)
    if not match:
        return ""
    return normalize_whitespace(html_to_text(match.group(1)))


def cleaned_department_label(title: str, h1: str, school_name: str) -> str:
    for candidate in (title, h1):
        if not candidate:
            continue
        label = candidate
        label = re.sub(r"\s*[|\-]\s*Home.*$", "", label, flags=re.I)
        label = re.sub(r"\s*[|\-]\s*" + re.escape(school_name) + r"\s*$", "", label, flags=re.I)
        label = normalize_whitespace(label)
        if label and len(label) <= 120:
            return label
    return school_name


def extract_institutional_root(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    if not host:
        raise FacultyCollectionError(f"Could not parse hostname from URL {url!r}.")
    parts = [part for part in host.split(".") if part]
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return host


def is_same_institutional_root(candidate_url: str, institutional_root: str) -> bool:
    hostname = (urlparse(candidate_url).hostname or "").lower()
    if not hostname:
        return False
    return hostname == institutional_root or hostname.endswith("." + institutional_root)


def parse_parent_map(js_text: str) -> dict[str, str]:
    match = re.search(r"CSRankings\.parentMap\s*=\s*\{(.*?)\};", js_text, flags=re.S)
    if not match:
        raise FacultyCollectionError("Could not locate CSRankings.parentMap in live JavaScript.")
    body = re.sub(r"//.*", "", match.group(1))
    entries = re.findall(r"'([^']+)'\s*:\s*'([^']+)'", body)
    if not entries:
        raise FacultyCollectionError("CSRankings.parentMap was found but could not be parsed.")
    return dict(entries)


def load_verified_schools(rows: Iterable[dict[str, str]]) -> dict[str, VerifiedSchool]:
    schools: dict[str, VerifiedSchool] = {}
    for row in rows:
        school_name = normalize_whitespace(row["school_name"])
        verified_source_url = row["verified_source_url"].strip()
        if not school_name or not verified_source_url:
            raise FacultyCollectionError("Verified school input contains a blank school name or source URL.")
        title = ""
        h1 = ""
        try:
            homepage_html = fetch_text(verified_source_url)
        except RuntimeError:
            homepage_html = ""
        if homepage_html:
            title = extract_title(homepage_html)
            h1 = extract_h1(homepage_html)
        schools[school_name] = VerifiedSchool(
            school_name=school_name,
            rank=int(row["rank"]),
            verified_source_url=verified_source_url,
            department=cleaned_department_label(title, h1, school_name),
            institutional_root=extract_institutional_root(verified_source_url),
        )
    if not schools:
        raise FacultyCollectionError("No verified schools were loaded from schools_verified.csv.")
    return schools


def collect_target_candidates(
    author_rows: Iterable[dict[str, str]],
    author_index: dict[tuple[str, str], str],
    verified_schools: dict[str, VerifiedSchool],
    parent_map: dict[str, str],
) -> dict[tuple[str, str], dict[str, object]]:
    candidates: dict[tuple[str, str], dict[str, object]] = {}
    for row in author_rows:
        school_name = normalize_whitespace(row["dept"])
        if school_name not in verified_schools:
            continue
        area = row["area"].strip()
        parent_area = parent_map.get(area)
        if parent_area not in TARGET_PARENT_AREAS:
            continue
        professor_name = normalize_whitespace(row["name"])
        faculty_url = author_index.get((school_name, professor_name), "").strip()
        if not faculty_url:
            continue
        key = (school_name, professor_name)
        entry = candidates.setdefault(
            key,
            {
                "school_name": school_name,
                "professor_name": professor_name,
                "faculty_url": faculty_url,
                "areas": set(),
            },
        )
        entry["areas"].add(parent_area)
    return candidates


def page_mentions_school(page_text: str, school_name: str) -> bool:
    return normalize_whitespace(school_name).lower() in normalize_whitespace(page_text).lower()


def page_looks_like_lab(url: str, page_text: str, title: str) -> bool:
    haystack = " ".join([url.lower(), title.lower(), page_text.lower()])
    return any(keyword in haystack for keyword in LAB_KEYWORDS)


def url_looks_like_lab(url: str) -> bool:
    lowered = url.lower()
    return any(keyword in lowered for keyword in LAB_KEYWORDS)


def extract_lab_url(faculty_url: str, html_text: str, institutional_root: str) -> str:
    parser = LinkExtractor()
    parser.feed(html_text)
    for href, text in parser.links:
        absolute = urljoin(faculty_url, href)
        if not absolute.startswith(("http://", "https://")):
            continue
        combined = f"{absolute} {text}".lower()
        if not any(keyword in combined for keyword in LAB_KEYWORDS):
            continue
        if is_same_institutional_root(absolute, institutional_root):
            return absolute
    return ""


def verify_candidate(
    school: VerifiedSchool,
    professor_name: str,
    faculty_url: str,
    areas: set[str],
) -> CandidateFaculty | None:
    official_domain_match = is_same_institutional_root(faculty_url, school.institutional_root)

    if official_domain_match:
        source_type = "faculty_page"
        verification_bits = ["official_domain"]
        return CandidateFaculty(
            school_name=school.school_name,
            rank=school.rank,
            professor_name=professor_name,
            department=school.department,
            faculty_url=faculty_url,
            lab_url="",
            source_type=source_type,
            notes=f"areas={','.join(sorted(areas))}; verified_by={'+'.join(verification_bits)}",
        )

    if not url_looks_like_lab(faculty_url):
        return None

    try:
        html_text = fetch_text(faculty_url)
    except RuntimeError:
        return None

    page_text = html_to_text(html_text)
    title = extract_title(html_text)
    mentions_school = page_mentions_school(page_text, school.school_name)
    looks_like_lab = page_looks_like_lab(faculty_url, page_text, title)

    if looks_like_lab and mentions_school:
        source_type = "lab_page"
        verification_bits = ["lab_page", "school_name_on_page"]
    else:
        return None

    notes = (
        f"areas={','.join(sorted(areas))}; "
        f"verified_by={'+'.join(verification_bits)}"
    )
    return CandidateFaculty(
        school_name=school.school_name,
        rank=school.rank,
        professor_name=professor_name,
        department=school.department,
        faculty_url=faculty_url,
        lab_url=faculty_url,
        source_type=source_type,
        notes=notes,
    )


def validate_rows(rows: Iterable[CandidateFaculty], allowed_schools: set[str]) -> None:
    bad_schools = sorted({row.school_name for row in rows if row.school_name not in allowed_schools})
    if bad_schools:
        raise FacultyCollectionError(
            "Output contained schools outside the verified list: " + ", ".join(bad_schools)
        )


def write_output_csv(rows: Iterable[CandidateFaculty], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "school_name",
                "rank",
                "professor_name",
                "department",
                "faculty_url",
                "lab_url",
                "source_type",
                "notes",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "school_name": row.school_name,
                    "rank": row.rank,
                    "professor_name": row.professor_name,
                    "department": row.department,
                    "faculty_url": row.faculty_url,
                    "lab_url": row.lab_url,
                    "source_type": row.source_type,
                    "notes": row.notes,
                }
            )


def build_author_index(author_rows: Iterable[dict[str, str]]) -> dict[tuple[str, str], str]:
    index: dict[tuple[str, str], str] = {}
    for row in author_rows:
        school_name = normalize_whitespace(row["affiliation"])
        professor_name = normalize_whitespace(row["name"])
        homepage = row["homepage"].strip()
        if not school_name or not professor_name or not homepage:
            continue
        index[(school_name, professor_name)] = homepage
    return index


def main(argv: list[str] | None = None) -> int:
    parser = build_parser("Collect verified faculty candidates from ranked schools.")
    add_input_output_args(parser, default_input=INPUT_PATH, default_output=OUTPUT_PATH)
    args = parser.parse_args(argv)

    verified_school_rows = parse_csv_rows(
        args.input,
        required_columns=["school_name", "rank", "verified_source_url"],
        source_label=str(args.input),
    )
    verified_schools = load_verified_schools(verified_school_rows)

    parent_map = parse_parent_map(fetch_text(JS_URL))
    author_rows = parse_csv_rows(
        fetch_text(AUTHOR_INFO_URL),
        required_columns=["name", "dept", "area"],
        source_label=AUTHOR_INFO_URL,
    )
    author_index_rows = parse_csv_rows(
        fetch_text(AUTHOR_URL),
        required_columns=["name", "affiliation", "homepage"],
        source_label=AUTHOR_URL,
    )
    author_index = build_author_index(author_index_rows)

    candidates = collect_target_candidates(
        author_rows=author_rows,
        author_index=author_index,
        verified_schools=verified_schools,
        parent_map=parent_map,
    )

    verified_rows: list[CandidateFaculty] = []
    seen_output_keys: set[tuple[str, str, str]] = set()
    for key in sorted(candidates, key=lambda item: (verified_schools[item[0]].rank, item[0], item[1])):
        candidate = candidates[key]
        school = verified_schools[candidate["school_name"]]
        row = verify_candidate(
            school=school,
            professor_name=candidate["professor_name"],
            faculty_url=candidate["faculty_url"],
            areas=set(candidate["areas"]),
        )
        if row is None:
            continue
        output_key = (row.school_name, row.professor_name, row.faculty_url)
        if output_key in seen_output_keys:
            continue
        seen_output_keys.add(output_key)
        verified_rows.append(row)

    validate_rows(verified_rows, set(verified_schools))
    write_output_csv(verified_rows, args.output)
    print(f"Wrote {len(verified_rows)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - top-level failure path
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
