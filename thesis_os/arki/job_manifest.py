from __future__ import annotations

from pathlib import Path


DEFAULT_JOBS_YAML = """# Thesis OS recurring job manifest example.
jobs:
  - id: alpha-daily-market-refresh
    owner_agent: alpha
    cadence: "weekday 18:00 local"
    command: "thesis-os demo --out ./demo_run"
    outputs:
      - "local/thesis_os.db"
      - "vault/evidence/"
    freshness_sla: "1 trading day"
    failure_policy: "log and alert"
    enabled: true

  - id: lattice-prediction-feedback
    owner_agent: lattice
    cadence: "weekday 19:00 local"
    command: "thesis-os demo --out ./demo_run"
    outputs:
      - "vault/feedback/"
      - "prediction_ledger.jsonl"
    freshness_sla: "1 trading day"
    failure_policy: "preserve previous output and log failure"
    enabled: true

  - id: arki-health-check
    owner_agent: arki
    cadence: "daily 08:00 local"
    command: "thesis-os lint --root ."
    outputs:
      - "health report"
    freshness_sla: "1 day"
    failure_policy: "block release until fixed"
    enabled: true
"""


def write_default_job_manifest(path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(DEFAULT_JOBS_YAML, encoding="utf-8")
    return path
