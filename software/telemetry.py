"""Hardware-independent telemetry model."""
from dataclasses import dataclass
from time import time

@dataclass(frozen=True)
class Telemetry:
    timestamp: float
    distance_cm: float | None = None
    battery_percent: float | None = None
    mode: str = "IDLE"
    last_command: str = "STOP"
    fault: str | None = None

def snapshot(**kwargs) -> Telemetry:
    return Telemetry(timestamp=time(), **kwargs)
