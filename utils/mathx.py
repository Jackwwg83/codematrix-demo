def clamp(x, lo, hi):
    """Return x bounded to the inclusive range [lo, hi]."""
    return max(lo, min(x, hi))