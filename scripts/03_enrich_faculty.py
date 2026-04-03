#!/usr/bin/env python3
"""Enrich faculty rows with evidence from official pages."""

from __future__ import annotations

import argparse
import csv
import html
import io
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research_pipeline.config import get_config_value
from research_pipeline.csv_utils import parse_csv_file, write_csv_file
from research_pipeline.http import HttpResponse, get_http_client
from research_pipeline.cli import add_input_output_args, build_parser


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "faculty_raw.csv"
OUTPUT_PATH = ROOT / "data" / "faculty_enriched.csv"

HTTP_CLIENT = get_http_client()
MAX_WORKERS = int(get_config_value("http.max_workers", 16))
UNKNOWN = "UNKNOWN"
MAX_SNIPPET_LENGTH = 320
RECENT_YEARS = ("2026", "2025", "2024", "2023")

TAG_PATTERNS = [
    ("artificial intelligence", [r"\bartificial intelligence\b", r"\bai\b"]),
    ("machine learning", [r"\bmachine learning\b", r"\bml\b"]),
    ("deep learning", [r"\bdeep learning\b"]),
    ("computer vision", [r"\bcomputer vision\b", r"\bvisual recognition\b", r"\bimage understanding\b"]),
    ("natural language processing", [r"\bnatural language processing\b", r"\bnlp\b"]),
    ("language models", [r"\blanguage model", r"\bllm", r"\bgenerative ai\b"]),
    ("computational biology", [r"\bcomputational biology\b"]),
    ("bioinformatics", [r"\bbioinformatics\b"]),
    ("genomics", [r"\bgenomics\b"]),
    ("medical imaging", [r"\bmedical imaging\b"]),
    ("robotics", [r"\brobotics?\b"]),
    ("reinforcement learning", [r"\breinforcement learning\b"]),
    ("data mining", [r"\bdata mining\b"]),
    ("information retrieval", [r"\binformation retrieval\b"]),
    ("human-ai interaction", [r"\bhuman-ai\b", r"\bhuman ai\b"]),
]

RESEARCH_PATTERNS = [
    r"\bresearch interests? (?:include|are)\b",
    r"\bmy research\b",
    r"\bi work on\b",
    r"\bwe work on\b",
    r"\bour research\b",
    r"\bfocus(?:es|ed)? on\b",
    r"\binterests? (?:include|are)\b",
    r"\bstudies\b",
]
RECENT_PATTERNS = [
    r"\b(2026|2025|2024|2023)\b",
    r"\brecent publications?\b",
    r"\bselected publications?\b",
    r"\bnews\b",
    r"\brecent work\b",
    r"\bpreprint\b",
]
RA_PATTERNS = [
    r"\bresearch assistant",
    r"\bprospective ra",
    r"\bra positions?\b",
    r"\bjoin (?:my|our) (?:group|lab)\b",
    r"\bopenings?\b",
    r"\brecruiting\b",
    r"\blooking for (?:students|research assistants?)\b",
]
ADVISING_PATTERNS = [
    r"\baccepting students\b",
    r"\bprospective students\b",
    r"\bph\.?d\.? students?\b",
    r"\badvising\b",
    r"\badvise\b",
    r"\bsupervis(?:e|ing)\b",
]
LOW_SIGNAL_PATTERNS = [
    r"about .* academics .* admission .* research .* campus life",
    r"information for: .* current students .* faculty .* staff",
    r"\ba to z index\b",
    r"\bfacebook\b.*\btwitter\b.*\blinkedin\b",
]


class FacultyEnrichmentError(RuntimeError):
    """Raised when faculty enrichment cannot be completed safely."""


@dataclass(frozen=True)
class FacultyRow:
    school_name: str
    rank: str
    professor_name: str
    department: str
    faculty_url: str
    lab_url: str
    source_type: str
    notes: str


@dataclass(frozen=True)
class FetchedPage:
    final_url: str
    html_text: str
    text: str


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_csv_rows(path: Path, required_columns: Iterable[str]) -> list[dict[str, str]]:
    try:
        return parse_csv_file(path, required_columns)
    except RuntimeError as exc:
        raise FacultyEnrichmentError(str(exc)) from exc


