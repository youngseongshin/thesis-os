from __future__ import annotations

import json
from pathlib import Path

from thesis_os.models import Prediction


def append_prediction(path: str | Path, prediction: Prediction) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(prediction.to_dict(), ensure_ascii=False) + "\n")
    return path


def read_predictions(path: str | Path) -> list[dict[str, object]]:
    path = Path(path)
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

