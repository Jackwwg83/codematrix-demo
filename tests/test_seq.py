import pytest
from utils.seq import chunk


def test_empty_list():
    """chunk of an empty list returns an empty list."""
    assert chunk([], 3) == []


def test_exact_multiple():
    """chunk splits evenly when length is an exact multiple of size."""
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_remainder():
    """chunk produces a shorter last sublist when there is a remainder."""
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_size_larger_than_list():
    """chunk returns a single sublist when size exceeds list length."""
    assert chunk([1, 2, 3], 10) == [[1, 2, 3]]