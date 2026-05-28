from __future__ import annotations

import json
from pathlib import Path

from thesis_os.models import Action


def write_action_queue(path: str | Path, actions: list[Action]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [action.to_dict() for action in actions]
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path

