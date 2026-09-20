"""Safe parsing and formatting for the NEXO serial protocol."""
from enum import Enum

class Command(str, Enum):
    STOP = "STOP"
    FORWARD = "FORWARD"
    BACK = "BACK"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    STATUS = "STATUS"
    PING = "PING"

ALLOWED_COMMANDS = frozenset(Command)

def parse_command(raw: str) -> Command | None:
    if not isinstance(raw, str):
        return None
    try:
        return Command(raw.strip().upper())
    except ValueError:
        return None

def format_command(command: Command) -> str:
    if command not in ALLOWED_COMMANDS:
        raise ValueError("Command is not allowlisted")
    return command.value + "\n"
