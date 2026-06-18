from utils.dictx import pick


def test_all_keys_present():
    """All requested keys exist in the dict."""
    assert pick({"a": 1, "b": 2, "c": 3}, ["a", "b"]) == {"a": 1, "b": 2}


def test_some_keys_missing():
    """Missing keys are silently omitted."""
    assert pick({"a": 1, "b": 2}, ["a", "x"]) == {"a": 1}


def test_empty_keys():
    """Empty key list returns empty dict."""
    assert pick({"a": 1, "b": 2}, []) == {}


def test_empty_dict():
    """Empty source dict returns empty dict regardless of keys."""
    assert pick({}, ["a", "b"]) == {}