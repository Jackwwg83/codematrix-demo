import pytest

from utils.strings import truncate


class TestTruncateShortBranch:
    """Tests where the string is at or below max_len and should be returned unchanged."""

    def test_empty_string(self):
        """Empty string is always within any positive max_len."""
        assert truncate("", 5) == ""

    def test_string_shorter_than_max_len(self):
        """String shorter than max_len is returned as-is."""
        assert truncate("hello", 10) == "hello"

    def test_string_equal_to_max_len(self):
        """String whose length equals max_len is returned as-is."""
        assert truncate("hello", 5) == "hello"


class TestTruncateLongBranch:
    """Tests where the string exceeds max_len and should be truncated with an ellipsis."""

    def test_string_longer_than_max_len(self):
        """String longer than max_len is cut and suffixed with '...'."""
        assert truncate("hello world", 8) == "hello..."

    def test_truncated_result_has_correct_length(self):
        """Truncated result is exactly max_len characters long."""
        result = truncate("abcdefghij", 7)
        assert len(result) == 7

    def test_truncated_result_ends_with_ellipsis(self):
        """Truncated result ends with exactly three dots."""
        result = truncate("abcdefghij", 7)
        assert result.endswith("...")

    def test_truncated_result_preserves_prefix(self):
        """Characters before the ellipsis match the start of the original string."""
        result = truncate("abcdefghij", 7)
        assert result == "abcd..."

    def test_max_len_just_above_threshold(self):
        """String one character longer than max_len triggers truncation."""
        assert truncate("abcd", 3) == "..."

    def test_long_string(self):
        """Long input is truncated to max_len characters including the ellipsis."""
        s = "x" * 100
        result = truncate(s, 10)
        assert result == "x" * 7 + "..."
        assert len(result) == 10