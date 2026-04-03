#!/usr/bin/env python3
"""Fetch and verify CSRankings schools ranked 50 through 100 inclusive.

This script intentionally derives the rankings from the live CSRankings assets
instead of relying on any remembered ordering. It validates a few critical
HTML/JavaScript contracts before using the site's published CSV data and rank
computation rules to build `data/schools_verified.csv`.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research_pipeline.config import get_config_value
from research_pipeline.csv_utils import parse_csv_text
from research_pipeline.http import get_http_client
from research_pipeline.cli import add_input_output_args, build_parser


BASE_URL = "https://csrankings.org"
HTML_URL = f"{BASE_URL}/"
JS_URL = f"{BASE_URL}/csrankings.js"
AUTHOR_INFO_URL = f"{BASE_URL}/generated-author-info.csv"
INSTITUTIONS_URL = f"{BASE_URL}/institutions.csv"

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "data" / "schools_verified.csv"

TARGET_REGION = str(get_config_value("ranking.target_region", "us"))
TARGET_RANK_MIN = int(get_config_value("ranking.rank_min", 50))
TARGET_RANK_MAX = int(get_config_value("ranking.rank_max", 100))
ALLOWED_IGNORED_AREAS = {"pets"}
HTTP_CLIENT = get_http_client()


class CSRankingsFormatError(RuntimeError):
    """Raised when the live CSRankings page no longer matches expected format."""


@dataclass(frozen=True)
class Institution:
    name: str
    homepage: str
    countryabbrv: str


@dataclass(frozen=True)
class RankedSchool:
    rank: int
    school_name: str
    csrankings_url: str
    verified_source_url: str


def fetch_text(url: str) -> str:
    return HTTP_CLIENT.fetch_text(url)


def require_substrings(label: str, text: str, required: Iterable[str]) -> None:
    missing = [needle for needle in required if needle not in text]
    if missing:
        joined = ", ".join(repr(item) for item in missing)
        raise CSRankingsFormatError(f"{label} is missing required markers: {joined}")


def strip_js_line_comments(js_block: str) -> str:
    return re.sub(r"//.*", "", js_block)


def extract_js_object_body(js_text: str, object_name: str) -> str:
    pattern = rf"{re.escape(object_name)}\s*=\s*\{{(.*?)\}};"
    match = re.search(pattern, js_text, flags=re.DOTALL)
    if not match:
        raise CSRankingsFormatError(f"Could not locate {object_name} in live JavaScript.")
    return strip_js_line_comments(match.group(1))


def parse_parent_map(js_text: str) -> dict[str, str]:
    body = extract_js_object_body(js_text, "CSRankings.parentMap")
    entries = re.findall(r"'([^']+)'\s*:\s*'([^']+)'", body)
    if not entries:
        raise CSRankingsFormatError("Live JavaScript parentMap was found but could not be parsed.")
    parent_map = dict(entries)
    sentinels = {
        "aaai": "ai",
        "sigcomm": "comm",
        "sigcse": "csed",
        "usenixsec": "sec",
    }
    for key, expected in sentinels.items():
        actual = parent_map.get(key)
        if actual != expected:
            raise CSRankingsFormatError(
                f"Unexpected parent mapping for {key!r}: expected {expected!r}, got {actual!r}."
            )
    return parent_map


def parse_next_tier(js_text: str) -> set[str]:
    body = extract_js_object_body(js_text, "CSRankings.nextTier")
    entries = re.findall(r"'([^']+)'\s*:\s*true", body)
    if not entries:
        raise CSRankingsFormatError("Live JavaScript nextTier map was found but could not be parsed.")
    next_tier = set(entries)
    for sentinel in ("kdd", "ndss", "pods", "oopsla"):
        if sentinel not in next_tier:
            raise CSRankingsFormatError(f"Expected next-tier venue {sentinel!r} was not found.")
    return next_tier


def validate_live_contract(html_text: str, js_text: str) -> None:
    require_substrings(
        "HTML",
        html_text,
        [
            '<form id="rankform"',
            '<script src="csrankings.js"',
            'id="regions"',
            'id="fromyear"',
            'id="toyear"',
        ],
    )
    require_substrings(
        "JavaScript",
        js_text,
        [
            'CSRankings.authorinfoFile = "./generated-author-info.csv";',
            'CSRankings.countryinfoFile = "./institutions.csv";',
            'function sortIndex(univagg)',
            "rank = rank + ties;",
            "currYear - 10",
        ],
    )


def parse_csv_rows(text: str, required_columns: Iterable[str], source_url: str) -> list[dict[str, str]]:
    try:
        return parse_csv_text(text, required_columns, source_url)
    except RuntimeError as exc:
        raise CSRankingsFormatError(str(exc)) from exc


def load_us_institutions(rows: Iterable[dict[str, str]]) -> dict[str, Institution]:
    institutions: dict[str, Institution] = {}
    for row in rows:
        name = row["institution"].strip()
        homepage = row["homepage"].strip()
        countryabbrv = row["countryabbrv"].strip().lower()
        if not name:
            continue
        if countryabbrv != TARGET_REGION:
            continue
        institutions[name] = Institution(name=name, homepage=homepage, countryabbrv=countryabbrv)
    if not institutions:
        raise CSRankingsFormatError("No US institutions were found in institutions.csv.")
    return institutions


def current_year_range() -> tuple[int, int]:
    current_year = dt.datetime.now().year
    return current_year - 10, current_year


def compute_ranked_schools(
    author_rows: Iterable[dict[str, str]],
    us_institutions: dict[str, Institution],
    parent_map: dict[str, str],
    next_tier: set[str],
    start_year: int,
    end_year: int,
) -> list[RankedSchool]:
    selected_parent_areas = sorted(set(parent_map.values()))
    if not selected_parent_areas:
        raise CSRankingsFormatError("No top-level areas were derived from the live JavaScript.")

    area_dept_adjusted_count: dict[tuple[str, str], float] = defaultdict(float)
    dept_names: dict[str, set[str]] = defaultdict(set)
    ignored_unknown_areas: set[str] = set()

    for row in author_rows:
        dept = row["dept"].strip()
        area = row["area"].strip()
        year = int(float(row["year"]))
        if dept not in us_institutions:
            continue
        if year < start_year or year > end_year:
            continue
        if area in next_tier:
            continue
        if area not in parent_map:
            ignored_unknown_areas.add(area)
            continue

        parent_area = parent_map[area]
        adjusted_count = float(row["adjustedcount"])
        area_dept_adjusted_count[(parent_area, dept)] += adjusted_count
        dept_names[dept].add(row["name"].strip())

    if not dept_names:
        raise CSRankingsFormatError("No departments were ranked after applying live filters.")

    stats: dict[str, float] = {}
    for dept in dept_names:
        stat = 1.0
        for parent_area in selected_parent_areas:
            stat *= area_dept_adjusted_count.get((parent_area, dept), 0.0) + 1.0
        stats[dept] = round(stat ** (1.0 / len(selected_parent_areas)), 1)

    ordered_departments = sorted(stats, key=lambda dept: (-stats[dept], dept))

    pinned_rankings_url = f"{BASE_URL}/fromyear/{start_year}/toyear/{end_year}/index?all"
    ranked_schools: list[RankedSchool] = []
    rank = 0
    ties = 1
    old_value: float | None = None
    previous_rank = 0

    for dept in ordered_departments:
        value = stats[dept]
        if value == 0.0:
            break
        if old_value != value:
            rank += ties
            ties = 0
        previous_rank = rank

        if TARGET_RANK_MIN <= rank <= TARGET_RANK_MAX:
            homepage = us_institutions[dept].homepage.strip()
            if not homepage:
                raise CSRankingsFormatError(f"US institution {dept!r} is missing a homepage in institutions.csv.")
            ranked_schools.append(
                RankedSchool(
                    rank=rank,
                    school_name=dept,
                    csrankings_url=pinned_rankings_url,
                    verified_source_url=homepage,
                )
            )
        elif rank > TARGET_RANK_MAX:
            break

        ties += 1
        old_value = value

    if not ranked_schools:
        raise CSRankingsFormatError(
            f"No schools were found in the requested rank range {TARGET_RANK_MIN}-{TARGET_RANK_MAX}."
        )
    if ranked_schools[0].rank < TARGET_RANK_MIN or ranked_schools[-1].rank > TARGET_RANK_MAX:
        raise CSRankingsFormatError("Rank filtering produced out-of-range results.")
    if any(curr.rank > nxt.rank for curr, nxt in zip(ranked_schools, ranked_schools[1:])):
        raise CSRankingsFormatError("Ranked schools are not sorted in ascending rank order.")
    unexpected_unknown_areas = ignored_unknown_areas - ALLOWED_IGNORED_AREAS
    if unexpected_unknown_areas:
        raise CSRankingsFormatError(
            "Encountered unexpected area codes outside the live parentMap: "
            + ", ".join(sorted(unexpected_unknown_areas))
        )

    return ranked_schools


def write_output_csv(rows: Iterable[RankedSchool], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["rank", "school_name", "csrankings_url", "verified_source_url"],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "rank": row.rank,
                    "school_name": row.school_name,
                    "csrankings_url": row.csrankings_url,
                    "verified_source_url": row.verified_source_url,
                }
            )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser("Fetch and verify ranked schools from CSRankings.")
    add_input_output_args(parser, default_output=OUTPUT_PATH)
    args = parser.parse_args(argv)

    html_text = fetch_text(HTML_URL)
    js_text = fetch_text(JS_URL)
    validate_live_contract(html_text, js_text)

    parent_map = parse_parent_map(js_text)
    next_tier = parse_next_tier(js_text)

    institution_rows = parse_csv_rows(
        fetch_text(INSTITUTIONS_URL),
        required_columns=["institution", "countryabbrv", "homepage"],
        source_url=INSTITUTIONS_URL,
    )
    author_rows = parse_csv_rows(
        fetch_text(AUTHOR_INFO_URL),
        required_columns=["name", "dept", "area", "adjustedcount", "year"],
        source_url=AUTHOR_INFO_URL,
    )

    us_institutions = load_us_institutions(institution_rows)
    start_year, end_year = current_year_range()
    ranked_schools = compute_ranked_schools(
        author_rows=author_rows,
        us_institutions=us_institutions,
        parent_map=parent_map,
        next_tier=next_tier,
        start_year=start_year,
        end_year=end_year,
    )
    write_output_csv(ranked_schools, args.output)
    print(f"Wrote {len(ranked_schools)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - top-level failure path
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
