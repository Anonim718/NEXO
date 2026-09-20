from software.orchestration import Tool, validate_tool

def test_known_tool(): assert validate_tool("move") is Tool.MOVE
def test_unknown_tool_rejected(): assert validate_tool("shell") is None