def build_rows(rows: Iterable[dict[str, str]]) -> list[FacultyRow]:
    built = [
        FacultyRow(
            school_name=row["school_name"].strip(),
            rank=row["rank"].strip(),
            professor_name=row["professor_name"].strip(),
            department=row["department"].strip(),
            faculty_url=row["faculty_url"].strip(),
            lab_url=row["lab_url"].strip(),
            source_type=row["source_type"].strip(),
            notes=row["notes"].strip(),
        )
        for row in rows
    ]
    if not built:
        raise FacultyEnrichmentError("No faculty rows were built from input.")
    return built


def strip_html_to_text(html_text: str) -> str:
    cleaned = re.sub(r"(?is)<script.*?>.*?</script>", " ", html_text)
    cleaned = re.sub(r"(?is)<style.*?>.*?</style>", " ", cleaned)
    cleaned = re.sub(r"(?is)<noscript.*?>.*?</noscript>", " ", cleaned)
    cleaned = re.sub(r"(?s)<[^>]+>", " ", cleaned)
    return normalize_whitespace(html.unescape(cleaned))


def extract_meta_refresh_target(html_text: str) -> str:
    match = re.search(r'(?is)<meta[^>]+http-equiv=["\']?refresh["\']?[^>]+content=["\'][^"\']*url\s*=\s*([^"\';>]+)', html_text)
    if not match:
        return ""
    return match.group(1).strip()


_fetch_cache: dict[str, FetchedPage | None] = {}
_fetch_lock = threading.Lock()


def fetch_page_uncached(url: str, depth: int = 0) -> FetchedPage | None:
    try:
        response: HttpResponse = HTTP_CLIENT.fetch_response(url)
        html_text = response.text
        final_url = response.final_url
    except Exception:
        return None

    if depth < 2:
        refresh_target = extract_meta_refresh_target(html_text)
        if refresh_target:
            redirected_url = urljoin(final_url, refresh_target)
            redirected_page = fetch_page_uncached(redirected_url, depth + 1)
            if redirected_page is not None:
                return redirected_page

    return FetchedPage(
        final_url=final_url,
        html_text=html_text,
        text=strip_html_to_text(html_text),
    )


def fetch_page(url: str) -> FetchedPage | None:
    if not url:
        return None
    with _fetch_lock:
        if url in _fetch_cache:
            return _fetch_cache[url]
    page = fetch_page_uncached(url)
    with _fetch_lock:
        _fetch_cache[url] = page
    return page


def clip_snippet(text: str, max_length: int = MAX_SNIPPET_LENGTH) -> str:
    text = normalize_whitespace(text)
    if len(text) <= max_length:
        return text
    clipped = text[:max_length].rsplit(" ", 1)[0].strip()
    return (clipped or text[:max_length]).strip() + "..."


def split_into_segments(text: str) -> list[str]:
    rough_parts = re.split(r"(?<=[\.\!\?])\s+|\s{2,}", text)
    segments = [clip_snippet(part) for part in rough_parts if len(normalize_whitespace(part)) >= 25]
    compiled_low_signal = [re.compile(pattern, flags=re.I) for pattern in LOW_SIGNAL_PATTERNS]
    return [
        segment
        for segment in segments
        if segment and not any(pattern.search(segment) for pattern in compiled_low_signal)
    ]


def first_matching_segment(segments: Iterable[str], patterns: Iterable[str]) -> str:
    compiled = [re.compile(pattern, flags=re.I) for pattern in patterns]
    for segment in segments:
        if any(pattern.search(segment) for pattern in compiled):
            return clip_snippet(segment)
    return UNKNOWN


def collect_tags(text: str) -> str:
    lowered = text.lower()
    matches = []
    for label, patterns in TAG_PATTERNS:
        if any(re.search(pattern, lowered, flags=re.I) for pattern in patterns):
            matches.append(label)
    if not matches:
        return UNKNOWN
    return "; ".join(matches)


