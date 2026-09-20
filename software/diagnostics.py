"""Deterministic diagnostics checks for NEXO software."""
from dataclasses import dataclass

@dataclass(frozen=True)
class DiagnosticResult:
    name: str
    ok: bool
    detail: str

def run_diagnostics(bridge_connected: bool, battery_percent: float | None, fault: str | None) -> list[DiagnosticResult]:
    return [
        DiagnosticResult("bridge", bridge_connected, "connected" if bridge_connected else "not connected"),
        DiagnosticResult("battery", battery_percent is None or battery_percent > 0, "available" if battery_percent is not None else "not reported"),
        DiagnosticResult("fault", fault is None, "clear" if fault is None else fault),
    ]
