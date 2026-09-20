from unittest.mock import MagicMock

import pytest

from software.bridge.serial_bridge import NexoBridge


@pytest.fixture
def bridge():
    return NexoBridge("COM_TEST")


def test_send_command_writes_line_and_returns_response(bridge):
    fake_serial = MagicMock()
    fake_serial.is_open = True
    fake_serial.readline.return_value = b"OK=PONG\r\n"
    bridge.connection = fake_serial

    response = bridge.send_command(" ping ")

    fake_serial.write.assert_called_once_with(b"PING\n")
    assert response == "OK=PONG"


def test_rejects_unknown_command(bridge):
    bridge.connection = MagicMock(is_open=True)

    with pytest.raises(ValueError):
        bridge.send_command("DANCE")


def test_requires_connection(bridge):
    with pytest.raises(RuntimeError):
        bridge.send_command("STOP")


def test_timeout_without_response(bridge):
    fake_serial = MagicMock()
    fake_serial.is_open = True
    fake_serial.readline.return_value = b""
    bridge.connection = fake_serial

    with pytest.raises(TimeoutError):
        bridge.send_command("STATUS")


def test_send_and_parse_returns_structured_response(bridge):
    fake_serial = MagicMock()
    fake_serial.is_open = True
    fake_serial.readline.return_value = b"OK=STATUS STATE=FORWARD DIST_CM=42\r\n"
    bridge.connection = fake_serial

    response = bridge.send_and_parse("STATUS")

    assert response.category == "OK"
    assert response.value == "STATUS"
    assert response.fields == {"STATE": "FORWARD", "DIST_CM": "42"}
