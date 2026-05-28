from __future__ import annotations

from pathlib import Path

from thesis_os.adapters.base import SourceEvent
from thesis_os.alpha.collectors import load_evidence_csv
from thesis_os.alpha.local_db import connect, init_db, insert_evidence
from thesis_os.arki.vault_writer import VaultWriter
from thesis_os.models import Evidence, utc_now


def event_to_evidence(event: SourceEvent, confidence: str = "low") -> Evidence:
    return Evidence(
        id=event.id.replace("SRC-", "EVID-"),
        entity=event.entity,
        source_type=event.channel,
        source=event.source,
        source_url=event.url,
        source_date=event.source_date,
        collected_at=utc_now(),
        claim=event.content,
        interpretation="Converted from qualitative source event. Review before high-conviction use.",
        confidence=confidence,
        tags=["qualitative", event.channel],
    )


def ingest_evidence_to_workspace(workspace: str | Path, records: list[Evidence]) -> dict[str, object]:
    workspace = Path(workspace)
    vault = VaultWriter(workspace / "vault")
    vault.ensure_layout()
    conn = connect(workspace / "local" / "thesis_os.db")
    init_db(conn)
    count = insert_evidence(conn, records)
    conn.close()

    for item in records:
        vault.write_note(
            f"evidence/{item.id}.md",
            title=f"Evidence: {item.entity}",
            body="\n".join(
                [
                    f"**Claim:** {item.claim}",
                    "",
                    f"**Interpretation:** {item.interpretation or 'No interpretation provided.'}",
                    "",
                    f"**Source:** {item.source}",
                ]
            ),
            frontmatter=item.to_dict(),
        )

    return {"workspace": str(workspace), "evidence_count": count}


def ingest_csv_to_workspace(csv_path: str | Path, workspace: str | Path) -> dict[str, object]:
    records = load_evidence_csv(csv_path)
    return ingest_evidence_to_workspace(workspace, records)

