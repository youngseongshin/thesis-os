---
sample: true
public_sanitized: true
not_financial_advice: true
source_policy: synthetic_example
object_type: social_collection_summary
owner_agent: alpha
review_agent: lattice
---

# Social Collection Summary

## 1. Purpose

Social collection helps Alpha detect emerging attention, narrative changes, and unusual discussion clusters.

It should not store raw private messages in public outputs. The public-safe artifact is a summarized, deduplicated, evidence-graded digest.

## 2. Collection Window

| Field | Sample Value |
|---|---|
| Window | Last 24 hours |
| Channels | Public or permissioned community/news surfaces |
| Raw storage | Private runtime only |
| Public artifact | Aggregated summary |
| Review owner | Lattice |

## 3. Signal Clusters

| Cluster | Intensity | Evidence Grade | Summary | Route |
|---|---:|---|---|---|
| AI server bottlenecks | high | C+ | Discussion shifted from generic AI demand to memory, networking, and substrate constraints | attach to AI-INFRA thesis |
| Humanoid robotics | medium | C | Mentions rising, but source quality uneven | quarantine until verified |
| Software agents | medium | B- | Product adoption examples increasing, monetization unclear | research packet |
| Rumor-like microcap cluster | high | D | High velocity, weak evidence, no official confirmation | reject |

## 4. What Lattice Should Use

Use social collection as:

- an early warning layer
- a narrative-quality signal
- a source of research questions
- a prompt for official-source verification

Do not use it as:

- final proof
- position sizing evidence
- a substitute for filings, financials, or market data
- a reason to override invalidation rules

## 5. Privacy And Storage Policy

Public-safe storage:

- topic cluster
- timestamp window
- intensity score
- source grade
- route decision
- link to verified evidence if available

Private-only or excluded:

- raw channel content
- author handles
- channel IDs
- message IDs
- personal conversations
- unlicensed raw data

## 6. Handoff To Screeners

Social signals can increase candidate priority only when paired with other evidence.

| Social Signal | Required Pairing |
|---|---|
| high attention | quant strength or official catalyst |
| new theme | analyst-report or filing evidence |
| rumor | reject or quarantine |
| repeated pain point | research question for Alpha |

