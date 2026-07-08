from __future__ import annotations

import mimetypes
import os
import json
from pathlib import Path
from typing import Any, Iterable, List

from azure.core.exceptions import ResourceExistsError
from azure.core.pipeline.transport import RequestsTransport
from azure.storage.blob import BlobServiceClient, ContentSettings

from .settings import ROOT_DIR, load_env_file


DEFAULT_UPLOAD_PREFIXES = [
    "config/",
    "data/normalized/",
    "data/claims/",
    "data/raw/scrape_manifest.json",
    "docs/",
]


def build_blob_service_client() -> BlobServiceClient:
    load_env_file()
    connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
    if not connection_string:
        raise RuntimeError("AZURE_STORAGE_CONNECTION_STRING is not set.")
    verify_ssl = os.environ.get("AZURE_STORAGE_VERIFY_SSL", "false").lower() == "true"
    transport = RequestsTransport(connection_verify=verify_ssl)
    return BlobServiceClient.from_connection_string(connection_string, transport=transport)


def get_container_name() -> str:
    load_env_file()
    container = os.environ.get("AZURE_BLOB_CONTAINER")
    if not container:
        raise RuntimeError("AZURE_BLOB_CONTAINER is not set.")
    return container


def iter_upload_paths(prefixes: Iterable[str] | None = None) -> List[Path]:
    selected = prefixes or DEFAULT_UPLOAD_PREFIXES
    paths: List[Path] = []
    for prefix in selected:
        candidate = ROOT_DIR / prefix
        if candidate.is_file():
            paths.append(candidate)
            continue
        if candidate.is_dir():
            paths.extend(path for path in candidate.rglob("*") if path.is_file())
    return paths


def upload_paths(paths: Iterable[Path]) -> list[str]:
    service = build_blob_service_client()
    container = get_container_name()
    container_client = service.get_container_client(container)
    try:
        container_client.create_container()
    except ResourceExistsError:
        pass

    uploaded: list[str] = []
    for path in paths:
        relative = path.relative_to(ROOT_DIR).as_posix()
        blob_client = container_client.get_blob_client(relative)
        content_type, _ = mimetypes.guess_type(path.name)
        with path.open("rb") as handle:
            blob_client.upload_blob(
                handle,
                overwrite=True,
                content_settings=ContentSettings(content_type=content_type or "application/octet-stream"),
            )
        uploaded.append(relative)
    return uploaded


def upload_json(blob_name: str, payload: Any) -> str:
    service = build_blob_service_client()
    container = get_container_name()
    container_client = service.get_container_client(container)
    try:
        container_client.create_container()
    except ResourceExistsError:
        pass
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(
        json.dumps(payload, indent=2).encode("utf-8"),
        overwrite=True,
        content_settings=ContentSettings(content_type="application/json"),
    )
    return blob_name


def download_json(blob_name: str) -> Any:
    service = build_blob_service_client()
    container = get_container_name()
    blob_client = service.get_blob_client(container=container, blob=blob_name)
    data = blob_client.download_blob().readall().decode("utf-8")
    return json.loads(data)


def list_blob_names(prefix: str) -> list[str]:
    service = build_blob_service_client()
    container = get_container_name()
    container_client = service.get_container_client(container)
    return [blob.name for blob in container_client.list_blobs(name_starts_with=prefix)]
