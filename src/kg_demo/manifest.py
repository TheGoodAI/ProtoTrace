from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .settings import DATA_DIR


def manifest_path() -> Path:
    return DATA_DIR / "raw" / "scrape_manifest.json"


def read_manifest(path: Path | None = None) -> List[Dict[str, Any]]:
    location = path or manifest_path()
    if not location.exists():
        return []
    return json.loads(location.read_text(encoding="utf-8"))


def write_manifest(rows: List[Dict[str, Any]], path: Path | None = None) -> Path:
    location = path or manifest_path()
    location.parent.mkdir(parents=True, exist_ok=True)
    location.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    return location


def merge_results_into_manifest(rows: List[Dict[str, Any]], results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    by_id = {row["source_id"]: row for row in rows}
    for result in results:
        row = by_id.get(result["source_id"])
        if not row:
            continue
        row.update(result)
    return list(by_id.values())
