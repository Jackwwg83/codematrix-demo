import re


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]