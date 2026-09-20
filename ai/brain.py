"""NEXO brain boundary."""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class Intent(str, Enum):
    STOP="STOP"; FORWARD="FORWARD"; BACK="BACK"; LEFT="LEFT"; RIGHT="RIGHT"; STATUS="STATUS"; PING="PING"; UNKNOWN="UNKNOWN"

@dataclass(frozen=True)
class BrainDecision:
    intent: Intent
    command: str | None
    reason: str

_COMMANDS={Intent.STOP:"STOP",Intent.FORWARD:"FORWARD",Intent.BACK:"BACK",Intent.LEFT:"LEFT",Intent.RIGHT:"RIGHT",Intent.STATUS:"STATUS",Intent.PING:"PING"}

def decide(intent: Intent)->BrainDecision:
    command=_COMMANDS.get(intent)
    if command is None: return BrainDecision(Intent.UNKNOWN,None,"No safe controller command")
    return BrainDecision(intent,command,"Mapped to allowlisted controller command")
