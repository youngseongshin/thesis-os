# Vault Governance

Thesis OS treats the vault as an operational memory system. A vault that accepts arbitrary generated notes will eventually become hard to search, hard to trust, and unsafe to publish.

The public pattern is inspired by a live Research OS, but generalized for open-source use.

## Core Principle

All generated vault writes should go through policy.

```text
document type -> policy resolver -> canonical path -> owner check -> frontmatter -> write -> index
```

Agents should not invent new folders during a run.

## Governance Layers

| Layer | Purpose |
|---|---|
| Vault document policy | Maps document types to canonical directories and filename rules |
| Vault codeowners | Defines which agent may create or modify each path |
| Vault writer | Central write API that applies frontmatter, tags, and safe paths |
| Layout compatibility layer | Preserves legacy aliases while routing new writes to canonical paths |
| Consistency validator | Checks that every policy rule has an owner and every owner path is valid |
| Wiki index | Builds retrieval surfaces from canonical notes |
| Cleanup policy | Removes empty, duplicate, stale, or raw-heavy folders after migration |

## Canonical Write Rules

1. Every generated document must have a document type.
2. Every document type must resolve to one canonical directory.
3. Every canonical directory must have an owner agent.
4. Agents may read across the vault, but should write only to owned paths.
5. Shared paths require explicit scope notes.
6. Legacy paths can be read for migration, but new writes should go to canonical paths.
7. Raw data should be summarized before entering the semantic vault.

## Public Example Layout

| Public Path | Owner | Purpose |
|---|---|---|
| `evidence/` | Alpha | Source-grounded facts, market snapshots, freshness notes |
| `screeners/` | Alpha | Candidate lists, feature snapshots, discovery queues |
| `alerts/` | Alpha | Intraday alert notes for holdings/watchlists |
| `theses/` | Lattice | Living thesis cards |
| `decisions/` | Lattice | Decision cards, roundtable notes, action rationale |
| `feedback/` | Lattice | Prediction, screener, and judgment feedback |
| `jobs/` | Arki | Recurring job manifests and run notes |
| `wiki/` | Arki | Generated retrieval index |
| `ssot/` | Arki | Canonical layout and policy notes |

Private deployments can use deeper domain paths, but the governance rule is the same: document type resolves to a canonical owner-controlled path.

## Document Policy

A vault document policy should define:

- document type
- owner agent
- description
- canonical directory
- filename template
- required context fields
- collision policy
- public/private handling

Example:

```yaml
rules:
  thesis-card:
    owner_agent: lattice
    directory: "theses/{entity_slug}"
    filename: "{thesis_id}.md"
    required_context: ["entity_slug", "thesis_id"]
```

## Codeowners

Codeowners prevent cross-agent write drift.

Example:

```yaml
codeowners:
  - path: "screeners/"
    owner: alpha
    notes: "Alpha writes candidates; Lattice reads them for judgment."
  - path: "theses/"
    owner: lattice
    notes: "Lattice writes thesis cards; Alpha links evidence."
```

The important rule:

```text
read broadly, write narrowly
```

All agents may read what they need. Only the owner writes the canonical object.

## Frontmatter Minimum

Every durable vault note should include frontmatter that helps agents retrieve and audit it.

Minimum:

```yaml
type: thesis-card
owner_agent: lattice
created_at: 2026-01-31
updated_at: 2026-01-31
entity: AI Infrastructure Basket
status: active_watch
source_policy: policy_resolved
```

Recommended:

- `thesis_id`
- `evidence_ids`
- `candidate_id`
- `action_id`
- `prediction_id`
- `feedback_id`
- `freshness`
- `confidence`
- `tags`
- `public_sanitized`

## Hot, Canonical, And Archive Surfaces

Thesis OS should separate storage surfaces:

| Surface | Purpose | Retention |
|---|---|---|
| Hot | Recent alerts, breaking signals, active working notes | Short |
| Canonical | Thesis, evidence, decisions, predictions, feedback | Durable |
| Archive | Raw files, old generated artifacts, superseded snapshots | Cold/private |

This prevents high-frequency collectors from flooding the long-term vault.

## Cleanup Rules

Vault cleanup should be policy-driven:

- delete empty folders after confirming no job writes there
- merge duplicate folders into canonical paths
- stop generators that write to legacy locations
- move root-alias or stray outputs into the vault root or reject them
- replace many timestamped raw files with daily/weekly rollups
- keep summaries in the vault and move raw media/cache outside the vault

Cleanup should be logged as a migration, not done silently.

## Validator Checks

A vault policy validator should check:

1. Every document rule has a directory and filename.
2. Every document rule has an owner.
3. Every rule directory is covered by a codeowner path.
4. Policy owner and codeowner owner match.
5. No rule resolves outside the vault.
6. Legacy aliases do not receive new writes.
7. Required frontmatter exists for generated notes.

## Agent Responsibilities

### Alpha

- writes evidence, screeners, alerts, and source freshness
- must not write final Lattice decisions
- should summarize raw qualitative sources before vault write

### Lattice

- writes theses, decisions, predictions, and feedback interpretation
- must not rewrite raw evidence
- should link every judgment to evidence and future feedback

### Arki

- owns policies, validators, migration notes, wiki index, and cleanup plans
- must not make investment judgments
- should block or flag writes that violate canonical layout

## Why This Matters

Without vault governance, agent systems drift:

- duplicate folders appear
- old paths keep receiving new writes
- raw collectors flood the vault
- agents retrieve stale notes
- users cannot tell which document is canonical
- feedback cannot link back to the original judgment

With vault governance, the vault becomes a durable research memory layer rather than a folder full of generated markdown.

