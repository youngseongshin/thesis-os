from __future__ import annotations

from pathlib import Path

from thesis_os.alpha.local_db import connect, init_db, list_evidence
from thesis_os.arki.job_manifest import write_default_job_manifest
from thesis_os.arki.vault_writer import VaultWriter
from thesis_os.models import Evidence


def init_workspace(root: str | Path) -> Path:
    root = Path(root)
    (root / "local").mkdir(parents=True, exist_ok=True)
    vault = VaultWriter(root / "vault")
    vault.ensure_layout()
    write_default_job_manifest(root / "jobs.yaml")
    conn = connect(root / "local" / "thesis_os.db")
    init_db(conn)
    conn.close()
    return root


def load_workspace_evidence(root: str | Path) -> list[Evidence]:
    root = Path(root)
    conn = connect(root / "local" / "thesis_os.db")
    init_db(conn)
    rows = list_evidence(conn)
    conn.close()
    return [
        Evidence(
            id=str(row["id"]),
            entity=str(row["entity"]),
            source_type=str(row["source_type"]),
            source=str(row["source"]),
            source_url=str(row.get("source_url") or ""),
            source_date=str(row["source_date"]),
            collected_at=str(row["collected_at"]),
            claim=str(row["claim"]),
            interpretation=str(row.get("interpretation") or ""),
            confidence=str(row["confidence"]),
            tags=list(row.get("tags") or []),
        )
        for row in rows
    ]

