"""Reset the local demo state to the intended 75 mg baseline.

Run this before any external demo or meeting so the UI starts from a known, clean state
(active dose = 75 mg once daily, visit interval = 21 days) rather than whatever amendments a
previous session left behind.

Usage:
    python scripts/reset_demo_baseline.py
"""

from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

os.environ.setdefault("KG_DEMO_LOCAL_ONLY", "true")
# Target the same state directory the demo UI serves from (see run_demo_ui.py); without this
# the script resets the eval state in local_state/ while the UI keeps serving local_state_ui/.
os.environ.setdefault("KG_LOCAL_STATE_DIR", str(ROOT / "local_state_ui"))

from kg_demo.preload_local_state import ensure_local_demo_state  # noqa: E402
from kg_demo.rag_baselines import run_claim_graph_method  # noqa: E402


if __name__ == "__main__":
    ensure_local_demo_state(reset=True)
    current = run_claim_graph_method({"task_type": "current_fact", "gold": {}}, mode="full")
    print("Demo state reset to baseline.")
    print(f"  active dose: {current.get('current_dose')}")
    print(f"  sources:     {current.get('supporting_sources')}")
