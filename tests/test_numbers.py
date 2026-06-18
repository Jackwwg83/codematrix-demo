import pytest
from utils.numbers import is_even


def test_even_positive():
    """Return True for a positive even number."""
    assert is_even(4) is True


def test_odd_positive():
    """Return False for a positive odd number."""
    assert is_even(3) is False


def test_zero():
    """Return True for zero, which is even by definition."""
    assert is_even(0) is True


def test_negative_even():
    """Return True for a negative even number."""
    assert is_even(-2) is True


def test_negative_odd():
    """Return False for a negative odd number."""
    assert is_even(-7) is False