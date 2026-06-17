import pytest
from utils.text import slugify


def test_basic_lowercase():
    """Verify basic string is lowercased."""
    assert slugify("Hello World") == "hello-world"


def test_multiple_spaces():
    """Verify runs of spaces collapse to a single hyphen."""
    assert slugify("foo   bar") == "foo-bar"


def test_special_characters():
    """Verify non-alphanumeric characters are replaced with hyphens."""
    assert slugify("Hello, World!") == "hello-world"


def test_leading_trailing_hyphens():
    """Verify leading and trailing hyphens are stripped."""
    assert slugify("--hello--") == "hello"


def test_mixed_punctuation():
    """Verify mixed punctuation runs collapse to a single hyphen."""
    assert slugify("foo!@#bar") == "foo-bar"


def test_already_slug():
    """Verify a clean slug is returned unchanged."""
    assert slugify("hello-world") == "hello-world"


def test_numbers():
    """Verify numbers are preserved."""
    assert slugify("foo 123 bar") == "foo-123-bar"


def test_empty_string():
    """Verify empty string returns empty string."""
    assert slugify("") == ""


def test_only_special_chars():
    """Verify a string of only special chars returns empty string."""
    assert slugify("!!!") == ""


def test_unicode_letters_removed():
    """Verify non-ASCII characters are treated as non-alphanumeric."""
    assert slugify("café") == "caf"