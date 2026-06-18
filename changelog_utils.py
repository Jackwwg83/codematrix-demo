"""Utilities for parsing and formatting CHANGELOG entries."""

import re
from typing import Optional


def parse_version(header: str) -> Optional[str]:
    """Extract a semantic version string from a Keep-a-Changelog section header."""
    match = re.search(r"\[([^\]]+)\]", header)
    return match.group(1) if match else None


def format_entry(section: str, items: list[str]) -> str:
    """Render a CHANGELOG subsection (e.g. 'Added') with bullet-point items."""
    if not items:
        return ""
    bullets = "\n".join(f"- {item.strip()}" for item in items)
    return f"### {section}\n\n{bullets}\n"