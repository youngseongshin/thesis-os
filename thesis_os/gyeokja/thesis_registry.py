from __future__ import annotations

from thesis_os.models import Evidence, Thesis, utc_now


def build_sample_thesis(evidence: list[Evidence]) -> Thesis:
    evidence_ids = [item.id for item in evidence]
    return Thesis(
        id="THESIS-SAMPLE-AI-INFRA-001",
        entity="AI Infrastructure Basket",
        status="active",
        claim="AI infrastructure demand remains investable only if evidence confirms both demand persistence and market under-reaction.",
        assumptions=[
            "Demand indicators are not merely inventory build.",
            "Consensus has not fully absorbed the evidence.",
            "The relevant value-chain companies can convert demand into earnings.",
        ],
        evidence_ids=evidence_ids,
        risks=[
            "The thesis can be right but already priced in.",
            "Supplier benefits may be diluted by ASP pressure or capacity constraints.",
        ],
        invalidation=[
            "Two consecutive evidence updates weaken demand persistence.",
            "Price and consensus already reflect the positive scenario.",
        ],
        updated_at=utc_now(),
        tags=["sample", "ai-infra", "thesis-os"],
    )


def thesis_markdown(thesis: Thesis) -> str:
    return "\n".join(
        [
            f"**Entity:** {thesis.entity}",
            f"**Status:** {thesis.status}",
            "",
            "## Claim",
            thesis.claim,
            "",
            "## Assumptions",
            *[f"- {item}" for item in thesis.assumptions],
            "",
            "## Evidence",
            *[f"- `{item}`" for item in thesis.evidence_ids],
            "",
            "## Risks",
            *[f"- {item}" for item in thesis.risks],
            "",
            "## Invalidation",
            *[f"- {item}" for item in thesis.invalidation],
        ]
    )

