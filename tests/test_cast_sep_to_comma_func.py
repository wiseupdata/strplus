import pytest

from strplus.functions import cast_sep_to_comma


def test_cast_sep_to_comma_with_separator():
    input_str = "1;2;3"
    separator = ";"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str, separator) == expected_output


def test_cast_sep_to_comma_without_separator():
    input_str = "1,2,3"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_with_auto_separator():
    input_str = "1\t2\t3"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_with_empty_string():
    input_str = ""
    expected_output = ""
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_empty_input():
    input_str = ""
    expected_output = ""
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_single_input():
    input_str = "1"
    expected_output = "1"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_multiple_same_inputs():
    input_str = "1,1,1"
    expected_output = "1,1,1"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_multiple_different_inputs():
    input_str = "1,2,3"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_tab_separator():
    input_str = "1\t2\t3"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_space_separator():
    input_str = "1 2 3"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_semicolon_separator():
    input_str = "1;2;3"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_colon_separator():
    input_str = "1:2:3"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_dot_separator():
    input_str = "1.2.3"
    expected_output = "1.2.3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_mixed_separators():
    input_str = "1,2;3\t4 5.6"
    expected_output = "1,2;3\t4 5.6"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_leading_trailing_spaces():
    input_str = " 1 , 2 , 3 "
    expected_output = "1,,,2,,,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_extra_spaces_between_inputs():
    input_str = "1   2   3"
    expected_output = "1,,,2,,,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_empty_spaces_between_inputs():
    input_str = "1     2     3"
    expected_output = "1,,,,,2,,,,,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_newline_separator():
    input_str = "1\n2\n3"
    expected_output = "1,2,3"
    assert cast_sep_to_comma(input_str) == expected_output


def test_cast_sep_to_comma_different_whitespace_separator():
    input_str = "1 2\t3\n4"
    expected_output = "1,2\t3\n4"
    assert cast_sep_to_comma(input_str) == expected_output
