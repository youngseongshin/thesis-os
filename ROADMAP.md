# Roadmap

Thesis OS is intentionally small at the public core. The roadmap expands it without mixing in private broker credentials, private chat logs, or paid raw data.

## v0.1: Public Core

- Three-agent model: Alpha, Lattice, Arki
- Evidence / Thesis / Action / Prediction / Feedback schemas
- Markdown vault writer
- Local SQLite demo database
- Prediction ledger
- Deterministic feedback report
- Schema lint and CI

## v0.2: Adapter Contracts

- Provider interface for quant data
- Provider interface for qualitative intelligence
- Delivery interface for Telegram/email/web output
- Public sample adapters
- Private adapter boundary documentation

## v0.3: Workspace Runtime

- Workspace initialization
- Agent-specific CLI commands
- Job manifest validation
- Health check report
- Freshness status

## v0.4: Judgment Quality

- Evidence grade policy
- Decision card policy
- Devil's advocate gate policy
- Base-rate and market-reflection checklist
- Action queue lifecycle

## v0.5: Feedback Engine

- Horizon-based prediction evaluation
- MFE / MAE
- Absolute and relative return
- Failure mode classification
- Thesis update suggestions

## v1.0: Reproducible Thesis Loop

- Pluggable adapters
- Stable schemas
- Reproducible demo workspace
- Clear public/private boundary
- Minimal but complete thesis -> prediction -> feedback workflow
