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

## Skill Outputs

Qualitative collection should feed skills, not create unmanaged notes.

| Skill | Input | Output | Route |
|---|---|---|---|
| Social collector | channel/community updates | topic clusters and evidence candidates | Alpha evidence memory |
| Facebook collector | public or permissioned posts | summarized post themes | Alpha evidence memory |
| YouTube scout | transcripts, subtitles, or metadata fallback | source note and thesis implications | Alpha -> Lattice |
| Deep Alpha | cross-source signals | non-obvious candidates and evidence gaps | Alpha -> Lattice |
| Deep Dive | Top 5 candidates | structured research packet | Alpha -> Lattice |

Each skill should mark source confidence and fallback status. A metadata-only video note is not the same as a transcript-based source note.
