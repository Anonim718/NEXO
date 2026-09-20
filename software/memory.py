"""Bounded, non-critical robot memory store."""
from dataclasses import dataclass, field

@dataclass
class Memory:
    entries: list[str] = field(default_factory=list)
    max_entries: int = 100
    def remember(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip(): return
        self.entries.append(value.strip())
        self.entries = self.entries[-self.max_entries:]
    def recent(self, limit: int = 10) -> list[str]:
        return self.entries[-max(0, limit):]
