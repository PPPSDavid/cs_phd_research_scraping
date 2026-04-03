from __future__ import annotations

import functools
import tomllib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = ROOT / "configs" / "pipeline.toml"


@functools.lru_cache(maxsize=1)
def load_config(path: str | Path | None = None) -> dict[str, Any]:
    config_path = Path(path) if path is not None else DEFAULT_CONFIG_PATH
    with config_path.open("rb") as handle:
        return tomllib.load(handle)


def get_config_value(key_path: str, default: Any = None) -> Any:
    value: Any = load_config()
    for part in key_path.split("."):
        if not isinstance(value, dict) or part not in value:
            return default
        value = value[part]
    return value


def root_path() -> Path:
    return ROOT
