"""Hardware-independent arm controller interface."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ArmCommand(str, Enum):
    HOME = "HOME"
    STOP = "STOP"
    GRAB = "GRAB"
    RELEASE = "RELEASE"


@dataclass(frozen=True)
class ArmResult:
    command: ArmCommand
    accepted: bool
    reason: str


class ArmController:
    """Safe software boundary for future servo/arm implementations."""

    def execute(self, command: ArmCommand) -> ArmResult:
        return ArmResult(command, False, "No physical arm driver configured")
