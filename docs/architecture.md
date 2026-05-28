# Architecture

Thesis OS is organized as a loop.

```text
Quant + qualitative sources
  -> Alpha evidence collection
  -> Local DB + vault memory
  -> Lattice thesis and judgment
  -> Prediction ledger and action queue
  -> Feedback evaluator
  -> Arki system maintenance
```

## Runtime Boundary

Thesis OS defines the investment judgment core. It does not require a specific agent runtime.

The same core can be executed by:

- CLI commands
- cron / launchd / systemd jobs
- GitHub Actions
- OpenClaw
- a custom application or service

The original long-running deployment uses OpenClaw as the reference runtime. OpenClaw supplies persistent agents, chat gateways, local skills, recurring jobs, memory promotion, logs, and recovery workflows. Thesis OS supplies the schemas, local DB, vault notes, screeners, thesis cards, prediction ledger, feedback reports, and dashboard.

See [Runtime Adapters](runtime-adapters.md) and [OpenClaw Reference Runtime](openclaw-reference-runtime.md).

## Layers

### Data Sources

External and local sources feed the system:

- Prices and volume
- Investor flow
- Fundamentals
- Filings
- Consensus
- Short sale and stock loan
- News and newsletters
- Telegram channels
- Facebook posts
- YouTube transcripts
- Internal notes

After market close, Alpha should refresh local KR/US listed-equity snapshots before downstream screeners and Lattice judgments run.

### Alpha Layer

Alpha normalizes raw inputs into evidence records and local DB snapshots.

Output examples:

- `evidence/*.md`
- `local/thesis_os.db`
- `market_snapshots`
- `intraday_alerts`
- `research_packet.json`
- `screener_candidates.json`
- `vault/screeners/{candidate}.md`
- `vault/alerts/intraday-alerts.md`

Alpha discovery has three daily channels:

1. quantitative screeners
2. social/community collection
3. analyst-report collection

Integrated screening compresses the combined queue to Top 5 candidates for Lattice portfolio-review.

### Lattice Layer

Lattice turns evidence into investment objects.

Output examples:

- `theses/{entity}.md`
- `decisions/{date}_{entity}.md`
- `prediction_ledger.jsonl`
- `action_queue.json`

### Arki Layer

Arki keeps the system operational.

Output examples:

- schema lint reports
- recurring job manifests
- health reports
- migration notes
- vault policy checks

### Feedback Layer

The system evaluates prior predictions, screener candidates, and Lattice decisions against outcomes.

Output examples:

- `feedback/{date}_feedback.md`
- `feedback_metrics.json`
- updated thesis status
- screener forward-performance reviews
- judgment feedback reports for entity-level and portfolio-inclusion decisions

### Vault Wiki / SSOT Layer

Arki builds generated indexes over the vault so agents can find canonical, current objects without scanning stale duplicate notes.

Output examples:

- `vault/wiki/index.md`
- `vault/ssot/canonical-locations.md`
