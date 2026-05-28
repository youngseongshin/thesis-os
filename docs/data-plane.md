# Quant Data Plane

The quant data plane collects structured market and company data.

## Common Inputs

- Daily and intraday prices
- Volume and turnover
- Foreign and institutional flows
- Short sale and stock loan data
- Program trading
- Fundamentals and financial statements
- Consensus and estimate revisions
- Filings and official disclosures
- Export/import and macro data

## Public Sources Are First-Class Inputs

The public core starts with a no-key Yahoo Finance chart endpoint, but Thesis OS is intentionally adapter-based. Users can plug in strong public and open analysis sources such as:

- OpenBB and FinanceDataReader for broad market data workflows
- pykrx and KRX-derived files for Korea listed-equity research
- SEC EDGAR and edgartools for US filings
- DART/OpenDART for Korean filings
- FRED, central banks, and statistical agencies for macro context
- government customs/export-import APIs for supply-chain proxy evidence

See [Public Data Sources](public-data-sources.md). The important rule is to preserve source metadata, date, delay, and confidence so Lattice can judge evidence quality.

## Screener Role

Screeners convert the quant data plane into thesis-review candidates. They should preserve the feature snapshot that caused selection so the system can later evaluate whether the rule worked.

Examples:

- relative strength + volume expansion
- earnings revision + flow confirmation
- short pressure unwind
- quality + cycle acceleration
- official catalyst proximity

## Provider Contract

Every provider should produce records with:

- `provider`
- `source`
- `source_date`
- `collected_at`
- `entity_id`
- `metric`
- `value`
- `unit`
- `confidence`

## Local Database

The default local store is SQLite for portability. Larger deployments can use DuckDB or Postgres.

Storage rules:

- Use stable entity identifiers.
- Keep provider and source metadata.
- Preserve raw timestamps.
- Avoid silent fallback.
- Make refresh jobs idempotent.
- Write via temp files or transactions.

## Public Adapter Boundary

Open-source providers should use public or sample data. Broker, paid data, and authenticated sources should be implemented as private adapters.
