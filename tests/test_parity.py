import pytest
from utils.parity import is_odd


def test_odd():
    """Test that a positive odd number is identified correctly."""
    assert is_odd(3) is True


def test_even():
    """Test that a positive even number is identified correctly."""
    assert is_odd(4) is False


def test_zero():
    """Test that zero is identified as even."""
    assert is_odd(0) is False


def test_negative_odd():
    """Test that a negative odd number is identified correctly."""
    assert is_odd(-7) is True


def test_negative_even():
    """Test that a negative even number is identified correctly."""
    assert is_odd(-8) is False