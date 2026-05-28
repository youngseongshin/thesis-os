---
sample: true
public_sanitized: true
not_financial_advice: true
source_policy: synthetic_example
object_type: nightly_top5_deep_dive
owner_agent: alpha
review_agent: lattice
---

# Nightly Top 5 Deep Dive

## 1. Purpose

The nightly Top 5 deep dive converts noisy discovery into a short portfolio-review queue.

Top 5 does not mean "buy." It means "review first." Lattice must decide whether each candidate belongs in the portfolio, watchlist, thesis audit queue, or rejection bin.

## 2. Inputs

| Input Layer | Owner | Sample Source |
|---|---|---|
| Local market DB | Alpha | KR/US close snapshots, volume, flows |
| Quant screeners | Alpha | quality, cycle, momentum, revision, flow |
| Social collection | Alpha | summarized community and social clusters |
| Analyst-report collection | Alpha | revision tone and catalyst mentions |
| Thesis registry | Lattice | existing thesis cards and invalidation rules |
| Vault memory | Arki | prior decisions, feedback, wiki index |

## 3. Top 5 Queue

| Rank | Candidate | Channel Overlap | Score | Why It Surfaced | Lattice Route |
|---:|---|---:|---:|---|---|
| 1 | AI-INFRA | 3/3 | 86 | Quant strength plus rising evidence quality | Deep dive |
| 2 | SUBSTRATE | 3/3 | 82 | Cycle recovery plus component bottleneck narrative | Thesis card update |
| 3 | SEMICAP | 2/3 | 77 | Capex sensitivity and improving revision tone | Watchlist review |
| 4 | HUMANOID | 2/3 | 71 | Social intensity high, evidence quality mixed | Quarantine until verified |
| 5 | AI-SW | 2/3 | 69 | Product-cycle narrative improving, price action early | Small research packet |

## 4. Candidate Notes

### 4.1 AI-INFRA

- Quant signal is strong enough for review.
- Social signal is specific to supply bottlenecks rather than generic AI excitement.
- Analyst signal suggests estimate revision potential.
- Main risk is crowding.

Decision need:

`Does the basket still have unpriced earnings revision potential?`

### 4.2 SUBSTRATE

- Appears in both cycle and component screeners.
- May benefit from AI server board complexity.
- Needs stronger customer and margin linkage.

Decision need:

`Is this a true thesis upgrade or just a second-order sympathy trade?`

### 4.3 SEMICAP

- Quant profile is improving but catalyst distance is unclear.
- Sensitive to order timing and capex headlines.

Decision need:

`Can the next 1 to 3 month catalyst be identified?`

### 4.4 HUMANOID

- Social attention rose sharply.
- Evidence quality is mixed.
- Lattice should not promote social heat into a thesis without official or financial evidence.

Decision need:

`Reject, quarantine, or request evidence?`

### 4.5 AI-SW

- Early signal, not mature enough for action.
- Needs better linkage between product adoption and revenue.

Decision need:

`Keep on watchlist or request a focused research note?`

## 5. Roundtable Packet

| Candidate | Proposed Next Step | Required Evidence |
|---|---|---|
| AI-INFRA | Deep dive | valuation, revision, crowding check |
| SUBSTRATE | Thesis update | customer linkage and margin sensitivity |
| SEMICAP | Watchlist review | catalyst calendar |
| HUMANOID | Evidence quarantine | official source confirmation |
| AI-SW | Research packet | monetization evidence |

## 6. What Gets Written

| Vault Area | Artifact |
|---|---|
| `vault/screeners/` | daily Top 5 queue |
| `vault/evidence/` | linked evidence records |
| `vault/theses/` | thesis update candidates |
| `vault/decisions/` | Lattice roundtable notes |
| `vault/feedback/` | future forward-return evaluation |
| `vault/wiki/` | current index for agent retrieval |

