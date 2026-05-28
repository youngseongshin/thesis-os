from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from thesis_os.cli import run_demo, run_lint


class DemoTest(unittest.TestCase):
    def test_demo_generates_core_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "demo"
            self.assertEqual(run_demo(out), 0)
            self.assertTrue((out / "local" / "thesis_os.db").exists())
            self.assertTrue((out / "vault" / "theses" / "THESIS-SAMPLE-AI-INFRA-001.md").exists())
            self.assertTrue((out / "prediction_ledger.jsonl").exists())
            self.assertTrue((out / "manifest.json").exists())

    def test_schema_lint(self) -> None:
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(run_lint(root), 0)


if __name__ == "__main__":
    unittest.main()

