#!/usr/bin/env python3
"""Score enriched faculty rows and render a ranked markdown report."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research_pipeline.config import get_config_value, root_path
from research_pipeline.csv_utils import parse_csv_file
from research_pipeline.cli import add_input_output_args, build_parser


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "faculty_enriched.csv"
OUTPUT_PATH = ROOT / "data" / "final_ranked.md"

UNKNOWN = "UNKNOWN"
STRICT_SCORING_PROMPT = str(get_config_value("scoring.strict_prompt", ""))
SCORING_EXAMPLES_PATH = root_path() / str(get_config_value("scoring.examples_path", "configs/scoring_examples.json"))


PROFILE_KEYWORDS = {
    "ai_for_science": (
        34,
        [
            r"\bai for science\b",
            r"\bscientific machine learning\b",
            r"\bscience-driven ai\b",
        ],
        "AI for science",
    ),
    "inverse_problems": (
        34,
        [
            r"\binverse problems?\b",
            r"\binverse imaging\b",
        ],
        "inverse problems",
    ),
    "drug_discovery": (
        34,
        [
            r"\bdrug discovery\b",
            r"\bdrug design\b",
            r"\bmolecular design\b",
            r"\bmolecule generation\b",
            r"\bprotein design\b",
        ],
        "AI for drug discovery",
    ),
    "medical_imaging": (
        32,
        [
            r"\bmedical imaging\b",
            r"\bbiomedical imaging\b",
            r"\bradiology\b",
            r"\bclinical imaging\b",
        ],
        "medical imaging",
    ),
    "comp_bio": (
        32,
        [
            r"\bcomputational biology\b",
            r"\bbioinformatics\b",
            r"\bgenomics\b",
            r"\bproteomics\b",
            r"\bprotein\b",
            r"\bmolecular biology\b",
            r"\bbiomedical\b",
        ],
        "computational biology / bioinformatics",
    ),
    "machine_learning": (
        18,
        [
            r"\bmachine learning\b",
            r"\bartificial intelligence\b",
            r"\bdeep learning\b",
        ],
        "general AI / ML",
    ),
    "computer_vision": (
        16,
        [
            r"\bcomputer vision\b",
            r"\bvisual recognition\b",
            r"\bimage understanding\b",
        ],
        "computer vision",
    ),
    "nlp": (
        8,
        [
            r"\bnatural language processing\b",
            r"\blanguage models?\b",
            r"\bllms?\b",
        ],
        "NLP / language models",
    ),
}


@dataclass(frozen=True)
class EnrichedFaculty:
    school_name: str
    rank: int
    professor_name: str
    department: str
    faculty_url: str
    lab_url: str
    source_type: str
    notes: str
    research_description: str
    research_tags: str
    recent_work_cues: str
    ra_opportunity_cues: str
    advising_cues: str
    uncertainty_flags: str


@dataclass(frozen=True)
class ScoredFaculty:
    row: EnrichedFaculty
    summary: str
    phd_score: int
    ra_score: int
    rationale_phd: str
    rationale_ra: str
    potential_concerns: str
    confidence: str


def parse_csv_rows(path: Path, required_columns: Iterable[str]) -> list[dict[str, str]]:
    return parse_csv_file(path, required_columns)


def build_rows(rows: Iterable[dict[str, str]]) -> list[EnrichedFaculty]:
    built = []
    for row in rows:
        built.append(
            EnrichedFaculty(
                school_name=row["school_name"].strip(),
                rank=int(row["rank"]),
                professor_name=row["professor_name"].strip(),
                department=row["department"].strip(),
                faculty_url=row["faculty_url"].strip(),
                lab_url=row["lab_url"].strip(),
                source_type=row["source_type"].strip(),
                notes=row["notes"].strip(),
                research_description=row["research_description"].strip(),
                research_tags=row["research_tags"].strip(),
                recent_work_cues=row["recent_work_cues"].strip(),
                ra_opportunity_cues=row["ra_opportunity_cues"].strip(),
                advising_cues=row["advising_cues"].strip(),
                uncertainty_flags=row["uncertainty_flags"].strip(),
            )
        )
    return built


def known(value: str) -> bool:
    return bool(value and value != UNKNOWN)


def combined_evidence_text(row: EnrichedFaculty) -> str:
    parts = [
        row.research_description,
        row.research_tags,
        row.recent_work_cues,
        row.ra_opportunity_cues,
        row.advising_cues,
        row.notes,
    ]
    return " ".join(part for part in parts if known(part))


def detect_profile_hits(row: EnrichedFaculty) -> list[tuple[str, int, str]]:
    text = combined_evidence_text(row).lower()
    hits = []
    for _key, (weight, patterns, label) in PROFILE_KEYWORDS.items():
        if any(re.search(pattern, text, flags=re.I) for pattern in patterns):
            hits.append((label, weight, label))
    hits.sort(key=lambda item: (-item[1], item[0]))
    return hits


def score_phd(row: EnrichedFaculty, hits: list[tuple[str, int, str]]) -> tuple[int, str]:
    alignment = min(sum(weight for _, weight, _ in hits[:3]), 60)
    evidence_bonus = 0
    reasons = []

    if hits:
        reasons.append("Explicit overlap found in: " + ", ".join(label for label, _, _ in hits[:3]) + ".")
    else:
        reasons.append("No direct overlap with the user's target domains appears in the structured evidence.")

    if known(row.research_description):
        evidence_bonus += 12
        reasons.append("Research description is explicit.")
    if known(row.recent_work_cues):
        evidence_bonus += 8
        reasons.append("Recent work cues are present.")
    if known(row.advising_cues):
        evidence_bonus += 15
        reasons.append("Advising or prospective-student cues are present.")
    if row.source_type == "lab_page":
        evidence_bonus += 3
        reasons.append("Evidence includes a lab-oriented page.")

    score = max(0, min(100, alignment + evidence_bonus))
    return score, " ".join(reasons)


def score_ra(row: EnrichedFaculty, hits: list[tuple[str, int, str]]) -> tuple[int, str]:
    alignment = min(sum(weight for _, weight, _ in hits[:3]), 50)
    evidence_bonus = 0
    reasons = []

    if hits:
        reasons.append("Relevant overlap found in: " + ", ".join(label for label, _, _ in hits[:3]) + ".")
    else:
        reasons.append("Direct topical overlap is not explicit in the available evidence.")

    if known(row.ra_opportunity_cues):
        evidence_bonus += 25
        reasons.append("RA or recruiting cues are explicit.")
    if known(row.advising_cues):
        evidence_bonus += 10
        reasons.append("Student-mentoring cues are present.")
    if known(row.recent_work_cues):
        evidence_bonus += 10
        reasons.append("Recent activity cues are present.")
    if row.source_type == "lab_page":
        evidence_bonus += 5
        reasons.append("The evidence comes from an active lab-style page.")

    score = max(0, min(100, alignment + evidence_bonus))
    return score, " ".join(reasons)


def build_summary(row: EnrichedFaculty, hits: list[tuple[str, int, str]]) -> str:
    if not hits and not known(row.research_description):
        return "UNKNOWN"
    overlap = ", ".join(label for label, _, _ in hits[:2]) if hits else "general AI-adjacent evidence only"
    advising_state = "advising cues present" if known(row.advising_cues) else "advising cues UNKNOWN"
    ra_state = "RA cues present" if known(row.ra_opportunity_cues) else "RA cues UNKNOWN"
    return f"Evidence shows overlap in {overlap}; {advising_state}; {ra_state}."


def build_potential_concerns(row: EnrichedFaculty, hits: list[tuple[str, int, str]]) -> str:
    concerns = []
    explicit_priority_hit = any(
        label in {
            "AI for science",
            "inverse problems",
            "AI for drug discovery",
            "medical imaging",
            "computational biology / bioinformatics",
        }
        for label, _, _ in hits
    )
    if not explicit_priority_hit:
        concerns.append("No explicit evidence of the user's highest-priority domains.")
    if not known(row.ra_opportunity_cues):
        concerns.append("No explicit RA / recruiting cue on the official evidence page.")
    if not known(row.advising_cues):
        concerns.append("No explicit advising / prospective-student cue on the official evidence page.")
    if not known(row.research_description) and not known(row.research_tags):
        concerns.append("Research fit evidence is sparse.")
    if row.source_type == "lab_page":
        concerns.append("Affiliation evidence relies on a lab page rather than a faculty profile.")
    return " ".join(concerns) if concerns else "NONE"


def compute_confidence(row: EnrichedFaculty, hits: list[tuple[str, int, str]]) -> str:
    known_count = sum(
        1
        for value in [
            row.research_description,
            row.research_tags,
            row.recent_work_cues,
            row.ra_opportunity_cues,
            row.advising_cues,
        ]
        if known(value)
    )
    confidence = 0.20 + 0.12 * known_count
    if hits:
        confidence += 0.10
    if row.source_type == "faculty_page":
        confidence += 0.05
    if "fetch_failed" in row.uncertainty_flags:
        confidence -= 0.15
    if "missing_research_description" in row.uncertainty_flags and "missing_research_tags" in row.uncertainty_flags:
        confidence -= 0.08
    confidence = max(0.05, min(0.95, confidence))
    return f"{confidence:.2f}"


def score_row(row: EnrichedFaculty) -> ScoredFaculty:
    hits = detect_profile_hits(row)
    phd_score, rationale_phd = score_phd(row, hits)
    ra_score, rationale_ra = score_ra(row, hits)
    summary = build_summary(row, hits)
    concerns = build_potential_concerns(row, hits)
    confidence = compute_confidence(row, hits)
    return ScoredFaculty(
        row=row,
        summary=summary,
        phd_score=phd_score,
        ra_score=ra_score,
        rationale_phd=rationale_phd,
        rationale_ra=rationale_ra,
        potential_concerns=concerns,
        confidence=confidence,
    )


def render_markdown(rows: list[ScoredFaculty]) -> str:
    examples = json.loads(SCORING_EXAMPLES_PATH.read_text(encoding="utf-8")) if SCORING_EXAMPLES_PATH.exists() else []
    lines = [
        "# Final Ranked Faculty",
        "",
        "Sorted by `phd_score` descending, then `ra_score` descending, then school rank ascending.",
        "",
        "## Strict Scoring Prompt",
        "",
        "```text",
        STRICT_SCORING_PROMPT.rstrip(),
        "```",
        "",
        "## Prompt Usage Examples",
        "",
    ]
    if examples:
        for example in examples:
            lines.extend(
                [
                    f"### {example['scenario']}",
                    "",
                    f"- Input summary: `{json.dumps(example['input_summary'], ensure_ascii=True)}`",
                    f"- Expected shape: `{json.dumps(example['expected_shape'], ensure_ascii=True)}`",
                    "",
                ]
            )
    else:
        lines.extend(["No prompt usage examples configured.", ""])
    lines.extend([
        "## Ranked Results",
        "",
    ])
    for index, scored in enumerate(rows, start=1):
        row = scored.row
        lines.extend(
            [
                f"### {index}. {row.professor_name} ({row.school_name})",
                "",
                f"- Rank: `{row.rank}`",
                f"- Department: `{row.department}`",
                f"- Faculty URL: `{row.faculty_url}`",
                f"- Lab URL: `{row.lab_url or UNKNOWN}`",
                f"- Source Type: `{row.source_type}`",
                f"- Summary: {scored.summary}",
                f"- phd_score: `{scored.phd_score}`",
                f"- ra_score: `{scored.ra_score}`",
                f"- rationale_phd: {scored.rationale_phd}",
                f"- rationale_ra: {scored.rationale_ra}",
                f"- potential_concerns: {scored.potential_concerns}",
                f"- confidence: `{scored.confidence}`",
                "",
            ]
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser("Score enriched faculty rows and render a ranked markdown report.")
    add_input_output_args(parser, default_input=INPUT_PATH, default_output=OUTPUT_PATH)
    args = parser.parse_args(argv)

    rows = build_rows(
        parse_csv_rows(
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
                "research_description",
                "research_tags",
                "recent_work_cues",
                "ra_opportunity_cues",
                "advising_cues",
                "uncertainty_flags",
            ],
        )
    )
    scored_rows = [score_row(row) for row in rows]
    scored_rows.sort(
        key=lambda scored: (
            -scored.phd_score,
            -scored.ra_score,
            scored.row.rank,
            scored.row.school_name,
            scored.row.professor_name,
        )
    )
    args.output.write_text(render_markdown(scored_rows), encoding="utf-8")
    print(f"Wrote {len(scored_rows)} ranked entries to {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
