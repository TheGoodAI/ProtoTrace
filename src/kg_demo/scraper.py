from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from .settings import DATA_DIR


USER_AGENT = "GoodAI-KG-Demo/0.1 (+regulatory-ingestion)"
TIMEOUT_SECONDS = 30


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    lowered = re.sub(r"[^a-z0-9]+", "_", lowered)
    return lowered.strip("_")


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass
class FetchResult:
    source_id: str
    url: str
    kind: str
    status: str
    fetched_at: str
    http_status: Optional[int] = None
    content_type: Optional[str] = None
    raw_path: Optional[str] = None
    normalized_path: Optional[str] = None
    content_hash: Optional[str] = None
    error: Optional[str] = None


class SourceScraper:
    def __init__(self, output_dir: Path | None = None) -> None:
        self.output_dir = output_dir or DATA_DIR
        self.snapshots_dir = self.output_dir / "raw" / "snapshots"
        self.normalized_dir = self.output_dir / "normalized"
        self.snapshots_dir.mkdir(parents=True, exist_ok=True)
        self.normalized_dir.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
        self.session.trust_env = False
        self.session.headers.update({"User-Agent": USER_AGENT})

    def scrape_sources(self, sources: Iterable[Dict[str, Any]]) -> List[FetchResult]:
        results: List[FetchResult] = []
        for source in sources:
            results.append(self.scrape_source(source))
        return results

    def scrape_source(self, source: Dict[str, Any]) -> FetchResult:
        source_id = source["id"]
        url = source["seed_url"]
        kind = source["kind"]
        fetched_at = datetime.now(timezone.utc).isoformat()

        try:
            response = self.session.get(url, timeout=TIMEOUT_SECONDS)
            content_type = response.headers.get("Content-Type", "")
            response.raise_for_status()

            if kind == "pdf" or "pdf" in content_type.lower():
                raw_path = self._write_binary_snapshot(source_id, response.content, ".pdf")
                return FetchResult(
                    source_id=source_id,
                    url=url,
                    kind=kind,
                    status="pdf_staged",
                    fetched_at=fetched_at,
                    http_status=response.status_code,
                    content_type=content_type,
                    raw_path=str(raw_path),
                    content_hash=hashlib.sha256(response.content).hexdigest(),
                )

            html = response.text
            raw_path = self._write_text_snapshot(source_id, html, ".html")
            normalized = self._normalize_html(source, html, response.url)
            normalized_path = self.normalized_dir / f"{slugify(source_id)}.json"
            normalized_path.write_text(json.dumps(normalized, indent=2), encoding="utf-8")

            return FetchResult(
                source_id=source_id,
                url=response.url,
                kind=kind,
                status="normalized",
                fetched_at=fetched_at,
                http_status=response.status_code,
                content_type=content_type,
                raw_path=str(raw_path),
                normalized_path=str(normalized_path),
                content_hash=text_hash(normalized["text"]),
            )
        except Exception as exc:  # noqa: BLE001
            return FetchResult(
                source_id=source_id,
                url=url,
                kind=kind,
                status="failed",
                fetched_at=fetched_at,
                error=str(exc),
            )

    def _write_text_snapshot(self, source_id: str, content: str, suffix: str) -> Path:
        path = self.snapshots_dir / f"{slugify(source_id)}{suffix}"
        path.write_text(content, encoding="utf-8")
        return path

    def _write_binary_snapshot(self, source_id: str, content: bytes, suffix: str) -> Path:
        path = self.snapshots_dir / f"{slugify(source_id)}{suffix}"
        path.write_bytes(content)
        return path

    def _normalize_html(self, source: Dict[str, Any], html: str, resolved_url: str) -> Dict[str, Any]:
        soup = BeautifulSoup(html, "html.parser")
        self._drop_noise(soup)

        title = self._extract_title(soup, source)
        sections = self._extract_sections(soup)
        text = "\n\n".join(section["text"] for section in sections if section["text"].strip())
        links = self._extract_links(soup, resolved_url)

        return {
            "source_id": source["id"],
            "family": source["family"],
            "label": source["label"],
            "kind": source["kind"],
            "seed_url": source["seed_url"],
            "resolved_url": resolved_url,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "title": title,
            "text": text,
            "sections": sections,
            "outgoing_links": links,
        }

    def _drop_noise(self, soup: BeautifulSoup) -> None:
        for tag in soup(["script", "style", "noscript", "svg"]):
            tag.decompose()

    def _extract_title(self, soup: BeautifulSoup, source: Dict[str, Any]) -> str:
        if soup.title and soup.title.string:
            return soup.title.string.strip()

        h1 = soup.find("h1")
        if h1:
            return h1.get_text(" ", strip=True)

        return source["label"]

    def _extract_sections(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        sections: List[Dict[str, str]] = []
        current_heading = "Introduction"
        buffer: List[str] = []

        for node in soup.find_all(["h1", "h2", "h3", "p", "li"]):
            if node.name in {"h1", "h2", "h3"}:
                if buffer:
                    sections.append(
                        {
                            "heading": current_heading,
                            "text": self._clean_text(" ".join(buffer)),
                        }
                    )
                    buffer = []
                current_heading = node.get_text(" ", strip=True)
            else:
                text = node.get_text(" ", strip=True)
                if text:
                    buffer.append(text)

        if buffer:
            sections.append(
                {
                    "heading": current_heading,
                    "text": self._clean_text(" ".join(buffer)),
                }
            )

        return [section for section in sections if section["text"]]

    def _extract_links(self, soup: BeautifulSoup, base_url: str) -> List[Dict[str, str]]:
        links: List[Dict[str, str]] = []
        seen = set()

        for anchor in soup.find_all("a", href=True):
            href = urljoin(base_url, anchor["href"])
            parsed = urlparse(href)
            if parsed.scheme not in {"http", "https"}:
                continue

            dedupe_key = href
            if dedupe_key in seen:
                continue
            seen.add(dedupe_key)

            label = anchor.get_text(" ", strip=True)
            links.append(
                {
                    "url": href,
                    "label": label,
                }
            )

        return links

    def _clean_text(self, text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()
