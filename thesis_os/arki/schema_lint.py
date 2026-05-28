from __future__ import annotations

import json
from pathlib import Path


def lint_schemas(root: str | Path) -> list[str]:
    root = Path(root)
    schema_dir = root / "schemas"
    errors: list[str] = []
    if not schema_dir.exists():
        return [f"missing schema directory: {schema_dir}"]
    for path in sorted(schema_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid json: {exc}")
            continue
        for required in ("$schema", "title", "type"):
            if required not in data:
                errors.append(f"{path}: missing {required}")
    return errors

