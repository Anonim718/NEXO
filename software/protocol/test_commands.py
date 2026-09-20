from software.protocol.commands import Command, format_command, parse_command

def test_parse_normalizes_input():
    assert parse_command("  forward ") is Command.FORWARD

def test_unknown_command_is_rejected():
    assert parse_command("DELETE_ALL") is None

def test_format_adds_protocol_terminator():
    assert format_command(Command.STOP) == "STOP\n"
