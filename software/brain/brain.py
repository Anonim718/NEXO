"""Deterministic NEXO intent -> state -> safety -> command layer.

This module deliberately contains no LLM calls and no direct hardware access.
An online/offline AI adapter can translate natural language into Intent values,
after which this deterministic layer validates and produces controller commands.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Intent(str, Enum):
    STOP = "STOP"
    FORWARD = "FORWARD"
    BACK = "BACK"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    STATUS = "STATUS"
    PING = "PING"


class RobotMode(str, Enum):
    IDLE = "IDLE"
    MOVING = "MOVING"
    FAULT = "FAULT"


@dataclass
class RobotState:
    mode: RobotMode = RobotMode.IDLE
    distance_cm: Optional[float] = None
    battery_percent: Optional[float] = None
    last_command: str = "STOP"
    fault: Optional[str] = None


@dataclass(frozen=True)
class BrainDecision:
    command: str
    reason: str


@dataclass
class SafetyLimits:
    obstacle_stop_cm: float = 30.0
    minimum_battery_percent: float = 10.0


@dataclass
class NexoBrain:
    limits: SafetyLimits = field(default_factory=SafetyLimits)
    state: RobotState = field(default_factory=RobotState)

    def decide(self, intent: Intent) -> BrainDecision:
        if intent == Intent.STOP:
            return BrainDecision("STOP", "explicit_stop")

        if intent == Intent.PING:
            return BrainDecision("PING", "connectivity_check")

        if intent == Intent.STATUS:
            return BrainDecision("STATUS", "status_request")

        if self.state.mode == RobotMode.FAULT:
            return BrainDecision("STOP", "fault_lockout")

        if intent == Intent.FORWARD:
            if self._obstacle_blocking():
                return BrainDecision("STOP", "obstacle_detected")
            if self._battery_low():
                return BrainDecision("STOP", "battery_low")
            return BrainDecision("FORWARD", "path_clear")

        if intent in {Intent.BACK, Intent.LEFT, Intent.RIGHT}:
            if self._battery_low():
                return BrainDecision("STOP", "battery_low")
            return BrainDecision(intent.value, "validated_motion")

        return BrainDecision("STOP", "unknown_intent")

    def apply(self, intent: Intent) -> BrainDecision:
        decision = self.decide(intent)
        self.state.last_command = decision.command

        if decision.command == "STOP":
            self.state.mode = RobotMode.FAULT if self.state.fault else RobotMode.IDLE
        elif decision.command in {"FORWARD", "BACK", "LEFT", "RIGHT"}:
            self.state.mode = RobotMode.MOVING

        return decision

    def set_fault(self, reason: str) -> None:
        self.state.fault = reason
        self.state.mode = RobotMode.FAULT

    def clear_fault(self) -> None:
        self.state.fault = None
        self.state.mode = RobotMode.IDLE

    def _obstacle_blocking(self) -> bool:
        d = self.state.distance_cm
        return d is not None and d > 0 and d <= self.limits.obstacle_stop_cm

    def _battery_low(self) -> bool:
        b = self.state.battery_percent
        return b is not None and b <= self.limits.minimum_battery_percent
