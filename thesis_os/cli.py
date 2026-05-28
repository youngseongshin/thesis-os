from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from thesis_os.alpha.collectors import load_evidence_csv
from thesis_os.alpha.local_db import connect, init_db, insert_evidence, list_evidence
from thesis_os.arki.health_check import check_demo_outputs
from thesis_os.arki.job_manifest import write_default_job_manifest
from thesis_os.arki.schema_lint import lint_schemas
from thesis_os.arki.vault_writer import VaultWriter
from thesis_os.gyeokja.action_queue import write_action_queue
from thesis_os.gyeokja.decision_card import decision_card_markdown
from thesis_os.gyeokja.feedback_interpreter import feedback_report_markdown
from thesis_os.gyeokja.prediction_ledger import append_prediction, read_predictions
from thesis_os.gyeokja.thesis_registry import build_sample_thesis, thesis_markdown
from thesis_os.models import Action, Prediction, utc_now


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="thesis-os")
    sub = parser.add_subparsers(dest="command", required=True)

    demo_parser = sub.add_parser("demo", help="Generate a runnable sample Thesis OS loop.")
    demo_parser.add_argument("--out", default="./demo_run", help="Output directory.")

    init_parser = sub.add_parser("init", help="Initialize a local Thesis OS workspace.")
    init_parser.add_argument("--out", default="./thesis_os_workspace", help="Output directory.")

    lint_parser = sub.add_parser("lint", help="Lint public schemas.")
    lint_parser.add_argument("--root", default=".", help="Repository root.")

    args = parser.parse_args(argv)
    if args.command == "demo":
        return run_demo(Path(args.out))
    if args.command == "init":
        return run_init(Path(args.out))
    if args.command == "lint":
        return run_lint(Path(args.root))
    parser.error("unknown command")
    return 2


def run_init(out: Path) -> int:
    vault = VaultWriter(out / "vault")
    vault.ensure_layout()
    write_default_job_manifest(out / "jobs.yaml")
    print(f"initialized Thesis OS workspace: {out}")
    return 0


def run_lint(root: Path) -> int:
    errors = lint_schemas(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("schema lint ok")
    return 0


def run_demo(out: Path) -> int:
    out.mkdir(parents=True, exist_ok=True)
    sample_csv = out / "sample_evidence.csv"
    _write_sample_evidence_csv(sample_csv)

    vault = VaultWriter(out / "vault")
    vault.ensure_layout()
    write_default_job_manifest(out / "jobs.yaml")

    evidence = load_evidence_csv(sample_csv)
    db_path = out / "local" / "thesis_os.db"
    conn = connect(db_path)
    init_db(conn)
    insert_evidence(conn, evidence)

    for item in evidence:
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

    thesis = build_sample_thesis(evidence)
    vault.write_note(
        "theses/THESIS-SAMPLE-AI-INFRA-001.md",
        title="Sample AI Infrastructure Thesis",
        body=thesis_markdown(thesis),
        frontmatter=thesis.to_dict(),
    )

    action = Action(
        id="ACTION-SAMPLE-001",
        entity=thesis.entity,
        action="watch",
        reason="Evidence supports active monitoring, but market reflection and base-rate checks are still required.",
        evidence_ids=thesis.evidence_ids,
        created_at=utc_now(),
        thesis_id=thesis.id,
        confidence="medium",
        next_check="Next weekly refresh",
    )
    vault.write_note(
        "decisions/ACTION-SAMPLE-001.md",
        title="Sample Decision Card",
        body=decision_card_markdown(thesis, action),
        frontmatter=action.to_dict(),
    )
    write_action_queue(out / "action_queue.json", [action])

    prediction = Prediction(
        id="PRED-SAMPLE-001",
        entity=thesis.entity,
        thesis_id=thesis.id,
        prediction="The sample basket should outperform its benchmark if evidence remains positive and market reflection is incomplete.",
        direction="relative_outperform",
        horizon="1m",
        confidence=0.55,
        created_at=utc_now(),
        evaluation_due="sample+1m",
        evidence_ids=thesis.evidence_ids,
        invalidation=thesis.invalidation,
    )
    ledger_path = out / "prediction_ledger.jsonl"
    append_prediction(ledger_path, prediction)
    latest_prediction = read_predictions(ledger_path)[-1]
    feedback_md = feedback_report_markdown(latest_prediction, absolute_return=0.04, benchmark_return=0.015)
    vault.write_note(
        "feedback/PRED-SAMPLE-001_feedback.md",
        title="Sample Feedback Report",
        body=feedback_md,
        frontmatter={
            "prediction_id": prediction.id,
            "entity": prediction.entity,
            "generated_at": utc_now(),
            "sample": True,
        },
    )

    manifest = {
        "db": str(db_path),
        "vault": str(out / "vault"),
        "evidence_count": len(list_evidence(conn)),
        "health": check_demo_outputs(out),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    conn.close()

    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


def _write_sample_evidence_csv(path: Path) -> None:
    rows = [
        {
            "id": "EVID-SAMPLE-001",
            "entity": "AI Infrastructure Basket",
            "source_type": "market_data",
            "source": "sample_quant_provider",
            "source_date": "2026-01-31",
            "claim": "Relative strength improved while volume expanded.",
            "interpretation": "Potential evidence of renewed institutional interest, not sufficient alone.",
            "confidence": "medium",
            "source_url": "",
            "tags": "sample|quant|relative-strength",
        },
        {
            "id": "EVID-SAMPLE-002",
            "entity": "AI Infrastructure Basket",
            "source_type": "youtube",
            "source": "sample_transcript_digest",
            "source_date": "2026-01-31",
            "claim": "Industry commentary points to sustained AI infrastructure capex.",
            "interpretation": "Qualitative support; must be cross-checked against official and market data.",
            "confidence": "low",
            "source_url": "https://example.com/sample",
            "tags": "sample|qualitative|youtube",
        },
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    raise SystemExit(main())

