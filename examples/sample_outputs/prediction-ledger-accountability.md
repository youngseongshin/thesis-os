---
sample: true
public_sanitized: true
not_financial_advice: true
source_policy: synthetic_example
---

# Prediction Ledger Accountability Sample

This synthetic sample shows how Thesis OS turns predictions into an accountability ledger.

It is not a model-performance claim. It includes both hits and misses because the point is process auditability, not selective promotion.

## Registered Predictions

| ID | Entity | Thesis type | Native horizon | Direction | Registered before outcome | Process score | Result score | Hit | Failure mode |
|---|---|---|---|---|---:|---:|---:|---|---|
| `PRED-SYN-001` | AI Infrastructure Basket | `cycle_rerating` | 3m | relative outperform | yes | 0.89 | 0.64 | yes | none |
| `PRED-SYN-002` | Crowded Momentum Basket | `timing_trade` | 1m | relative outperform | yes | 0.78 | 0.31 | no | already_priced_in |
| `PRED-SYN-003` | Quality Compounder Basket | `compounder_hold` | 1y | relative outperform | yes | 0.94 | 0.48 | no | timing_failure |

## Interpretation

- `PRED-SYN-001` had a clean process and a positive outcome. Preserve the evidence mix, but do not treat one hit as proof of alpha.
- `PRED-SYN-002` had a decent process but failed because the signal was already crowded. Tighten extension and market-reflection checks.
- `PRED-SYN-003` shows why native horizons matter. A weak 1m timing read should not invalidate a 1y compounder thesis unless the original thesis claimed short-term timing.

## Accountability Rules

1. Record the prediction before the outcome.
2. Keep the original thesis, evidence, invalidation, and horizon unchanged.
3. Score process quality separately from market outcome.
4. Show hits and misses together.
5. Feed failure modes back into screener rules and Lattice judgment.

## Disclaimer

This is a synthetic workflow example. It is not financial advice, investment research, a recommendation, or a representation of live portfolio performance.
