# Qualitative Intelligence

Qualitative intelligence converts unstructured sources into evidence candidates.

## Supported Channel Types

- Telegram channel messages
- Facebook posts
- YouTube transcripts and subtitles
- Newsletters
- News articles
- Filings and official press releases
- Community discussions
- Internal notes

## Collector Rules

Collectors should:

- Respect source terms and rate limits.
- Store minimal raw data when possible.
- Deduplicate repeated content.
- Preserve source URLs and timestamps.
- Separate source text from model interpretation.
- Mark transcript fallback and metadata-only cases honestly.

## Output Types

Qualitative collectors should produce:

- source event
- evidence note
- digest
- thesis update candidate
- action queue candidate

## Telegram / Facebook / YouTube

Public code should provide adapter interfaces and sample collectors. Real sessions, cookies, channel IDs, browser states, and private credentials must stay outside the public repository.

