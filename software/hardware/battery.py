"""Hardware-independent battery monitoring interface."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BatteryStatus:
    percent: int | None
    voltage: float | None
    low: bool


class BatteryMonitor:
    """Interface boundary; no ADC pin is assumed until hardware is selected."""

    def read(self) -> BatteryStatus:
        return BatteryStatus(percent=None, voltage=None, low=False)
