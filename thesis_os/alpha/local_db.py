from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Iterable

from thesis_os.models import Evidence


def connect(path: str | Path) -> sqlite3.Connection:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS evidence (
            id TEXT PRIMARY KEY,
            entity TEXT NOT NULL,
            source_type TEXT NOT NULL,
            source TEXT NOT NULL,
            source_date TEXT NOT NULL,
            collected_at TEXT NOT NULL,
            claim TEXT NOT NULL,
            interpretation TEXT,
            confidence TEXT NOT NULL,
            source_url TEXT,
            tags_json TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS collector_runs (
            id TEXT PRIMARY KEY,
            collector TEXT NOT NULL,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            status TEXT NOT NULL,
            records INTEGER NOT NULL DEFAULT 0
        );
        """
    )
    conn.commit()


def insert_evidence(conn: sqlite3.Connection, records: Iterable[Evidence]) -> int:
    count = 0
    for record in records:
        conn.execute(
            """
            INSERT OR REPLACE INTO evidence (
                id, entity, source_type, source, source_date, collected_at,
                claim, interpretation, confidence, source_url, tags_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.id,
                record.entity,
                record.source_type,
                record.source,
                record.source_date,
                record.collected_at,
                record.claim,
                record.interpretation,
                record.confidence,
                record.source_url,
                json.dumps(record.tags, ensure_ascii=False),
            ),
        )
        count += 1
    conn.commit()
    return count


def list_evidence(conn: sqlite3.Connection) -> list[dict[str, object]]:
    rows = conn.execute("SELECT * FROM evidence ORDER BY source_date, id").fetchall()
    out: list[dict[str, object]] = []
    for row in rows:
        item = dict(row)
        item["tags"] = json.loads(item.pop("tags_json") or "[]")
        out.append(item)
    return out

