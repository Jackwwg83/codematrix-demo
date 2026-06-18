def chunk(items, size):
    """Split a list into consecutive sublists of length size (last may be shorter)."""
    return [items[i:i + size] for i in range(0, len(items), size)]