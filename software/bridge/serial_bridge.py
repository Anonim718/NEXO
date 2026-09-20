"""Minimal NEXO computer-to-Arduino serial bridge.

This module intentionally contains no AI logic. Higher-level software can call
send_command(), while the Arduino remains responsible for physical safety.

Requires: pyserial
"""

from __future__ import annotations

import time
from typing import Optional

from software.bridge.protocol import ControllerResponse, parse_response

try:
    import serial
except ImportError:
    serial = None


ALLOWED_COMMANDS = {
    "STOP",
    "FORWARD",
    "BACK",
    "LEFT",
    "RIGHT",
    "STATUS",
    "PING",
}


class NexoBridge:
    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 1.0):
        if serial is None:
            raise RuntimeError("pyserial is required: pip install pyserial")
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection: Optional[serial.Serial] = None

    def connect(self) -> None:
        self.connection = serial.Serial(
            self.port,
            self.baudrate,
            timeout=self.timeout,
        )
        time.sleep(2)
        self.connection.reset_input_buffer()

    def close(self) -> None:
        if self.connection and self.connection.is_open:
            self.connection.close()

    def send_command(self, command: str) -> str:
        command = command.strip().upper()

        if command not in ALLOWED_COMMANDS:
            raise ValueError(f"Unsupported NEXO command: {command}")

        if not self.connection or not self.connection.is_open:
            raise RuntimeError("NEXO controller is not connected")

        self.connection.write((command + "\n").encode("ascii"))
        response = self.connection.readline().decode(
            "ascii", errors="replace"
        ).strip()

        if not response:
            raise TimeoutError(f"No response from NEXO controller for {command}")

        return response

    def send_and_parse(self, command: str) -> ControllerResponse:
        """Send an allowlisted command and return a structured response."""
        return parse_response(self.send_command(command))
