from software.core.safety import forward_allowed, safe_state
from software.core.state import RobotSnapshot, RobotState


def test_forward_blocked_by_obstacle():
    snapshot = RobotSnapshot(RobotState.STOP, distance_cm=15)
    assert not forward_allowed(snapshot)
    assert safe_state(snapshot) is RobotState.STOP


def test_forward_blocked_by_low_battery():
    snapshot = RobotSnapshot(RobotState.STOP, distance_cm=100, battery_percent=10)
    assert not forward_allowed(snapshot)


def test_fault_is_never_cleared_by_safety_helper():
    snapshot = RobotSnapshot(RobotState.FAULT, distance_cm=100)
    assert safe_state(snapshot) is RobotState.FAULT


def test_clear_path_allows_forward():
    snapshot = RobotSnapshot(RobotState.STOP, distance_cm=100, battery_percent=80)
    assert forward_allowed(snapshot)
