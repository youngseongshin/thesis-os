from __future__ import annotations

import csv
from pathlib import Path

from thesis_os.models import Evidence, utc_now


def load_evidence_csv(path: str | Path) -> list[Evidence]:
    """Load a simple public sample CSV into evidence records."""

    records: list[Evidence] = []
    with Path(path).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(
                Evidence(
                    id=row["id"],
                    entity=row["entity"],
                    source_type=row.get("source_type", "other"),
                    source=row.get("source", "sample"),
                    source_date=row["source_date"],
                    collected_at=row.get("collected_at") or utc_now(),
                    claim=row["claim"],
                    interpretation=row.get("interpretation", ""),
                    confidence=row.get("confidence", "medium"),
                    source_url=row.get("source_url", ""),
                    tags=[tag.strip() for tag in row.get("tags", "").split("|") if tag.strip()],
                )
            )
    return records

