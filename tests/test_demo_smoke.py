from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from kg_demo import artifact_store
from kg_demo.preload_local_state import ensure_local_demo_state
from kg_demo.ui_app import create_app


class DemoSmokeTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_state_dir = artifact_store.LOCAL_STATE_DIR
        artifact_store.LOCAL_STATE_DIR = Path(self.temp_dir.name) / "local_state"
        self.env = patch.dict(os.environ, {"KG_DEMO_LOCAL_ONLY": "true"})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        artifact_store.LOCAL_STATE_DIR = self.old_state_dir
        self.temp_dir.cleanup()

    def test_core_demo_endpoints(self):
        ensure_local_demo_state(reset=True)
        app = create_app()
        client = app.test_client()
        self.assertEqual(client.get("/api/health").status_code, 200)

        current = client.post("/api/actions/current-dose")
        self.assertEqual(current.status_code, 200)
        self.assertIn("75 mg once daily", current.get_json()["answer"])

        impact = client.post("/api/actions/impact-map")
        self.assertEqual(impact.status_code, 200)
        payload = impact.get_json()
        self.assertTrue(payload["impacted_sections"])
        self.assertTrue(payload["governing_sources"])


if __name__ == "__main__":
    unittest.main()
