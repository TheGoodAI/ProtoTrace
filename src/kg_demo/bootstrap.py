from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from .registry import high_priority_sources, load_yaml
from .settings import CONFIG_DIR, DATA_DIR


def build_scrape_manifest() -> List[Dict[str, Any]]:
    registry_path = CONFIG_DIR / "source_registry.yaml"
    sources = high_priority_sources(registry_path)
    timestamp = datetime.now(timezone.utc).isoformat()
    manifest = []

    for source in sources:
        manifest.append(
            {
                "source_id": source["id"],
                "family": source["family"],
                "label": source["label"],
                "seed_url": source["seed_url"],
                "kind": source["kind"],
                "priority": source["priority"],
                "queued_at": timestamp,
                "status": "pending",
            }
        )

    return manifest


def write_scrape_manifest(output_path: Path | None = None) -> Path:
    destination = output_path or (DATA_DIR / "raw" / "scrape_manifest.json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = build_scrape_manifest()
    destination.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return destination


def load_demo_tasks() -> Dict[str, Any]:
    return load_yaml(CONFIG_DIR / "demo_tasks.yaml")
