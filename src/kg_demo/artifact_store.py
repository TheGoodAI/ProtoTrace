from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any, List
from uuid import uuid4

from .blob_store import download_json, list_blob_names, upload_json
from .settings import ROOT_DIR


LOCAL_STATE_DIR = Path(os.environ.get("KG_LOCAL_STATE_DIR", str(ROOT_DIR / "local_state")))


def use_local_demo_state() -> bool:
    return os.environ.get("KG_DEMO_LOCAL_ONLY", "false").lower() == "true"


def _local_path(name: str) -> Path:
    return LOCAL_STATE_DIR / Path(name)


def read_json(name: str) -> Any:
    if use_local_demo_state():
        path = _local_path(name)
        last_error: json.JSONDecodeError | None = None
        for _ in range(3):
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                last_error = exc
                time.sleep(0.05)
        if last_error is not None:
            raise last_error
    return download_json(name)


def write_json(name: str, payload: Any) -> str:
    if use_local_demo_state():
        path = _local_path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = path.with_name(f"{path.name}.{uuid4().hex}.tmp")
        temp_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        try:
            temp_path.replace(path)
        except PermissionError:
            path.write_text(temp_path.read_text(encoding="utf-8"), encoding="utf-8")
        return str(path)
    return upload_json(name, payload)


def list_json_names(prefix: str) -> List[str]:
    if use_local_demo_state():
        base = _local_path(prefix)
        if base.is_file():
            return [prefix]
        if not base.exists():
            return []
        return [str(path.relative_to(LOCAL_STATE_DIR)).replace("\\", "/") for path in base.rglob("*") if path.is_file()]
    return list_blob_names(prefix)
