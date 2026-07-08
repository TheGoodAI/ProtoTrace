"""Deterministic impact/governance rules for all 8 pilot-pool amendment archetypes.

Kept separate from impact_analyzer.py (the live demo's rule engine, which only covers
dose and visit-interval) so extending coverage here cannot regress the live demo or its
benchmark.

Rules are derived from general ICH E6(R2) / FDA / EMA protocol-amendment principles, not
from data/pilot_annotation/gold_labels_v1.json. They are scored against a separate,
non-overlapping held-out pool (data/pilot_annotation/heldout_pool_v1.json), so the
resulting F1 is a held-out check rather than a fit to already-seen labels.
"""
from __future__ import annotations

from typing import Any, Dict, List

# Fixed governing-reference slugs, matching data/pilot_annotation's scheme.
FDA_AMEND = "fda_21cfr312_30"
FDA_SAFETY = "fda_21cfr312_32"
EMA_AMEND = "ema_gcpqa_s3"
EMA_CONSENT = "ema_gcpqa_s5"
ICH_AMEND = "ich_e6r2_s4_5"
SOP_DOSE = "sop_dosechange_01"
SOP_SAFETY = "sop_safetymonitoring_02"
SOP_ELIG = "sop_eligibility_03"

# archetype -> (impacted_sections, governing_sources), reasoned independently per
# archetype from what a protocol amendment of that kind would plausibly require a
# reviewer to check, using the same fixed 20-code section scheme and 8-item reference
# pool the pilot pool itself draws from.
ARCHETYPE_RULES: Dict[str, Dict[str, List[str]]] = {
    "dose_change": {
        "impacted_sections": ["5.2", "5.3", "11.3"],
        "governing_sources": [FDA_AMEND, EMA_AMEND, ICH_AMEND, SOP_DOSE],
    },
    "eligibility_change": {
        "impacted_sections": ["4.1", "4.2"],
        "governing_sources": [FDA_AMEND, EMA_AMEND, ICH_AMEND, SOP_ELIG],
    },
    "visit_schedule_change": {
        "impacted_sections": ["8.1", "8.2", "7.2"],
        "governing_sources": [FDA_AMEND, EMA_AMEND, ICH_AMEND],
    },
    "safety_monitoring_change": {
        "impacted_sections": ["11.3", "8.1", "11.4"],
        "governing_sources": [FDA_SAFETY, ICH_AMEND, SOP_SAFETY],
    },
    "endpoint_change": {
        "impacted_sections": ["7.1", "7.2", "12.1"],
        "governing_sources": [FDA_AMEND, ICH_AMEND],
    },
    "informed_consent_change": {
        "impacted_sections": ["9.1", "9.2"],
        "governing_sources": [EMA_CONSENT, ICH_AMEND, FDA_AMEND],
    },
    "discontinuation_criteria_change": {
        "impacted_sections": ["10.1", "10.2"],
        "governing_sources": [FDA_AMEND, ICH_AMEND],
    },
    "drug_interaction_change": {
        "impacted_sections": ["6.1", "6.2", "5.3"],
        "governing_sources": [FDA_AMEND, ICH_AMEND],
    },
}


def analyze_pilot_scenario(archetype: str) -> Dict[str, Any]:
    """Deterministic prediction for a pilot-pool scenario, keyed only on its archetype
    label (the same signal impact_analyzer.py uses: the amendment's subject type)."""
    rule = ARCHETYPE_RULES.get(archetype)
    if rule is None:
        return {"impacted_sections": [], "governing_sources": []}
    return {
        "impacted_sections": list(rule["impacted_sections"]),
        "governing_sources": list(rule["governing_sources"]),
    }
