from __future__ import annotations

import json
import os
from typing import Any, Dict, List

import httpx
from openai import AzureOpenAI

from .settings import load_env_file


def build_azure_openai_client(api_version: str | None = None) -> AzureOpenAI:
    load_env_file()
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    api_key = os.environ["AZURE_OPENAI_API_KEY"]
    api_version = api_version or os.environ.get("AZURE_OPENAI_MINI_API_VERSION", "2025-01-01-preview")
    verify_ssl = os.environ.get("AZURE_OPENAI_VERIFY_SSL", "false").lower() == "true"
    return AzureOpenAI(
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=endpoint,
        http_client=httpx.Client(verify=verify_ssl, timeout=60.0),
    )


def normalize_claim_candidates(claims: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not claims:
        return []

    deployment = os.environ.get("AZURE_OPENAI_MINI_DEPLOYMENT_NAME", "gpt-4o-mini")
    client = build_azure_openai_client()
    prompt = {
        "task": "Normalize claim candidates into compact structured claims without inventing facts.",
        "rules": [
            "Preserve source_id, chunk_id, claim_text, and evidence.",
            "Return JSON only.",
            "Prefer normalized_subject values like protocol.current_dose, protocol.visit_interval, sop.dose_change_citation_requirement, regulation.protocol_amendment_requirement.",
            "Use concise predicates such as equals, requires, changes_to, states.",
            "Use objects exactly grounded in evidence.",
            "Set claim_type to one of factual, requirement, recommendation, change_event.",
            "Infer claim_status as active unless the evidence explicitly states an older version or superseded fact.",
        ],
        "claims": claims,
    }
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a precise clinical-regulatory claim normalizer. Output valid JSON only."},
            {"role": "user", "content": json.dumps(prompt)},
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    content = response.choices[0].message.content or "{\"claims\": []}"
    payload = json.loads(content)
    if isinstance(payload, dict) and "claims" in payload:
        return payload["claims"]
    if isinstance(payload, list):
        return payload
    return []
