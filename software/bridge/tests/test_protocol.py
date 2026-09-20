from protocol import parse_response
import pytest

def test_parse_pong():
    r=parse_response("OK=PONG"); assert r.category=="OK"; assert r.value=="PONG"; assert r.fields=={}

def test_parse_status():
    r=parse_response("OK=STATUS STATE=FORWARD DIST_CM=42")
    assert r.category=="OK"; assert r.value=="STATUS"; assert r.fields=={"STATE":"FORWARD","DIST_CM":"42"}

def test_rejects_malformed():
    with pytest.raises(ValueError): parse_response("NOT_A_RESPONSE")
