"""Allowlisted tool orchestration boundary for NEXO."""
from enum import Enum

class Tool(str, Enum):
    MOVE = "MOVE"
    STATUS = "STATUS"
    STOP = "STOP"
    ARM = "ARM"

ALLOWED_TOOLS=frozenset(Tool)

def validate_tool(name: str) -> Tool | None:
    try: return Tool(name.strip().upper())
    except (AttributeError, ValueError): return None