def collect_recent_work_cues(segments: Iterable[str]) -> str:
    compiled = [re.compile(pattern, flags=re.I) for pattern in RECENT_PATTERNS]
    hits = []
    for segment in segments:
        if any(pattern.search(segment) for pattern in compiled):
            hits.append(clip_snippet(segment))
        if len(hits) >= 2:
            break
    if not hits:
        return UNKNOWN
    return " || ".join(hits)


def build_uncertainty_flags(
    *,
    page_sources: list[str],
    research_description: str,
    research_tags: str,
    recent_work_cues: str,
    ra_opportunity_cues: str,
    advising_cues: str,
) -> str:
    flags = []
    if not page_sources:
        flags.append("fetch_failed")
    elif page_sources == ["lab_url"]:
        flags.append("used_lab_page_only")
    elif len(page_sources) == 2:
        flags.append("used_faculty_and_lab_pages")
    if research_description == UNKNOWN:
        flags.append("missing_research_description")
    if research_tags == UNKNOWN:
        flags.append("missing_research_tags")
    if recent_work_cues == UNKNOWN:
        flags.append("missing_recent_work_cues")
    if ra_opportunity_cues == UNKNOWN:
        flags.append("missing_ra_opportunity_cues")
    if advising_cues == UNKNOWN:
        flags.append("missing_advising_cues")
    return "; ".join(flags) if flags else "NONE"


def combine_page_texts(faculty_page: FetchedPage | None, lab_page: FetchedPage | None) -> tuple[str, list[str]]:
    chunks = []
    sources = []
    if faculty_page is not None:
        chunks.append(faculty_page.text)
        sources.append("faculty_url")
    if lab_page is not None and (faculty_page is None or lab_page.final_url != faculty_page.final_url):
        chunks.append(lab_page.text)
        sources.append("lab_url")
    return normalize_whitespace(" ".join(chunks)), sources


def enrich_row(row: FacultyRow) -> dict[str, str]:
    faculty_page = fetch_page(row.faculty_url)
    lab_page = fetch_page(row.lab_url) if row.lab_url and row.lab_url != row.faculty_url else None
    combined_text, page_sources = combine_page_texts(faculty_page, lab_page)
    segments = split_into_segments(combined_text)

    research_description = first_matching_segment(segments, RESEARCH_PATTERNS)
    research_tags = collect_tags(combined_text)
    recent_work_cues = collect_recent_work_cues(segments)
    ra_opportunity_cues = first_matching_segment(segments, RA_PATTERNS)
    advising_cues = first_matching_segment(segments, ADVISING_PATTERNS)
    uncertainty_flags = build_uncertainty_flags(
        page_sources=page_sources,
        research_description=research_description,
        research_tags=research_tags,
        recent_work_cues=recent_work_cues,
        ra_opportunity_cues=ra_opportunity_cues,
        advising_cues=advising_cues,
    )

    return {
        "school_name": row.school_name,
        "rank": row.rank,
        "professor_name": row.professor_name,
        "department": row.department,
        "faculty_url": row.faculty_url,
        "lab_url": row.lab_url,
        "source_type": row.source_type,
        "notes": row.notes,
        "research_description": research_description,
        "research_tags": research_tags,
        "recent_work_cues": recent_work_cues,
        "ra_opportunity_cues": ra_opportunity_cues,
        "advising_cues": advising_cues,
        "uncertainty_flags": uncertainty_flags,
    }


def write_output(rows: Iterable[dict[str, str]], output_path: Path) -> None:
    fieldnames = [
        "school_name",
        "rank",
        "professor_name",
        "department",
        "faculty_url",
        "lab_url",
        "source_type",
        "notes",
        "research_description",
        "research_tags",
        "recent_work_cues",
        "ra_opportunity_cues",
        "advising_cues",
        "uncertainty_flags",
    ]
    write_csv_file(output_path, fieldnames, rows)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser("Enrich faculty rows with official-page evidence.")
    add_input_output_args(parser, default_input=INPUT_PATH, default_output=OUTPUT_PATH)
    args = parser.parse_args(argv)

    input_rows = parse_csv_rows(
        args.input,
        required_columns=[
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
    rows = build_rows(input_rows)
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        enriched_rows = list(executor.map(enrich_row, rows))
    write_output(enriched_rows, args.output)
    print(f"Wrote {len(enriched_rows)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
