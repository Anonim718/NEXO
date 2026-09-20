"""Deterministic in-memory NEXO controller simulator."""

from __future__ import annotations

from dataclasses import dataclass, field

ALLOWED_COMMANDS = {"STOP", "FORWARD", "BACK", "LEFT", "RIGHT", "STATUS", "PING"}


@dataclass
class SimulatedController:
    state: str = "STOP"
    distance_cm: int = 100
    battery_percent: int | None = None
    history: list[str] = field(default_factory=list)

    def command(self, command: str) -> str:
        command = command.strip().upper()
        if command not in ALLOWED_COMMANDS:
            return "ERR=UNKNOWN_COMMAND"

        self.history.append(command)

        if command == "PING":
            return "OK=PONG"
        if command == "STATUS":
            battery = "" if self.battery_percent is None else f" BATTERY={self.battery_percent}"
            return f"OK=STATUS STATE={self.state} DIST_CM={self.distance_cm}{battery}"
        if command == "STOP":
            self.state = "STOP"
            return "OK=STOP"
        if command in {"FORWARD", "BACK", "LEFT", "RIGHT"}:
            if command == "FORWARD" and self.distance_cm <= 20:
                self.state = "STOP"
                return "SAFETY=OBSTACLE_STOP DIST_CM=" + str(self.distance_cm)
            self.state = command
            return f"OK={command}"

        return "ERR=UNHANDLED"
