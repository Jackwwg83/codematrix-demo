import re


def slugify(s):
    """Lowercase s and replace runs of non-alphanumeric characters with a single hyphen, trimming leading/trailing hyphens."""
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')