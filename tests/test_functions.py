from strplus.functions import get_separator

import pytest

def test_get_separator_one_separator():
    assert get_separator("apple,orange,banana,grape") == ','
    assert get_separator("apple;orange;banana;grape") == ';'
    assert get_separator("apple|orange|banana|grape") == '|'
    assert get_separator("apple orange banana grape") == ' '
    assert get_separator("apple\torange\tbanana\tgrape") == '\t'
    assert get_separator("apple:orange:banana:grape") == ':'
    assert get_separator("apple/orange\\banana\ngrape") == '/'
    assert get_separator("apple\\orange/banana\ngrape") == '/'
    assert get_separator("apple\norange\nbanana\ngrape") == '\n'
    assert get_separator("apple orange banana grape") == ' '
    assert get_separator("") is None
    assert get_separator("apple") is None

def test_get_separator_multiple_separators():
    assert get_separator("apple,orange;banana|grape") == ','
    assert get_separator("apple,orange;banana grape") == ' '
    assert get_separator("apple;orange|banana,grape") == ','
    assert get_separator("apple:orange\nbanana grape") == '\n'
    assert get_separator("apple/orange\\banana grape") == '/'
    assert get_separator("apple\torange\nbanana grape") == '\t'
    assert get_separator("apple/orange\\banana grape") == '/'
    assert get_separator("apple\torange|banana:grape") == '|'
    assert get_separator("apple:orange\\banana\ngrape") == '\\'
    assert get_separator("apple/orange;banana\tgrape") == ';'

def test_get_separator_one_character():
    assert get_separator(",") == ','
    assert get_separator(";") == ';'
    assert get_separator("|") == '|'
    assert get_separator(" ") == ' '
    assert get_separator("\t") == '\t'
    assert get_separator(":") == ':'
    assert get_separator("/") == '/'
    assert get_separator("\\") == '\\'
    assert get_separator("\n") == '\n'

def test_get_separator_no_separator():
    assert get_separator("appleorangebananagrape") is None
    assert get_separator("1234567890") is None
    assert get_separator("+-*/=") is None
    assert get_separator("/") is None




