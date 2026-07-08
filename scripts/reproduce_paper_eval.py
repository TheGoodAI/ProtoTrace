"""One-command reproduction of the demo-paper evaluation.

Runs the fair-baseline objective benchmark and the multi-amendment update-stability
experiment, then prints the objective-task table and points at the generated artifacts.

Usage:
    python scripts/reproduce_paper_eval.py

Environment:
    Forces the release method set: claim system + ablations vs. a deterministic
    version-aware lexical proxy. Optional LLM experiments are separate and fail closed;
    they are not mixed into the paper table.
"""

from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

os.environ.setdefault("KG_EVAL_METHOD_SET", "release")
os.environ.setdefault("KG_ALLOW_HEURISTIC_FALLBACK", "false")

from kg_demo.eval_runner import (  # noqa: E402
    OBJECTIVE_SUMMARY_MD_PATH,
    PAPER_SUMMARY_MD_PATH,
    RESULTS_PATH,
    run_comparison,
)
from kg_demo.eval_dataset import write_eval_dataset  # noqa: E402
from kg_demo.settings import load_env_file  # noqa: E402
from kg_demo.update_stability_eval import (  # noqa: E402
    UPDATE_STABILITY_MD,
    run_update_stability_experiment,
)


if __name__ == "__main__":
    load_env_file()
    write_eval_dataset()

    print("[1/2] Running fair objective benchmark ...")
    run_comparison()
    print("[2/2] Running multi-amendment update-stability experiment ...")
    run_update_stability_experiment()

    print("\n=== Objective-task summary (non-circular gold) ===\n")
    print(OBJECTIVE_SUMMARY_MD_PATH.read_text(encoding="utf-8"))

    print("Artifacts written:")
    for path in (RESULTS_PATH, PAPER_SUMMARY_MD_PATH, OBJECTIVE_SUMMARY_MD_PATH, UPDATE_STABILITY_MD):
        print(f"  - {path}")
