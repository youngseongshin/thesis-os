---
sample: true
public_sanitized: true
not_financial_advice: true
source_policy: synthetic_example
object_type: screener_discovery_results
owner_agent: alpha
---

# Screener Discovery Results

## 1. Purpose

Screeners are candidate generators. They do not decide.

The purpose is to surface review-worthy names from repeatable evidence, then let Lattice decide whether the candidate deserves a thesis update, watchlist entry, portfolio review, or rejection.

## 2. Discovery Channels

| Channel | Role |
|---|---|
| Quantitative screeners | Find strength, quality, cycle, flow, revision, and risk patterns |
| Social collection | Detect narrative intensity and emerging discussion clusters |
| Analyst-report collection | Detect revision language, catalyst mentions, and industry framing |

## 3. Candidate Table

| Candidate ID | Entity | Main Screener | Score | Channel Overlap | Feature Snapshot |
|---|---|---|---:|---:|---|
| SCR-AI-INFRA-001 | AI-INFRA | quality-cycle-momentum | 86 | 3/3 | RS 88, volume 1.7x, smart flow 0.72 |
| SCR-SUBSTRATE-001 | SUBSTRATE | cycle-revision | 82 | 3/3 | RS 82, revision 0.66, extension risk 0.22 |
| SCR-SEMICAP-001 | SEMICAP | capex-beta | 77 | 2/3 | RS 79, catalyst score 0.61 |
| SCR-HUMANOID-001 | HUMANOID | social-emergence | 71 | 2/3 | social intensity high, evidence grade mixed |
| SCR-AI-SW-001 | AI-SW | early-revision | 69 | 2/3 | product signal early, monetization unproven |

## 4. Selection Rules

The integrated screener favors:

- multi-channel confirmation
- positive price/volume evidence without extreme extension
- flow quality over raw volume alone
- catalyst proximity
- evidence quality
- thesis registry fit
- measurable forward-feedback potential

It penalizes:

- stale data
- pure social heat
- excessive extension
- weak evidence grade
- untestable narratives
- candidates that cannot be linked to a thesis or feedback horizon

## 5. Output Routing

| Candidate | Route |
|---|---|
| AI-INFRA | Top 5 deep dive and thesis review |
| SUBSTRATE | Thesis update candidate |
| SEMICAP | Watchlist review |
| HUMANOID | Evidence quarantine |
| AI-SW | Research packet |

## 6. Lattice Handoff

Alpha sends Lattice a compact packet:

- candidate ID
- selected features
- reason selected
- evidence IDs
- current thesis link if one exists
- rejection reasons if the candidate is noisy
- suggested feedback horizons

Lattice then decides, challenges, and records measurable judgments.

