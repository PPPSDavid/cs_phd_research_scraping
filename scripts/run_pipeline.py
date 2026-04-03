#!/usr/bin/env python3
"""Run the pipeline stages in order."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "scripts/01_get_csrankings.py",
    "scripts/02_collect_faculty.py",
    "scripts/03_enrich_faculty.py",
    "scripts/04_rank_faculty.py",
]


def main() -> int:
    for script in SCRIPTS:
        print(f"Running {script}...")
        subprocess.run([sys.executable, script], cwd=ROOT, check=True)
    print("Pipeline complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
