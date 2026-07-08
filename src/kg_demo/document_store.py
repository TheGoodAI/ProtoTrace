from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Dict, List

from .artifact_store import LOCAL_STATE_DIR, read_json, use_local_demo_state
from .blob_store import download_json, list_blob_names
from .settings import ROOT_DIR

_DOC_CACHE: Dict[str, Any] = {"value": None, "expires_at": 0.0}
_CACHE_TTL_SECONDS = 30.0


def invalidate_document_cache() -> None:
    _DOC_CACHE["value"] = None
    _DOC_CACHE["expires_at"] = 0.0


def load_normalized_documents() -> List[Dict[str, Any]]:
    now = time.time()
    if _DOC_CACHE["value"] is not None and now < _DOC_CACHE["expires_at"]:
        return _DOC_CACHE["value"]

    if use_local_demo_state():
        documents = load_local_normalized_documents()
        try:
            demo_documents = read_json("normalized/demo_documents.json")
            if isinstance(demo_documents, list):
                documents.extend(demo_documents)
        except Exception:  # noqa: BLE001
            pass
        _DOC_CACHE["value"] = documents
        _DOC_CACHE["expires_at"] = now + _CACHE_TTL_SECONDS
        return documents

    documents: List[Dict[str, Any]] = []

    for blob_name in list_blob_names("data/normalized/"):
        if blob_name.endswith(".json") and not blob_name.endswith(".gitkeep"):
            documents.append(download_json(blob_name))

    try:
        demo_documents = download_json("normalized/demo_documents.json")
        if isinstance(demo_documents, list):
            documents.extend(demo_documents)
    except Exception:  # noqa: BLE001
        pass

    _DOC_CACHE["value"] = documents
    _DOC_CACHE["expires_at"] = now + _CACHE_TTL_SECONDS
    return documents


def document_index() -> Dict[str, Dict[str, Any]]:
    return {doc["source_id"]: doc for doc in load_normalized_documents()}


def load_local_normalized_documents() -> List[Dict[str, Any]]:
    documents: List[Dict[str, Any]] = []
    normalized_dir = ROOT_DIR / "data" / "normalized"
    for path in normalized_dir.glob("*.json"):
        documents.append(json.loads(path.read_text(encoding="utf-8")))
    return documents
