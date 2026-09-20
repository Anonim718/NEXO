import pytest

from software.bridge.protocol import parse_response


def test_parse_pong():
    response = parse_response("OK=PONG")
    assert response.category == "OK"
    assert response.value == "PONG"
    assert response.fields == {}


def test_parse_status():
    response = parse_response("OK=STATUS STATE=FORWARD DIST_CM=42")
    assert response.category == "OK"
    assert response.value == "STATUS"
    assert response.fields == {"STATE": "FORWARD", "DIST_CM": "42"}


def test_rejects_malformed():
    with pytest.raises(ValueError):
        parse_response("NOT_A_RESPONSE")
