import pytest

from strplus.cases import to_pascal, to_camel


@pytest.mark.parametrize("input_string, expected_output", [
    ("the quick brown fox", "TheQuickBrownFox"),
    ("a b c d e f g", "ABCDEFG"),
    ("1234 5678 90", "1234567890"),
    ("PascalCase", "PascalCase"),
    ("UPPERCASE", "Uppercase")
])
def test_function_to_pascal(input_string, expected_output):
    assert to_pascal(input_string) == expected_output
    assert to_pascal("1_word") == "1Word"
    assert to_pascal("my-variable_name") == "MyVariableName"
    assert to_pascal("another_string_to_convert") == "AnotherStringToConvert"
    assert to_pascal("ThisIsAlreadyPascalCase") == "ThisIsAlreadyPascalCase"
    assert to_pascal("") == ""
    assert to_pascal("   ") == ""
    assert to_pascal("a") == "A"
    assert to_pascal("A") == "A"
    # assert to_pascal("aA") == "Aa"
    # assert to_pascal("AA") == "Aa"
    assert to_pascal("theQuick_brown_10Fox_jumps_over_the_lazy_dog") == "TheQuickBrown10FoxJumpsOverTheLazyDog"
    assert to_pascal("1234!@#$% abcdEFGH") == "1234AbcdEfgh"


def test_to_camel():
    assert to_camel("thisIsAlreadyCamelCase") == "thisIsAlreadyCamelCase"
    assert to_camel("1_word") == "1Word"
    assert to_camel("") == ""
    assert to_camel("   ") == ""
    assert to_camel("myCamelCaseString") == "myCamelCaseString"
    assert to_camel("a") == "a"
    assert to_camel("a") == "a"
    assert to_camel("aA") == "aA"
    assert to_camel("AA") == "aa"
    assert to_camel("my-variable_name") == "myVariableName"
    assert to_camel("another_string_to_convert") == "anotherStringToConvert"
    assert to_camel("the_quick_brown_fox_jumps_over_the_lazy_dog") == "theQuickBrownFoxJumpsOverTheLazyDog"
    assert to_camel("theQuick_brown_10Fox_jumps_over_the_lazy_dog") == "theQuickBrown10FoxJumpsOverTheLazyDog"
    assert to_camel("1234!@#$% abcdEFGH") == "1234AbcdEfgh"
