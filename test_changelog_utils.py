"""Tests for changelog_utils module."""

import pytest
from changelog_utils import format_entry, parse_version


class TestParseVersion:
    """Tests for parse_version."""

    def test_extracts_semver_from_header(self):
        """Confirm a standard version header yields its version string."""
        assert parse_version("## [1.2.3] - 2026-06-18") == "1.2.3"

    def test_extracts_unreleased(self):
        """Confirm the special Unreleased token is returned verbatim."""
        assert parse_version("## [Unreleased]") == "Unreleased"

    def test_returns_none_for_plain_text(self):
        """Confirm headers without brackets yield None."""
        assert parse_version("## No brackets here") is None

    def test_returns_none_for_empty_string(self):
        """Confirm an empty string yields None."""
        assert parse_version("") is None


class TestFormatEntry:
    """Tests for format_entry."""

    def test_basic_section(self):
        """Confirm a section with items is rendered correctly."""
        result = format_entry("Added", ["Feature A", "Feature B"])
        assert result == "### Added\n\n- Feature A\n- Feature B\n"

    def test_strips_item_whitespace(self):
        """Confirm leading/trailing whitespace is stripped from each item."""
        result = format_entry("Fixed", ["  Bug fix  "])
        assert "- Bug fix" in result

    def test_empty_items_returns_empty_string(self):
        """Confirm an empty item list produces an empty string."""
        assert format_entry("Removed", []) == ""

    def test_section_name_appears_as_heading(self):
        """Confirm the section name is rendered as a level-3 heading."""
        result = format_entry("Changed", ["Update X"])
        assert result.startswith("### Changed")