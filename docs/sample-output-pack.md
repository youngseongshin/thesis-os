# Sample Output Pack

The sample output pack shows how Thesis OS feels in operation without exposing private data.

Path:

```text
examples/sample_outputs/
```

All files in the pack are synthetic and marked:

```yaml
sample: true
public_sanitized: true
not_financial_advice: true
source_policy: synthetic_example
```

## Included Outputs

| Output | Why It Exists |
|---|---|
| Thesis card | Shows how a living investment thesis is structured |
| Nightly Top 5 deep dive | Shows the collection -> screening -> judgment handoff |
| Concentrated strategy review | Shows portfolio-level common-driver thinking |
| Screener discovery results | Shows how Alpha compresses candidates |
| Screener performance feedback | Shows the closed loop from signal to outcome |
| Social collection summary | Shows how qualitative signals are summarized safely |

## Design Principle

Public examples should demonstrate the loop, not reveal the deployment.

The examples should never include:

- real account data
- private holdings or exact portfolio weights
- raw community messages
- private channel IDs or user handles
- secrets, tokens, cookies, OAuth state, or API keys
- paid-feed raw data
- non-public company information

## How To Use

New contributors can read the sample outputs in this order:

1. `screener-discovery-results.md`
2. `nightly-top5-deep-dive.md`
3. `thesis-card-ai-infrastructure-basket.md`
4. `nightly-concentration-strategy.md`
5. `screener-performance-feedback.md`
6. `social-collection-summary.md`

This order follows the operating loop:

```text
collect -> screen -> compress -> judge -> record -> evaluate -> improve
```

