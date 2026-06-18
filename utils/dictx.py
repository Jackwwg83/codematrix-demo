def pick(d, keys):
    """Return a new dict containing only the given keys that exist in d."""
    return {k: d[k] for k in keys if k in d}