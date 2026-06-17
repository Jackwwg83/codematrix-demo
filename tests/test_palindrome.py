import pytest

from utils.palindrome import is_palindrome


def test_basic_palindrome():
    """Simple lowercase palindrome."""
    assert is_palindrome("racecar") is True


def test_case_insensitive():
    """Mixed-case input must be treated as equal."""
    assert is_palindrome("RaceCar") is True


def test_with_punctuation_and_spaces():
    """Classic phrase with punctuation and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_non_palindrome():
    """Ordinary word that is not a palindrome."""
    assert is_palindrome("hello") is False


def test_empty_string():
    """Empty string is trivially a palindrome."""
    assert is_palindrome("") is True


def test_single_character():
    """Single character is always a palindrome."""
    assert is_palindrome("a") is True


def test_numeric_palindrome():
    """Numeric string that reads the same forwards and backwards."""
    assert is_palindrome("12321") is True


def test_numeric_non_palindrome():
    """Numeric string that is not a palindrome."""
    assert is_palindrome("12345") is False


def test_only_non_alphanumeric():
    """String composed entirely of punctuation reduces to empty, which is a palindrome."""
    assert is_palindrome("!!!") is True