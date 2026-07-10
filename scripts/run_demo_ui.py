import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

os.environ.setdefault("KG_LOCAL_STATE_DIR", str(ROOT / "local_state_ui"))

from kg_demo.preload_local_state import ensure_local_demo_state
from kg_demo.ui_app import create_app


if __name__ == "__main__":
    os.environ["KG_DEMO_LOCAL_ONLY"] = "true"
    # Default to a clean baseline (75 mg) on every launch so external demos are deterministic
    # and never start from a previous session's leftover amendments. Set
    # KG_RESET_DEMO_ON_START=false to preserve in-progress state across restarts.
    ensure_local_demo_state(reset=os.environ.get("KG_RESET_DEMO_ON_START", "true").lower() == "true")
    app = create_app()
    host = os.environ.get("KG_DEMO_HOST", "127.0.0.1")
    port = int(os.environ.get("KG_DEMO_PORT", "8000"))
    app.run(host=host, port=port, debug=False)
