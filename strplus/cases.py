import logging
import re
from typing import List

logger = logging.getLogger(__name__)

import re


def to_pascal(text: str) -> str:
    """
    Simple and efficient method to converts a string to PascalCase.

    Args:
    text (str): The input string.

    Returns:
        str: The PascalCase version of the input string.

    Examples:
        !!! example "Converting strings to PascalCase"
            This example shows how to use `to_pascal()` to convert strings to PascalCase.

            === "Example 1"
                ```python
                to_pascal('hello_world')
                'HelloWorld'
                ```

            === "Example 2"
                ```python
                to_pascal('CamelCase')
                'CamelCase'
                ```

            === "Example 3"
                ```python
                to_pascal('some-mixed_string With spaces_underscores-and-hyphens')
                'SomeMixedStringWithSpacesUnderscoresAndHyphens'
                ```

            === "Example 4"
                ```python
                to_pascal('123abc')
                '123abc'
                ```
    warning:
        - For best results, avoid using punctuation or non-alphanumeric characters in the input string.
        - This function will preserve any digits in the input string.
        - If the input string already has PascalCase formatting, the function will return it unchanged.
        - This function uses regular expressions to identify words in the input string.

    tip: "See also"
        - `to_camel()` - Converts a string to camelCase formatting.
        - `to_snake()` - Converts a string to snake_case formatting.

    """
    text = text.strip()

    if not text:  # If the input string is empty or only whitespace, return an empty string
        return ""

    # Remove any underscores, hyphens, or spaces and split the string into words
    words = sum([re.findall(r"[a-zA-Z0-9]+", word) for word in re.sub("([A-Z][a-z]+)", r" \1", re.sub("([A-Z]+)", r" \1", text)).split()], [])

    # Capitalize the first letter of each word except the first word
    capitalized_words = []
    for i, word in enumerate(words):
        if i == 0 and word[0].isdigit():
            capitalized_words.append(str(word[0]))
            word = word[1:]
        capitalized_words.append(word.capitalize())

    # Join the words back together to form the CamelCase string
    return "".join(capitalized_words)


def to_camel(text) -> str:
    """
    Simple and efficient method to converts a string to camelCase.

    Args:
        text (str): The input string.

    Returns:
        str: The camelCase version of the input string.

    Examples:
        !!! example "Converting strings to camelCase"
            This example shows how to use `to_camel()` to convert strings to camelCase.

            === "Example 1"
                ```python
                to_camel('hello_world')
                'helloWorld'
                ```

            === "Example 2"
                ```python
                to_camel('PascalCase')
                'pascalCase'
                ```

            === "Example 3"
                ```python
                to_camel('some-mixed_string With spaces_underscores-and-hyphens')
                'someMixedStringWithSpacesUnderscoresAndHyphens'
                ```

            === "Example 4"
                ```python
                to_camel('123abc')
                '123abc'
                ```

    warning:
        - For best results, avoid using punctuation or non-alphanumeric characters in the input string.
        - This function will preserve any digits in the input string.
        - If the input string already has camelCase formatting, the function will return it unchanged.
        - This function uses regular expressions to identify words in the input string.

    tip: "See also"
        - `to_pascal()` - Converts a string to PascalCase formatting.
        - `to_snake()` - Converts a string to snake_case formatting.
    """

    text = text.strip()

    if not text:  # If the input string is empty, return an empty string
        return ""

    # Split the string into words using regex, split 1
    words: str = sum([re.findall(r"[a-zA-Z0-9]+", word) for word in re.sub("([A-Z][a-z]+)", r" \1", re.sub("([A-Z]+)", r" \1", text)).split()], [])

    # Capitalize the first letter of each word except the first word
    capitalized_words: str = [words[0].lower()] + [word.capitalize() for word in words[1:]]

    # Join the words back together to form the CamelCase string
    check_01: str = "".join(capitalized_words)

    # Final check
    words: str = re.split("[-_]", check_01)

    return words[0] + "".join(word.capitalize() for word in words[1:]).replace("_", "")


def to_snake(text) -> str:
    """Converts a string to snake_case.

    Args:
        text (str): The input string to convert.

    Returns:
        str: The string converted to snake_case.

    Examples:
        >>> to_snake("HelloWorld")
        'hello_world'

        >>> to_snake("  AnotherString!  ")
        'another_string'

        >>> to_snake("hello-world")
        'hello_world'
    """

    text = text.strip()

    if not text:
        # If the input string is empty or only whitespace, return an empty string
        return ""

    # Remove any non-alphanumeric characters and split the string into words
    words = sum([re.findall(r"[a-zA-Z0-9]+", word) for word in re.sub("([A-Z][a-z]+)", r"_\1", re.sub("([A-Z]+)", r"_\1", text)).split()], [])

    # Join the words back together to form the snake_case string
    return "_".join([word.lower() for word in words])


def to_list(text):
    """Converts a string to a list of alphanumeric words.

    Args:
        text (str): The input string to convert.

    Returns:
        list: A list of words extracted from the input string.

    Examples:
        >>> to_list("Hello world!")
        ['Hello', 'world']

        >>> to_list("   another-string_123  ")
        ['another', 'string', '123']

        >>> to_list("   ")
        []

        >>> to_list("")
        []
    """
    text = text.strip()

    if not text:  # If the input string is empty or only whitespace, return an empty string
        return []

    # Remove any non-alphanumeric characters and split the string into words
    word_list = sum([re.findall(r"[a-zA-Z0-9]+", word) for word in re.sub("([A-Z][a-z]+)", r"_\1", re.sub("([A-Z]+)", r"_\1", text)).split()], [])

    return word_list
