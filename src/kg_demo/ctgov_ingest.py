"""Real amendment data ingestion from ClinicalTrials.gov.

ClinicalTrials.gov exposes, for every registered study, a full version history with
machine-readable diffs. We use two endpoints:

* ``/api/v2/studies/{nct}``            -- current normalized record (v2 public API)
* ``/api/int/studies/{nct}/history``   -- list of versions with ``moduleLabels``
                                          (the registry's own record of which modules
                                          changed at each version)
* ``/api/int/studies/{nct}/history/{v}`` -- the full study record at version ``v``

The ``moduleLabels`` on each version are the sponsor/registry-declared changed sections.
They are produced independently of our system, so they give a *non-circular* gold signal
for "what changed" -- exactly what the synthetic benchmark lacked.

Everything is GET-only over public-domain data and cached under ``data/raw/ctgov/`` so the
benchmark build is reproducible and offline after the first fetch.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

from .settings import DATA_DIR

CTGOV_V2 = "https://clinicaltrials.gov/api/v2"
CTGOV_INT = "https://clinicaltrials.gov/api/int"
RAW_DIR = DATA_DIR / "raw" / "ctgov"
USER_AGENT = "kg-demo-research/1.0 (academic; protocol-amendment-study)"

# Fields we track across versions. Each maps a friendly key to an extractor over the
# protocolSection of a study record.
_TRACKED_MODULES = {
    "eligibility",
    "arms interventions",
    "outcomes",
    "design",
    "status",
}


def _get_json(url: str, cache_path: Optional[Path] = None, retries: int = 3) -> Any:
    if cache_path and cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    last_err: Optional[Exception] = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            if cache_path:
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_text(json.dumps(payload), encoding="utf-8")
            return payload
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:  # noqa: PERF203
            last_err = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {url}: {last_err}")


def fetch_history(nct: str) -> List[Dict[str, Any]]:
    """Return the list of version metadata dicts (version, date, status, moduleLabels)."""
    url = f"{CTGOV_INT}/studies/{nct}/history"
    payload = _get_json(url, RAW_DIR / f"{nct}_history.json")
    return payload.get("changes", [])


def fetch_version(nct: str, version: int) -> Dict[str, Any]:
    """Return the protocolSection of a study at a specific version index."""
    url = f"{CTGOV_INT}/studies/{nct}/history/{version}"
    payload = _get_json(url, RAW_DIR / f"{nct}_v{version}.json")
    study = payload.get("study", payload)
    return study.get("protocolSection", {})


def _outcomes_repr(outcomes: List[Dict[str, Any]]) -> Optional[str]:
    if not outcomes:
        return None
    return " | ".join(
        f"{o.get('measure', '')}::{(o.get('timeFrame', '') or '')}" for o in outcomes
    ) or None


def extract_fields(protocol_section: Dict[str, Any]) -> Dict[str, Optional[str]]:
    """Extract a richer set of comparable fields from a protocolSection.

    Coverage is deliberately broad within the five tracked modules (eligibility,
    arms/interventions, outcomes, design, status) so that structured diffs recover more of the
    registry-declared module changes.
    """
    elig = protocol_section.get("eligibilityModule", {})
    arms = protocol_section.get("armsInterventionsModule", {})
    outcomes = protocol_section.get("outcomesModule", {})
    design = protocol_section.get("designModule", {})
    status = protocol_section.get("statusModule", {})

    interventions = arms.get("interventions", []) or []
    intervention_repr = " | ".join(
        f"{i.get('type', '')}:{i.get('name', '')}:{(i.get('description', '') or '')[:160]}"
        for i in interventions
    )
    arm_groups = arms.get("armGroups", []) or []
    arm_repr = " | ".join(
        f"{a.get('label', '')}:{a.get('type', '')}:{(a.get('description', '') or '')[:120]}"
        for a in arm_groups
    )
    enrollment = design.get("enrollmentInfo", {}) or {}
    design_info = design.get("designInfo", {}) or {}
    masking = (design_info.get("maskingInfo", {}) or {}).get("masking")

    return {
        # eligibility module
        "eligibility_criteria": (elig.get("eligibilityCriteria") or "").strip() or None,
        "minimum_age": elig.get("minimumAge"),
        "maximum_age": elig.get("maximumAge"),
        "sex": elig.get("sex"),
        "healthy_volunteers": _as_str(elig.get("healthyVolunteers")),
        "study_population": (elig.get("studyPopulation") or "").strip() or None,
        "sampling_method": elig.get("samplingMethod"),
        # arms / interventions module
        "interventions": intervention_repr or None,
        "arm_groups": arm_repr or None,
        # outcomes module
        "primary_outcomes": _outcomes_repr(outcomes.get("primaryOutcomes", []) or []),
        "secondary_outcomes": _outcomes_repr(outcomes.get("secondaryOutcomes", []) or []),
        # design module
        "enrollment": _as_str(enrollment.get("count")),
        "study_type": design.get("studyType"),
        "phases": ",".join(design.get("phases", []) or []) or None,
        "allocation": design_info.get("allocation"),
        "intervention_model": design_info.get("interventionModel"),
        "primary_purpose": design_info.get("primaryPurpose"),
        "masking": masking,
        # status module
        "overall_status": status.get("overallStatus"),
        "why_stopped": (status.get("whyStopped") or "").strip() or None,
        "start_date": (status.get("startDateStruct", {}) or {}).get("date"),
        "completion_date": (status.get("completionDateStruct", {}) or {}).get("date"),
        "primary_completion_date": (status.get("primaryCompletionDateStruct", {}) or {}).get("date"),
        "status_verified_date": status.get("statusVerifiedDate"),
    }


def _as_str(value: Any) -> Optional[str]:
    return None if value is None else str(value)


def build_amendment_records(nct: str, max_versions: int = 40) -> Dict[str, Any]:
    """Fetch a study's full version history and build per-amendment records.

    For each consecutive version pair we record the registry-declared changed modules
    (``moduleLabels``, the non-circular gold) and the before/after values of the tracked
    fields, plus which tracked fields actually changed.
    """
    history = fetch_history(nct)
    if not history:
        return {"nct_id": nct, "versions": 0, "amendments": []}

    history = history[:max_versions]
    version_fields: Dict[int, Dict[str, Optional[str]]] = {}
    for entry in history:
        v = entry["version"]
        version_fields[v] = extract_fields(fetch_version(nct, v))

    amendments: List[Dict[str, Any]] = []
    versions_sorted = sorted(version_fields)
    for prev_v, cur_v in zip(versions_sorted, versions_sorted[1:]):
        prev_fields = version_fields[prev_v]
        cur_fields = version_fields[cur_v]
        changed_fields = [
            key for key in cur_fields if (prev_fields.get(key) or "") != (cur_fields.get(key) or "")
        ]
        cur_meta = next((e for e in history if e["version"] == cur_v), {})
        amendments.append(
            {
                "nct_id": nct,
                "from_version": prev_v,
                "to_version": cur_v,
                "date": cur_meta.get("date"),
                "registry_changed_modules": cur_meta.get("moduleLabels", []),
                "changed_fields": changed_fields,
                "before": prev_fields,
                "after": cur_fields,
            }
        )

    return {
        "nct_id": nct,
        "versions": len(versions_sorted),
        "first_date": history[0].get("date"),
        "last_date": history[-1].get("date"),
        "amendments": amendments,
    }


def discover_amended_trials(
    target: int = 25,
    page_size: int = 100,
    query_term: str = "dose amendment protocol",
    advanced_filter: str = "AREA[StudyType]INTERVENTIONAL AND AREA[Phase]PHASE2",
) -> List[str]:
    """Find NCT IDs of interventional trials that actually have substantive amendments.

    We page through the v2 search API and keep studies whose version history shows at least
    one amendment touching a tracked module (eligibility, arms/interventions, outcomes, or
    design), so the resulting benchmark contains real, non-trivial changes.
    """
    kept: List[str] = []
    page_token: Optional[str] = None
    scanned = 0
    while len(kept) < target and scanned < target * 12:
        params = {
            "query.term": query_term,
            "filter.advanced": advanced_filter,
            "pageSize": str(page_size),
            "fields": "NCTId",
            "format": "json",
        }
        if page_token:
            params["pageToken"] = page_token
        url = f"{CTGOV_V2}/studies?{urllib.parse.urlencode(params)}"
        payload = _get_json(url)
        studies = payload.get("studies", [])
        if not studies:
            break
        for study in studies:
            scanned += 1
            nct = (
                study.get("protocolSection", {})
                .get("identificationModule", {})
                .get("nctId")
            )
            if not nct:
                continue
            try:
                history = fetch_history(nct)
            except RuntimeError:
                continue
            substantive = any(
                any(_label_is_tracked(lbl) for lbl in entry.get("moduleLabels", []))
                for entry in history
            )
            if len(history) >= 2 and substantive:
                kept.append(nct)
                if len(kept) >= target:
                    break
        page_token = payload.get("nextPageToken")
        if not page_token:
            break
    return kept


def _label_is_tracked(label: str) -> bool:
    low = label.lower()
    return any(token in low for token in ("eligibility", "arm", "intervention", "outcome", "design"))
