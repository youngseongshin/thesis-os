from __future__ import annotations

from pathlib import Path


def check_demo_outputs(root: str | Path) -> dict[str, bool]:
    root = Path(root)
    return {
        "local_db": (root / "local" / "thesis_os.db").exists(),
        "vault_evidence": (root / "vault" / "evidence").exists(),
        "vault_theses": (root / "vault" / "theses").exists(),
        "prediction_ledger": (root / "prediction_ledger.jsonl").exists(),
        "feedback": (root / "vault" / "feedback").exists(),
    }

