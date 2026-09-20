"""Central NEXO software configuration."""
from dataclasses import dataclass

@dataclass(frozen=True)
class NexoConfig:
    serial_baud: int = 115200
    obstacle_stop_cm: float = 30.0
    minimum_battery_percent: float = 10.0
    planner_max_step_ms: int = 1000
    command_timeout_ms: int = 1000
