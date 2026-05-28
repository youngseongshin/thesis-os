# Adapter Contracts

Thesis OS keeps public methods separate from private runtime credentials.

Adapters are interfaces, not bundled private integrations.

## QuantProvider

Use for structured market or company data.

Required behavior:

- read-only by default
- return normalized `Evidence`
- include source date and collected time
- include provider name and confidence
- never silently fabricate missing data

## QualitativeProvider

Use for Telegram, Facebook, YouTube, newsletter, community, or filing text sources.

Required behavior:

- return `SourceEvent`
- preserve source timestamp and URL when available
- store minimal raw content when possible
- mark transcript or metadata fallback honestly

## DeliveryAdapter

Use for optional delivery to Telegram, email, Slack, web, or stdout.

Required behavior:

- delivery should not mutate investment state
- return a delivery result
- never log credentials

## Private Adapter Rule

Real broker APIs, Telegram sessions, browser cookies, Gmail OAuth, and paid feeds should live in private repositories or local runtime directories.

