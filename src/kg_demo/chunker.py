from __future__ import annotations

import hashlib
from typing import Any, Dict, Iterable, List


def build_chunk_id(source_id: str, heading: str, text: str) -> str:
    digest = hashlib.sha1(f"{source_id}|{heading}|{text}".encode("utf-8")).hexdigest()[:12]
    return f"chunk_{source_id}_{digest}"


def chunk_document(document: Dict[str, Any]) -> List[Dict[str, Any]]:
    chunks: List[Dict[str, Any]] = []
    sections = document.get("sections", []) or []
    for index, section in enumerate(sections, start=1):
        text = (section.get("text") or "").strip()
        if not text:
            continue
        heading = section.get("heading") or f"Section {index}"
        chunk_id = build_chunk_id(document["source_id"], heading, text)
        chunks.append(
            {
                "chunk_id": chunk_id,
                "source_id": document["source_id"],
                "family": document.get("family"),
                "title": document.get("title"),
                "heading": heading,
                "section_index": index,
                "text": text,
                "citation_locator": heading,
                "retrieved_via": document.get("retrieved_via"),
            }
        )
    return chunks


def chunk_documents(documents: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    chunks: List[Dict[str, Any]] = []
    for document in documents:
        chunks.extend(chunk_document(document))
    return chunks
