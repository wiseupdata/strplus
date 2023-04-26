from typing import Any, List, Optional, Union

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


def get_separator(input_string, separator_list: Optional[List[str]] = None):
    """

    Returns the most frequent separator character in an input string.

    Args:
        input_string (str): The input string to analyze.
        separator_list (Optional[List[str]], optional): A list of separator characters to consider. Defaults to None.

    Returns:
        Union[str, None]: The most frequent separator character in the input string, or None if there are no separators.

    !!! Example "Finding the most frequent separator character"
        This example shows how to use `get_separator()` to find the most frequent separator character in a string.

        === "Example 1"
            ```python
            get_separator("John, Doe; Jane | Doe")
            ```
            ','

        === "Example 2"
            ```python
            get_separator("John Doe Jane Doe")
            ```
            " "

        === "Example 3"
            ```python
            get_separator("A/B/C")
            ```
            '/'

    Tip: Use tips
        - If you want to specify a custom list of separator characters, pass it as the `separator_list` argument.
        - If you want to find the second most frequent separator character (or any other rank), you can modify the code to return a list of separator characters sorted by frequency.

    Info: Important
        - The function assumes that any character that appears at least once in the input string is a potential separator.
        - The function uses a common list of separator characters by default, but this list may not be appropriate for all types of input strings.
        - The function returns None if there are no separators in the input string.

    """

    # Common separator list by priority!
    common_separators = [",", ";", "|", " ", "\t", ":", "/", "\\", "\n"]
    input_string = input_string.strip()

    # Setting the separator list
    separator_list_target = separator_list if separator_list is not None and len(separator_list) > 0 else common_separators

    sep_frequency = {sep: input_string.count(sep) for sep in separator_list_target if input_string.count(sep) > 0}
    most_frequent_separator = None

    if len(sep_frequency) > 0:
        max_value = max(sep_frequency.values())
        max_frequency = [key for key, value in sep_frequency.items() if value == max_value]
        sep_sorted_by_priority = sorted(max_frequency, key=lambda x: separator_list_target.index(x))
        most_frequent_separator = sep_sorted_by_priority[0]

    if most_frequent_separator is None:
        print(f"common separators not found in the string provided, please inform the separator_list!\ncommon separator:\n{common_separators}")

    return most_frequent_separator


def split_by_separator(input_string: str, separator: Optional[Union[List[str], str]] = None, type_constraint: bool = True) -> Any:
    """
    Return a list of string or the object itself if the type_constraint is equals False!
    Splits a string into a list of strings using the specified separator(s), based on the built-in common separators.
    Return an error if it's not a string or return the object if type_constraint is set as False!

    Args:
        input_string (str): The input string to split.
        separator (Optional[Union[List[str], str]], optional): The separator(s) to use when splitting the input string.
            This can be a single string, a list of strings, or None. If None, the function will attempt to determine
            the appropriate separator based on the input string. Defaults to None.
        type_constraint (bool, optional): If True (default), raise an exception if input_string is not a string.

    Returns:
        List[str]: A list of strings resulting from splitting the input string using the specified separator(s).

    !!! Example "This example shows how to use `split_by_separator()` to split a string using a single separator"

        === "Example 1"
            ```python
            split_by_separator("one,two,three", ",")
            ```
            Returns:
            ```
            ["one", "two", "three"]
            ```

        === "Example 2"
            ```python
            split_by_separator("one-two three|four", ["-", " ", "|"])
            ```
            Returns:
            ```
            ['one', 'two three|four']
            ```
            !!! Warning
                Only one separator frequency found in the list provided, so the priority will be respected!

        === "Example 3"
            ```python
            split_by_separator("one two three four")
            ```
            Returns:
            ```
            ["one", "two", "three", "four"]
            ```
    Raises:
        TypeError: If the input string is not a string and `type_constraint` is True.

    Tips:
        - If the input string contains multiple consecutive instances of the specified separator(s), the resulting
          list may contain empty strings. To remove empty strings from the resulting list, you can use a list
          comprehension to filter out any empty strings.
        - See the `get_separator` for more details about how the function will attempt to determine the appropriate separator.

    Info: Important
        - If the separator is a list of strings, the function will attempt to determine the appropriate separator
          to use based on the input string. If no appropriate separator was found, the function will return the
          original input string as a single-element list.
    """

    if isinstance(input_string, str):
        input_string = input_string.strip()

        if separator is None:
            # Trying to identify the separator from the common separators!
            target_separator = get_separator(input_string=input_string)
            if target_separator is not None:
                return input_string.split(target_separator)
            else:
                return input_string
        elif isinstance(separator, list):
            # Trying to identify the separator by frequency and priority from the list passed!
            target_separator = get_separator(input_string=input_string, separator_list=separator)
            if target_separator is not None:
                return input_string.split(target_separator)
            else:
                return input_string
        else:
            return input_string.split(separator)

    elif type_constraint:
        raise ValueError("Error: The value passed is not a string.")
    else:
        print("Skipping: The value passed is not a string.")
        return input_string


def cast_separator_to_comma(input_string: str, separator: Optional[str] = None) -> str:
    """

    Replaces a specified separator or the automatically detected one with a comma in the input string.

    Args:
        input_string (str): The input string to replace separators in.
        separator (Optional[str], optional): The separator to replace with a comma. If None, the function will
            attempt to determine the appropriate separator based on the input string. Defaults to None.

    Returns:
        str: A string resulting from replacing the specified or detected separator with a comma.

    !!! Example "This example shows how to use `cast_separator_to_comma()` to replace a separator in a string"

        === "Example 1"
            ```python
            cast_separator_to_comma("one-two-three", "-")
            ```
            Returns:
            ```
            "one,two,three"
            ```

        === "Example 2"
            ```python
            cast_separator_to_comma("one two three")
            ```
            Returns:
            ```
            "one,two,three"
            ```
            !!! Warning
                The function will only attempt to detect the separator when the `separator` argument is None.

    Tips:
        - If the input string does not contain the specified or detected separator, the function will return the
          original input string unchanged.
        - See the `get_separator` function for more details about how the function will attempt to detect the separator.
    """

    # Simple cleansing
    input_string = input_string.strip()

    if separator is not None:
        return input_string.replace(separator, ",")
    else:
        separator = get_separator(input_string=input_string)
        if separator is not None:
            return input_string.replace(separator, ",")
        else:
            return input_string
