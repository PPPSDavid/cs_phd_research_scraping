from __future__ import annotations

import csv
import io
from pathlib import Path
from typing import Iterable


def parse_csv_text(text: str, required_columns: Iterable[str], source_label: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames is None:
        raise RuntimeError(f"{source_label} did not contain a CSV header row.")
    missing = [column for column in required_columns if column not in reader.fieldnames]
    if missing:
        raise RuntimeError(f"{source_label} is missing required columns: {', '.join(missing)}")
    rows = list(reader)
    if not rows:
        raise RuntimeError(f"{source_label} contained no data rows.")
    return rows


def parse_csv_file(path: Path, required_columns: Iterable[str]) -> list[dict[str, str]]:
    return parse_csv_text(path.read_text(encoding="utf-8"), required_columns, str(path))


def write_csv_file(path: Path, fieldnames: list[str], rows: Iterable[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
