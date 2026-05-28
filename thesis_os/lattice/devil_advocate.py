from __future__ import annotations

from thesis_os.models import Thesis


def devil_advocate_check(thesis: Thesis) -> list[str]:
    """Deterministic red-team checklist for a thesis."""

    checks = [
        "What would make this thesis false?",
        "Is the evidence official, observed, inferred, or social?",
        "Is the market already pricing the conclusion?",
        "Which assumption has the weakest base rate?",
        "What data would distinguish demand from inventory build?",
    ]
    if len(thesis.evidence_ids) < 2:
        checks.append("Evidence count is thin; require at least two independent sources.")
    if not thesis.invalidation:
        checks.append("No invalidation condition found; block high-conviction action.")
    return checks

