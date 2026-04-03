from __future__ import annotations

import argparse
from pathlib import Path


def add_input_output_args(
    parser: argparse.ArgumentParser,
    *,
    default_input: Path | None = None,
    default_output: Path | None = None,
) -> None:
    if default_input is not None:
        parser.add_argument("--input", type=Path, default=default_input, help=f"Input file path. Default: {default_input}")
    if default_output is not None:
        parser.add_argument("--output", type=Path, default=default_output, help=f"Output file path. Default: {default_output}")


def build_parser(description: str) -> argparse.ArgumentParser:
    return argparse.ArgumentParser(description=description)
