import pytest

from strplus import Str


def test_init():
    # Test initializing with a string
    s = Str("hello")
    assert str(s) == "hello"


def test_getitem():
    # Test getting a single character
    s = Str("hello")
    assert s[0] == "h"

    # Test getting a slice
    assert str(s[1:4]) == "ell"


def test_instancecheck():
    # Test checking if an instance is an instance of Str
    s = Str("hello")
    assert isinstance(s, Str)

    # Test checking if an instance is an instance of str
    assert isinstance(s, str)


def test_subclasscheck():
    # Test checking if a subclass is a subclass of Str
    class SubStr(Str):
        pass

    assert issubclass(SubStr, Str)

    # Test checking if a subclass is a subclass of str
    assert issubclass(SubStr, str)


def test_attr():
    # Test accessing an attribute
    s = Str("hello")
    assert s.upper() == "HELLO"

    # Test accessing a method
    assert s.capitalize() == "Hello"


def test_pascal_1():
    # Test accessing an attribute
    s = Str("UPPERCASE")
    assert s.to_pascal() == "Uppercase"


def test_pascal_2():
    # Test accessing an attribute
    s = Str("1234!@#$% abcdEFGH")
    assert s.to_pascal() == "1234AbcdEfgh"


def test_camel():
    # Test accessing an attribute
    s = Str("my_string")
    assert s.to_camel() == "myString"


def test_snake():
    # Test accessing an attribute
    s = Str("MyString")
    assert s.to_snake() == "my_string"


def test_list():
    # Test accessing an attribute
    s = Str("MyString")
    assert s.to_list() == ["My", "String"]


def test_cast_to_str_class():
    assert Str.cast("hello") == Str("hello")
    assert Str.cast(["foo", "bar", "baz"], join_sep="-") == Str("foo-bar-baz")
    with pytest.raises(ValueError):
        Str.cast(42)
    assert Str.cast(42, type_constraint=False) == 42


def test_to_pascal():
    assert Str("some-mixed_string With spaces_underscores-and-hyphens").to_pascal() == "SomeMixedStringWithSpacesUnderscoresAndHyphens"
    assert Str("camelCaseTest").to_pascal() == "CamelCaseTest"
    assert Str("snake_case_test").to_pascal() == "SnakeCaseTest"


def test_to_camel():
    assert Str("some-mixed_string With spaces_underscores-and-hyphens").to_camel() == "someMixedStringWithSpacesUnderscoresAndHyphens"
    assert Str("PascalCaseTest").to_camel() == "pascalCaseTest"
    assert Str("snake_case_test").to_camel() == "snakeCaseTest"


def test_to_snake():
    assert Str("some-mixed_string With spaces_underscores-and-hyphens").to_snake() == "some_mixed_string_with_spaces_underscores_and_hyphens"
    assert Str("PascalCaseTest").to_snake() == "pascal_case_test"
    assert Str("camelCaseTest").to_snake() == "camel_case_test"


def test_list():
    assert Str("a,b,c").list == ["a", "b", "c"]
    assert Str("1,2,3,4").list == ["1", "2", "3", "4"]


def test_split_by_sep():
    assert Str("a,b,c").split_by_sep == ["a", "b", "c"]
    assert Str("1.2.3.4").split_by_sep == "1.2.3.4"
    assert Str("a,b and c").split_by_sep == ["a,b", "and", "c"]


def test_sep_to_comma():
    assert Str("a;b;c").separator_as_comma == "a,b,c"
    assert Str("1-2-3-4").separator_as_comma == "1-2-3-4"
    assert Str("a|b and c").separator_as_comma == "a|b,and,c"
