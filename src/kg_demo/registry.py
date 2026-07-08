from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import yaml


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_source_registry(path: Path) -> List[Dict[str, Any]]:
    payload = load_yaml(path)
    return payload.get("sources", [])


def high_priority_sources(path: Path) -> List[Dict[str, Any]]:
    return [source for source in load_source_registry(path) if source.get("priority") == "high"]
