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
