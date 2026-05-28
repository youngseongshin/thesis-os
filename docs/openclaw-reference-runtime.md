# OpenClaw Reference Runtime

The original long-running deployment that inspired Thesis OS runs on OpenClaw.

Thesis OS itself is runtime-agnostic. OpenClaw is best understood as a reference runtime for operating the Thesis OS loop continuously with local agents, skills, memory, chat gateways, scheduled jobs, and logs.

## Role Split

| Thesis OS role | OpenClaw runtime responsibility |
|---|---|
| Alpha | run evidence collectors, market-data adapters, screeners, social/video/report summarizers, and source-quality checks |
| Lattice | review thesis cards, run devil's advocate gates, make portfolio/watchlist judgments, register predictions, interpret feedback |
| Arki | govern schemas, vault layout, memory policy, recurring jobs, launch health, migrations, and public/private boundaries |

## What OpenClaw Adds

OpenClaw is useful when the system needs to move beyond one-off CLI commands:

- long-running agent processes
- Telegram or chat gateways
- local skill execution
- recurring job orchestration
- memory capture and promotion
- vault write discipline
- logs, heartbeats, and operational recovery
- model and cost routing

In this structure, Thesis OS is the investment judgment core, while OpenClaw is the operational shell that keeps the loop alive.

```text
OpenClaw runtime
  -> schedules Alpha evidence work
  -> routes Lattice judgment requests
  -> lets Arki enforce schemas, memory, and vault policy
  -> delivers summaries through chat or web surfaces
  -> writes logs and recovery notes

Thesis OS core
  -> schemas
  -> local DB
  -> markdown vault
  -> screeners
  -> thesis cards
  -> prediction ledger
  -> feedback reports
  -> dashboard
```

## Public / Private Boundary

The public repo should include:

- role contracts
- sample OpenClaw agent maps
- sample harness contracts
- safe job examples
- public adapter interfaces

The public repo should not include:

- real Telegram tokens
- broker credentials
- OAuth sessions
- browser state
- private vault contents
- private portfolio holdings
- paid raw data

## Design Principle

Keep Thesis OS useful without OpenClaw, but document OpenClaw as the proven way to run the same loop as a persistent local multi-agent system.
