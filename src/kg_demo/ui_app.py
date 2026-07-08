from __future__ import annotations

import time
from functools import wraps
from typing import Any, Dict, List

from flask import Flask, jsonify, request, send_from_directory

from .artifact_store import read_json
from .document_store import document_index, invalidate_document_cache, load_normalized_documents
from .drafting import draft_dosing_section, flawed_dosing_draft
from .impact_analyzer import analyze_protocol_impacts
from .preload_local_state import ensure_local_demo_state
from .query_engine import GraphQueryEngine
from .simulate_amendment import simulate_dose_amendment
from .validator import validate_draft

_STATE_CACHE: Dict[str, Any] = {
    "bootstrap": None,
    "bootstrap_expires_at": 0.0,
    "ledger": None,
    "ledger_expires_at": 0.0,
    "graph": None,
    "graph_expires_at": 0.0,
}
_CACHE_TTL_SECONDS = 20.0


def _json_action(fn):
    """Wrap a Flask action handler so exceptions return a structured JSON error
    instead of Flask's default HTML 500 page (which the frontend can't parse)."""

    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return fn(*args, **kwargs)
        except ValueError as exc:
            return jsonify({"error": str(exc), "error_type": type(exc).__name__}), 400
        except Exception as exc:  # noqa: BLE001
            return jsonify({"error": str(exc), "error_type": type(exc).__name__}), 500

    return wrapper


def create_app() -> Flask:
    app = Flask(
        __name__,
        static_folder="ui_static",
        static_url_path="/static",
    )

    @app.get("/")
    def index() -> Any:
        return send_from_directory(app.static_folder, "index.html")

    @app.get("/api/health")
    def health() -> Any:
        return jsonify({"status": "ok"})

    @app.get("/api/bootstrap")
    def bootstrap() -> Any:
        cached = _cache_get("bootstrap")
        if cached is not None:
            return jsonify(cached)

        engine = GraphQueryEngine()
        docs = load_normalized_documents()
        claims = read_json("claims/claim_ledger.json")
        system_events = _safe_download_list("claims/approval_events.json")
        graph_manifest = _safe_download_object("graph/graph_manifest.json")
        payload = {
            "documents": [
                {
                    "source_id": doc["source_id"],
                    "title": doc.get("title") or doc.get("label") or doc["source_id"],
                    "family": doc.get("family"),
                    "kind": doc.get("kind"),
                }
                for doc in docs
            ],
            "claims": claims,
            "system_events": system_events,
            "approval_events": system_events,
            "graph_manifest": graph_manifest,
            "demo_flawed_draft": flawed_dosing_draft(),
            "current_dose": engine.answer_current_dose().__dict__,
        }
        _cache_set("bootstrap", payload)
        return jsonify(payload)

    @app.get("/api/documents/<source_id>")
    def get_document(source_id: str) -> Any:
        docs = document_index()
        document = docs.get(source_id)
        if not document:
            return jsonify({"error": "Document not found"}), 404
        return jsonify(document)

    @app.post("/api/actions/current-dose")
    @_json_action
    def current_dose() -> Any:
        engine = GraphQueryEngine()
        result = engine.answer_current_dose()
        return jsonify(result.__dict__)

    @app.post("/api/actions/what-changed")
    @_json_action
    def what_changed() -> Any:
        engine = GraphQueryEngine()
        result = engine.answer_what_changed()
        return jsonify(result.__dict__)

    @app.post("/api/actions/draft")
    @_json_action
    def draft() -> Any:
        engine = GraphQueryEngine()
        result = draft_dosing_section(engine)
        return jsonify(result)

    @app.post("/api/actions/validate")
    @_json_action
    def validate() -> Any:
        payload = request.get_json(silent=True) or {}
        text = payload.get("text") or flawed_dosing_draft()["text"]
        engine = GraphQueryEngine()
        result = validate_draft(engine, {"draft_id": payload.get("draft_id", "ui_draft"), "text": text})
        return jsonify(result)

    @app.post("/api/actions/impact-map")
    @_json_action
    def impact_map() -> Any:
        return jsonify(analyze_protocol_impacts())

    @app.post("/api/actions/simulate-amendment")
    @_json_action
    def simulate_amendment() -> Any:
        payload = request.get_json(silent=True) or {}
        new_dose_mg = int(payload.get("new_dose_mg", 100))
        note = payload.get("note", "Simulated amendment from the demo UI.")
        result = simulate_dose_amendment(new_dose_mg=new_dose_mg, reviewer_note=note)
        _cache_invalidate()
        return jsonify(result)

    @app.post("/api/actions/current-dose-now")
    @_json_action
    def current_dose_now() -> Any:
        engine = GraphQueryEngine()
        result = engine.answer_current_dose()
        return jsonify(result.__dict__)

    @app.post("/api/actions/reset-demo")
    @_json_action
    def reset_demo() -> Any:
        ensure_local_demo_state(reset=True)
        invalidate_document_cache()
        _cache_invalidate()
        return jsonify({"status": "ok", "message": "Demo state reset to the baseline amendment scenario."})

    @app.get("/api/state/ledger")
    def ledger() -> Any:
        cached = _cache_get("ledger")
        if cached is not None:
            return jsonify(cached)
        payload = {
            "claims": read_json("claims/claim_ledger.json"),
            "system_events": _safe_download_list("claims/approval_events.json"),
        }
        _cache_set("ledger", payload)
        return jsonify(payload)

    @app.get("/api/state/graph")
    def graph() -> Any:
        cached = _cache_get("graph")
        if cached is not None:
            return jsonify(cached)
        payload = {
            "nodes": read_json("graph/nodes.json"),
            "edges": read_json("graph/edges.json"),
        }
        _cache_set("graph", payload)
        return jsonify(payload)

    @app.get("/api/state/demo-results")
    def demo_results() -> Any:
        return jsonify(
            {
                "basic": _safe_download_object("demo/basic_demo_outputs.json"),
                "full": _safe_download_object("demo/full_demo_outputs.json"),
            }
        )

    return app


def _safe_download_object(blob_name: str) -> Dict[str, Any]:
    try:
        payload = read_json(blob_name)
        if isinstance(payload, dict):
            return payload
        return {}
    except Exception:  # noqa: BLE001
        return {}


def _safe_download_list(blob_name: str) -> List[Dict[str, Any]]:
    try:
        payload = read_json(blob_name)
        if isinstance(payload, list):
            return payload
        return []
    except Exception:  # noqa: BLE001
        return []


def _cache_get(key: str) -> Any:
    now = time.time()
    value = _STATE_CACHE.get(key)
    expires_at = _STATE_CACHE.get(f"{key}_expires_at", 0.0)
    if value is not None and now < expires_at:
        return value
    return None


def _cache_set(key: str, value: Any) -> None:
    _STATE_CACHE[key] = value
    _STATE_CACHE[f"{key}_expires_at"] = time.time() + _CACHE_TTL_SECONDS


def _cache_invalidate() -> None:
    for key in ("bootstrap", "ledger", "graph"):
        _STATE_CACHE[key] = None
        _STATE_CACHE[f"{key}_expires_at"] = 0.0
