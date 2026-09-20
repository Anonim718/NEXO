"""Atomic JSON persistence for non-critical NEXO state."""
import json
from pathlib import Path
from typing import Any

class JsonStateStore:
    def __init__(self, path: str | Path):
        self.path = Path(path)
    def save(self, state: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
        tmp.replace(self.path)
    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text(encoding="utf-8"))
