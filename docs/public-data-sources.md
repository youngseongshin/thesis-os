# Public Data Sources

Thesis OS is built as a data-source agnostic framework. The public repository ships a guaranteed bundled sample CSV quickstart, optional no-key Yahoo/Stooq live mode, and CSV adapters. A serious deployment should plug in the best public or licensed data sources available to the user.

The point is not to make Thesis OS the only data provider. The point is to make good data auditable once it enters the loop: evidence -> screener candidate -> thesis -> prediction -> feedback.

## Source Map

| Layer | Public or common sources | Thesis OS use |
|---|---|---|
| Price and volume | Yahoo Finance chart endpoint, Stooq, Yahoo Finance-compatible CSV exports, FinanceDataReader, OpenBB, exchange-provided files | market snapshots, momentum/relative-strength screeners, forward-return feedback |
| Fundamentals | SEC EDGAR, edgartools, DART/OpenDART, company IR pages, public annual reports | evidence records, thesis assumptions, invalidation checks |
| Korea listed equities | pykrx, KRX-derived files, FinanceDataReader, OpenDART, broker exports where permitted | KR market DB refresh, quant screeners, flow/short-sale overlays |
| Macro and rates | FRED, central banks, public statistical agencies, treasury datasets | regime evidence, benchmark context, risk checks |
| Supply-chain and trade proxy | government customs APIs, import/export statistics, public trade datasets | sector proxy evidence, semiconductor/AI infra supply-chain checks |
| Alternative public datasets | Nasdaq Data Link free datasets, Hugging Face datasets, Kaggle datasets with compatible licenses | thematic research, sector classifiers, text/event datasets |
| Qualitative sources | official company newsrooms, filings, public transcripts, public YouTube transcripts, public newsletters/blogs | qualitative evidence, counterarguments, thesis updates |

## Adapter Principle

Use the richest source you are allowed to use, but normalize it into simple Thesis OS objects:

```text
raw source -> adapter -> Evidence / MarketSnapshot / ScreenerCandidate -> Vault + Local DB
```

For example:

- A first-time user can run `thesis-os quickstart-stock` with the bundled sample CSV, then add `--live` for no-key Yahoo/Stooq public data or `--price-csv` for their own dataset.
- A quant user can replace the default CSV with OpenBB, FinanceDataReader, pykrx, or their own research database.
- A fundamental investor can add SEC/DART filings as evidence before Lattice builds thesis cards.
- A supply-chain investor can add customs or export/import proxy data as sector evidence.

## Production Cautions

Always check:

- license and terms of use
- data delay
- survivorship bias
- corporate-action adjustment policy
- exchange redistribution rules
- whether a dataset is suitable for research, redistribution, or commercial use

Thesis OS can make a judgment loop auditable. It cannot make low-quality, stale, or unauthorized data safe.
