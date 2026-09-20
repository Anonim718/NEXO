"""Shared NEXO software state model."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RobotState(str, Enum):
    STOP = "STOP"
    FORWARD = "FORWARD"
    BACK = "BACK"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    LOW_BATTERY = "LOW_BATTERY"
    FAULT = "FAULT"


@dataclass(frozen=True)
class RobotSnapshot:
    state: RobotState
    distance_cm: int | None = None
    battery_percent: int | None = None
    fault: str | None = None
