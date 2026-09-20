"""Deterministic high-level goal planner for NEXO."""
from dataclasses import dataclass
from enum import Enum

class Goal(str, Enum):
    STOP = "STOP"
    MOVE_FORWARD = "MOVE_FORWARD"
    MOVE_BACK = "MOVE_BACK"
    TURN_LEFT = "TURN_LEFT"
    TURN_RIGHT = "TURN_RIGHT"

class Action(str, Enum):
    STOP = "STOP"
    FORWARD = "FORWARD"
    BACK = "BACK"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

@dataclass(frozen=True)
class PlannedStep:
    action: Action
    duration_ms: int
    reason: str

class NexoPlanner:
    """Convert validated goals into bounded, deterministic action sequences."""
    MAX_STEP_MS = 1000

    def plan(self, goal: Goal, duration_ms: int = 500) -> list[PlannedStep]:
        duration_ms = max(1, min(duration_ms, self.MAX_STEP_MS))
        mapping = {
            Goal.STOP: (Action.STOP, 1, "Explicit stop requested"),
            Goal.MOVE_FORWARD: (Action.FORWARD, duration_ms, "Move forward goal"),
            Goal.MOVE_BACK: (Action.BACK, duration_ms, "Move back goal"),
            Goal.TURN_LEFT: (Action.LEFT, duration_ms, "Turn left goal"),
            Goal.TURN_RIGHT: (Action.RIGHT, duration_ms, "Turn right goal"),
        }
        action, step_duration, reason = mapping[goal]
        return [PlannedStep(action, step_duration, reason)]
