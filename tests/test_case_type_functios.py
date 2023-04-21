import pytest

from strplus.cases import to_camel, to_pascal, to_snake
from strplus.functions import to_list


@pytest.mark.parametrize(
    "input_string, expected_output",
    [("the quick brown fox", "TheQuickBrownFox"), ("a b c d e f g", "ABCDEFG"), ("1234 5678 90", "1234567890"), ("PascalCase", "PascalCase"), ("UPPERCASE", "Uppercase")],
)
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
    assert to_pascal("aA") == "AA"
    assert to_pascal("AA") == "Aa"
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


@pytest.mark.parametrize(
    "input_string, expected_output",
    [("the quick brown fox", "the_quick_brown_fox"), ("a b c d e f g", "a_b_c_d_e_f_g"), ("1234 5678 90", "1234_5678_90"), ("PascalCase", "pascal_case"), ("UPPERCASE", "uppercase")],
)
def test_function_to_snake_case(input_string, expected_output):
    assert to_snake(input_string) == expected_output
    assert to_snake("1_word") == "1_word"
    assert to_snake("my-variable_name") == "my_variable_name"
    assert to_snake("another_string_to_convert") == "another_string_to_convert"
    assert to_snake("this_is_already_snake_case") == "this_is_already_snake_case"
    assert to_snake("") == ""
    assert to_snake("   ") == ""
    assert to_snake("a") == "a"
    assert to_snake("A") == "a"
    assert to_snake("theQuick_brown_10Fox_jumps_over_the_lazy_dog") == "the_quick_brown_10_fox_jumps_over_the_lazy_dog"
    assert to_snake("1234!@#$% abcdEFGH") == "1234_abcd_efgh"
    assert to_snake("MyString") == "my_string"


def test_empty_string():
    assert to_list("") == []


def test_only_whitespace():
    assert to_list("  \n\t ") == []


def test_one_word():
    assert to_list("hello") == ["hello"]


def test_multiple_words():
    assert to_list("hello world") == ["hello", "world"]


def test_uppercase_words():
    assert to_list("HelloWorld") == ["Hello", "World"]
    assert to_list("HELLO_WORLD") == ["HELLO", "WORLD"]
    assert to_list("ThisIsATest") == ["This", "Is", "A", "Test"]
    assert to_list("T") == ["T"]


def test_special_characters():
    assert to_list("hello-world") == ["hello", "world"]
    assert to_list("hello_world!") == ["hello", "world"]
    assert to_list("h@llo") == ["h", "llo"]
