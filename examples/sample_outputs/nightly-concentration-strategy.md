---
sample: true
public_sanitized: true
not_financial_advice: true
source_policy: synthetic_example
object_type: nightly_concentration_strategy
owner_agent: lattice
input_agent: alpha
---

# Nightly Concentrated Strategy Review

## 1. Purpose

The concentrated strategy review asks a different question from a screener:

`What can hurt the portfolio because several positions depend on the same driver?`

It is a defensive judgment surface for holdings, watchlist names, and new candidates.

## 2. Sample Exposure Map

| Exposure Bucket | Sample Weight | Main Driver | Status |
|---|---:|---|---|
| AI Infrastructure Core | 38% | capex, accelerators, memory bandwidth | watch |
| Components / Substrate | 22% | server board complexity, packaging | review |
| Software / Platform | 16% | AI product adoption, monetization | neutral |
| Cash / Optionality | 24% | ability to redeploy | healthy |

The numbers are synthetic and included only to show how concentrated review works.

## 3. Common Driver Check

| Driver | Affected Buckets | Risk |
|---|---|---|
| Hyperscaler capex | AI Infrastructure, Components | high |
| Advanced packaging bottleneck | AI Infrastructure, Components | medium |
| Rate and multiple compression | AI Infrastructure, Software | medium |
| Earnings revision cycle | All equity buckets | high |
| Social narrative crowding | AI Infrastructure, Humanoid watchlist | medium |

## 4. Lattice Roundtable

| Entity | Current State | Judgment | Reason |
|---|---|---|---|
| AI-INFRA | Thesis active | hold | evidence positive but crowding risk rising |
| SUBSTRATE | Thesis needs update | review | possible upgrade if margin linkage improves |
| AI-SW | Watchlist | watch | product signal early, revenue link weak |
| CROWD-MOMO | Candidate | reject for now | extension risk too high |
| CASH | Optionality | maintain | useful while candidate quality is mixed |

## 5. Increase / Hold / Decrease / Exit Logic

| Action | Required Condition |
|---|---|
| Increase | thesis strengthened, feedback positive, risk budget available |
| Hold | thesis intact, no new asymmetric action |
| Decrease | thesis weaker, exposure too crowded, or forward feedback deteriorates |
| Exit | thesis invalidated or better opportunity exists |
| Watch | evidence interesting but not yet actionable |

## 6. Risk Breakers

1. Quant signal stays strong but 1 week and 1 month feedback turns negative.
2. Social signal rises while official or financial evidence weakens.
3. AI infrastructure candidates all depend on one capex narrative.
4. Lattice promotes a candidate before devil's advocate review.
5. The Top 5 queue becomes a momentum list rather than a portfolio-review queue.

## 7. Action Queue

| Action ID | Owner | Action | Reason |
|---|---|---|---|
| ACTION-SAMPLE-STRAT-001 | Alpha | Refresh market DB after close | avoid stale judgment |
| ACTION-SAMPLE-STRAT-002 | Alpha | Attach screener features to Top 5 queue | make selection auditable |
| ACTION-SAMPLE-STRAT-003 | Lattice | Run concentrated exposure check | avoid hidden common-driver risk |
| ACTION-SAMPLE-STRAT-004 | Arki | Update wiki index and SSOT note | improve retrieval |

## 8. Prediction Ledger Hooks

Only measurable claims should enter the ledger.

Examples:

- `AI-INFRA should outperform benchmark over 1 month if evidence remains positive.`
- `SUBSTRATE should not be upgraded unless customer-link evidence improves.`
- `CROWD-MOMO should underperform after rejection if extension risk is real.`

