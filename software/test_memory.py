from memory import Memory

def test_memory_is_bounded():
    m=Memory(max_entries=2); m.remember("a"); m.remember("b"); m.remember("c")
    assert m.recent()==["b","c"]
def test_empty_values_are_ignored():
    m=Memory(); m.remember(" "); assert m.entries==[]
