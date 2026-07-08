from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from kg_demo import artifact_store
from kg_demo.eval_dataset import _regulatory_tasks, build_eval_dataset
from kg_demo.preload_local_state import ensure_local_demo_state
from kg_demo.rag_baselines import run_claim_graph_method, synthesize_rag_answer


class EvaluationIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_state_dir = artifact_store.LOCAL_STATE_DIR
        artifact_store.LOCAL_STATE_DIR = Path(self.temp_dir.name) / "local_state"
        self.env = patch.dict(
            os.environ,
            {
                "KG_DEMO_LOCAL_ONLY": "true",
                "KG_EVAL_METHOD_SET": "release",
                "KG_ALLOW_HEURISTIC_FALLBACK": "false",
            },
        )
        self.env.start()

    def tearDown(self):
        self.env.stop()
        artifact_store.LOCAL_STATE_DIR = self.old_state_dir
        self.temp_dir.cleanup()

    def test_rule_retrieval_uses_prompt_without_gold(self):
        ensure_local_demo_state(reset=True)
        task = _regulatory_tasks()[3]
        prediction = run_claim_graph_method(
            {"task_type": "rule_answer", "prompt": task["prompt"]}
        )
        self.assertEqual(prediction["answer"], "implement immediately then notify FDA and IRB")
        self.assertTrue(prediction["matched_claim_id"].endswith("immediate_hazard_exception"))

    def test_release_dataset_contains_no_rule_subject_routing_key(self):
        dataset = build_eval_dataset()
        regulatory_tasks = [task for task in dataset["tasks"] if task["task_type"] == "rule_answer"]
        self.assertTrue(regulatory_tasks)
        self.assertTrue(all("rule_subject" not in task["gold"] for task in regulatory_tasks))

    def test_llm_baseline_fails_closed(self):
        from kg_demo import rag_baselines

        cache_path = Path(self.temp_dir.name) / "cache.json"
        with patch.object(rag_baselines, "EVAL_CACHE_PATH", cache_path), patch.object(
            rag_baselines,
            "build_azure_openai_client",
            side_effect=RuntimeError("offline"),
        ):
            with self.assertRaisesRegex(RuntimeError, "no fallback result was recorded"):
                synthesize_rag_answer(
                    "What is current?",
                    "current_fact",
                    [],
                    deployment_name="test-model",
                    api_version="test-version",
                )

        self.assertFalse(cache_path.exists())


if __name__ == "__main__":
    unittest.main()
