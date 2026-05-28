# Local Database

The local database is the structured memory of Thesis OS.

## Why Local

Local storage makes research reproducible, auditable, and independent from a single hosted provider.

## Minimum Tables

- `evidence`
- `theses`
- `actions`
- `predictions`
- `feedback`
- `collector_runs`

## Freshness

Each dataset should expose:

- latest source date
- latest collected time
- row count
- provider
- confidence
- failure count

Freshness is part of evidence quality. A stale dataset should not be treated as current.

