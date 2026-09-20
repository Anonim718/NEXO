"""Pure software safety rules shared by simulation and higher layers."""

from __future__ import annotations

from software.core.state import RobotState, RobotSnapshot


def forward_allowed(snapshot: RobotSnapshot, obstacle_stop_cm: int = 20) -> bool:
    if snapshot.state in {RobotState.LOW_BATTERY, RobotState.FAULT}:
        return False
    if snapshot.distance_cm is not None and snapshot.distance_cm <= obstacle_stop_cm:
        return False
    if snapshot.battery_percent is not None and snapshot.battery_percent <= 10:
        return False
    return True


def safe_state(snapshot: RobotSnapshot, obstacle_stop_cm: int = 20) -> RobotState:
    if snapshot.state in {RobotState.LOW_BATTERY, RobotState.FAULT}:
        return snapshot.state
    if not forward_allowed(snapshot, obstacle_stop_cm):
        return RobotState.STOP
    return snapshot.state
