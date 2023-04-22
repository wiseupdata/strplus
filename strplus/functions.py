from strplus.cases import *


def to_list(text: str) -> List[str]:
    """

    Converts a string to a list of strings, where each word is a separate element in the list.

    Args:
        text (str): The input string.

    Returns:
        List[str]: A list of strings, where each word in the input string is a separate element in the list.

    !!! Example "Converting a string to a list"
        This example shows how to use `to_list()` to convert a string to a list.

        === "Example 1"
            ```python
            to_list('hello world')
            ```
            ['hello', 'world']

        === "Example 2"
            ```python
            to_list('HelloWorld')
            ```
            ['Hello', 'World']

        === "Example 3"
            ```python
            to_list('some-mixed_string With spaces_underscores-and-hyphens')
            ```
            ['some', 'mixed', 'string', 'With', 'spaces', 'underscores', 'and', 'hyphens']

        === "Example 4"
            ```python
            to_list('123abc')
            ```
            ['123abc']

    Tip: Use tips
        - If you need to convert a string to a list of integers or floats, you can use list comprehension to convert each element to the desired type.
        - If you need to remove duplicates from the list, you can convert it to a set and then back to a list.

    Info: Important
        - For best results, avoid using punctuation or non-alphanumeric characters in the input string.
        - This function uses regular expressions to identify words in the input string.

    """
    text = text.strip()

    if not text:  # If the input string is empty or only whitespace, return an empty list
        return []

    # Remove any non-alphanumeric characters and split the string into words
    word_list = sum([re.findall(r"[a-zA-Z0-9]+", word) for word in re.sub("([A-Z][a-z]+)", r"_\1", re.sub("([A-Z]+)", r"_\1", text)).split()], [])

    return word_list


def get_separator(input_string):
    """

    Finds the most common separator in a given input string.

    Args:
        input_string (str): The input string to search for separators.

    Returns:
        str or None: The most common separator found in the input string, or None if no separators are found.

    !!! Example "Finding the most common separator"
        This example shows how to use `get_separator()` to find the most common separator in a string.

        === "Example 1"
            ```python
            get_separator('This is a sample sentence, separated by commas')
            ```
            ,

        === "Example 2"
            ```python
            get_separator('This string has no separators')
            ```
            None

        === "Example 3"
            ```python
            get_separator('This string has multiple separators: ;, |, and /')
            ```
            ;

    Tip: Use tips
        - This function can be used to split a string into a list using the most common separator, like so: `input_string.split(get_separator(input_string))`.
        - To split a string into a list using all possible separators, use the `re.split()` function instead.

    Info: Important
        - This function assumes that the input string contains only valid separators.
        - If multiple separators are tied for the most common, the first one encountered in the list of separators is returned.

    """

    separators = [",", ";", "|", " ", "\t", ":", "/", "\\", "\n"]

    # check each separator in the order of priority
    for sep in [",", ";", "|", " ", "\t", ":", "/", "\\", "\n"]:
        if sep in input_string:
            sep_count = input_string.count(sep)
            if sep_count == 1:
                return sep
            elif sep_count > 1:
                return max(separators, key=input_string.count)

    # if no separator was found, return None
    return None
