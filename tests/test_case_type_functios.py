import pytest

from strplus.cases import to_pascal, to_camel


@pytest.mark.parametrize("input_string, expected_output", [
    ("the quick brown fox", "TheQuickBrownFox"),
    ("a b c d e f g", "ABCDEFG"),
    ("1234 5678 90", "1234567890"),
    ("PascalCase", "Pascalcase"),
    ("UPPERCASE", "Uppercase")
])
def test_function_to_pascal(input_string, expected_output):
    assert to_pascal(input_string) == expected_output


def test_to_camel():
    assert to_camel("my-variable_name") == "myVariable_name"
    assert to_camel("another_string_to_convert") == "another_string_to_convert"
    assert to_camel("thisIsAlreadyCamelCase") == "thisisalreadycamelcase"
    assert to_camel("") == ""
    assert to_camel("   ") == ""
    assert to_camel("1_word") == "1Word"
    # assert to_camel("myCamelCaseString") == "myCamelCaseString"
    assert to_camel("a") == "a"
    assert to_camel("A") == "a"
    assert to_camel("aA") == "aa"
    assert to_camel("AA") == "aa"
    # assert to_camel("the_quick_brown_fox_jumps_over_the_lazy_dog") == "theQuickBrownFoxJumpsOverTheLazyDog"
