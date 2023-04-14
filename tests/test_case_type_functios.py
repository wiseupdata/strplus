import pytest

from strplus.cases import to_pascal


@pytest.mark.parametrize("input_string, expected_output", [
    ("the quick brown fox", "TheQuickBrownFox"),
    ("a b c d e f g", "ABCDEFG"),
    ("1234 5678 90", "1234567890"),
    ("PascalCase", "Pascalcase"),
    ("UPPERCASE", "Uppercase")
])
def test_function_to_pascal(input_string, expected_output):
    assert to_pascal(input_string) == expected_output
