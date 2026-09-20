from software.state_store import JsonStateStore

def test_state_round_trip(tmp_path):
    store = JsonStateStore(tmp_path / "state.json")
    expected = {"mode": "IDLE", "last_command": "STOP"}
    store.save(expected)
    assert store.load() == expected

def test_missing_state_is_empty(tmp_path):
    assert JsonStateStore(tmp_path / "missing.json").load() == {}
