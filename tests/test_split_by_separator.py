from typing import List

import pytest

from strplus.functions import get_separator, split_by_separator


def test_split_by_separator():
    # Test with default separator
    assert split_by_separator("1,2,3,4") == ["1", "2", "3", "4"]
    assert split_by_separator("1;2;3;4") == ["1", "2", "3", "4"]
    assert split_by_separator("1:2:3:4") == ["1", "2", "3", "4"]
    assert split_by_separator("1-2-3-4", separator=["-"]) == ["1", "2", "3", "4"]

    # Test with a specific separator
    assert split_by_separator("1,2,3,4", ",") == ["1", "2", "3", "4"]
    assert split_by_separator("1;2;3;4", ";") == ["1", "2", "3", "4"]
    assert split_by_separator("1:2:3:4", ":") == ["1", "2", "3", "4"]
    assert split_by_separator("1-2-3-4", "-") == ["1", "2", "3", "4"]

    # Test with a list of separators
    assert split_by_separator("1,2,3,4", [",", ";"]) == ["1", "2", "3", "4"]
    assert split_by_separator("1;2;3;4", [",", ";"]) == ["1", "2", "3", "4"]
    assert split_by_separator("1:2:3:4", [",", ";", ":"]) == ["1", "2", "3", "4"]
    assert split_by_separator("1-2-3-4", [":", "-"]) == ["1", "2", "3", "4"]

    # Test with no separator found
    assert split_by_separator("1234") == "1234"


def test_split_by_separator_type_constraint():
    with pytest.raises(Exception, match=r"The value passed is not a string."):
        split_by_separator(123)


def test_split_by_separator_type_constraint_skipping():
    assert split_by_separator(123, type_constraint=False) == 123


def test_split_by_separator_no_separator_found():
    assert split_by_separator("one two three four", separator=["-", "|"]) == "one two three four"


def test_split_by_separator_single_separator():
    assert split_by_separator("one,two,three", ",") == ["one", "two", "three"]


def test_split_by_separator_multiple_separators():
    assert split_by_separator("one-two three|four", ["-", " ", "|"]) == ["one", "two three|four"]
