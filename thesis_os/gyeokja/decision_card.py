from __future__ import annotations

from thesis_os.gyeokja.devil_advocate import devil_advocate_check
from thesis_os.models import Action, Thesis


def decision_card_markdown(thesis: Thesis, action: Action) -> str:
    checks = devil_advocate_check(thesis)
    return "\n".join(
        [
            f"**Entity:** {action.entity}",
            f"**Action:** {action.action}",
            f"**Confidence:** {action.confidence}",
            f"**Thesis:** `{action.thesis_id}`",
            "",
            "## Reason",
            action.reason,
            "",
            "## Evidence",
            *[f"- `{item}`" for item in action.evidence_ids],
            "",
            "## Devil's Advocate",
            *[f"- {item}" for item in checks],
            "",
            "## Next Check",
            action.next_check or "Not specified",
        ]
    )

