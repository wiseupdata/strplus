from typing import List

import pytest

from strplus.functions import get_separator, split_by_separator


def test_get_separator_one_separator():
    assert get_separator("apple,orange,banana,grape") == ","
    assert get_separator("apple;orange;banana;grape") == ";"
    assert get_separator("apple|orange|banana|grape") == "|"
    assert get_separator("apple orange banana grape") == " "
    assert get_separator("apple\torange\tbanana\tgrape") == "\t"
    assert get_separator("apple:orange:banana:grape") == ":"
    assert get_separator("apple/orange\\banana\ngrape") == "/"
    assert get_separator("apple\\orange/banana\ngrape") == "/"
    assert get_separator("apple\norange\nbanana\ngrape") == "\n"
    assert get_separator("apple orange banana grape") == " "
    assert get_separator("") is None
    assert get_separator("apple") is None


def test_get_separator_multiple_separators():
    assert get_separator("apple,orange;banana|grape") == ","
    assert get_separator("apple,orange;banana grape") == ","
    assert get_separator("apple;orange|banana,grape") == ","
    assert get_separator("apple:orange\nbanana grape") == " "
    assert get_separator("apple/orange\\banana grape") == " "
    assert get_separator("apple\torange\nbanana grape") == " "
    assert get_separator("apple/orange\\banana grape") == " "
    assert get_separator("apple\torange|banana:grape") == "|"
    assert get_separator("apple:orange\\banana\ngrape") == ":"
    assert get_separator("apple/orange;banana\tgrape") == ";"


def test_get_separator_one_character():
    assert get_separator(",") == ","
    assert get_separator(";") == ";"
    assert get_separator("|") == "|"
    assert get_separator(" ") == None
    assert get_separator("\t") == None
    assert get_separator(":") == ":"
    assert get_separator("/") == "/"
    assert get_separator("\\") == "\\"
    assert get_separator("\n") == None


def test_get_separator_no_separator():
    assert get_separator("appleorangebananagrape") is None
    assert get_separator("1234567890") is None
    assert get_separator("+-*/=") == "/"
    assert get_separator("/") == "/"


def test_get_separator_multiple_separators_with_different_counts():
    assert get_separator("apple,orange;banana|grape||melon") == "|"
    assert get_separator("apple,orange;banana|grape |melon") == "|"
    assert get_separator("apple,orange;banana|grape\t\t\tmelon") == "\t"
    assert get_separator("apple,orange;banana|grape/\n/\n/\nmelon") == "/"
    assert get_separator("apple,orange;banana/grape/melon") == "/"
    assert get_separator("apple,orange;banana/grape/melon,") == ","
    assert get_separator("apple|orange,banana,grape") == ","
    assert get_separator("apple;orange;banana;grape;") == ";"
    assert get_separator("apple\norange\nbanana\ngrape") == "\n"


def test_separator_list():
    # Test with custom separator list
    input_string = "apple,banana|cherry"
    separator_list = ["|", "."]
    expected_output = "|"
    assert get_separator(input_string, separator_list) == expected_output

    # Test with empty separator list
    input_string = "apple,banana|cherry"
    separator_list = []
    expected_output = ","
    assert get_separator(input_string, separator_list) == expected_output

    # Test with None as separator list (should use default separator list)
    input_string = "apple,banana|cherry"
    expected_output = ","
    assert get_separator(input_string) == expected_output

    # Test with separator list that does not contain any separators in the input string
    input_string = "apple,banana|cherry"
    separator_list = ["/", "\\"]
    expected_output = None
    assert get_separator(input_string, separator_list) == expected_output
