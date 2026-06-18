from utils.mathx import clamp


def test_clamp_below_range():
    """Value below lo is clamped to lo."""
    assert clamp(-5, 0, 10) == 0


def test_clamp_in_range():
    """Value within range is returned unchanged."""
    assert clamp(5, 0, 10) == 5


def test_clamp_above_range():
    """Value above hi is clamped to hi."""
    assert clamp(15, 0, 10) == 10


def test_clamp_lo_equals_hi():
    """When lo == hi, any value is clamped to that single point."""
    assert clamp(7, 3, 3) == 3