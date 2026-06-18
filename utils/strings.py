def truncate(s, max_len):
    """Return s unchanged if len(s) <= max_len, else cut to (max_len - 3) chars and append '...'."""
    if len(s) <= max_len:
        return s
    return s[:max_len - 3] + "..."