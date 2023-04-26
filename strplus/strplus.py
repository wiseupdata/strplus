from typing import List, Optional, Union

from strplus.cases import to_camel, to_pascal, to_snake
from strplus.functions import (cast_separator_to_comma, split_by_separator,
                               to_list)


class Str(str):
    """

    !!! Info "Str Class"

        The Str Class is a Wrapper class that extends the str Class, giving it superpowers
        to handle strings and making it easy to use the strplus functions! You don't need to import, only if you want!
        All methods from Str are recursive and return the Str object itself, so you always have the same features in the result.

    !!! Example "Easy and simple no parentheses!"

        === "Snake case"
            ```python
            my_string = Str("Cast_this_StringToSnake")
            my_string.snake
            ```
            cast_this_string_to_snake

        === "Camel case"
            ```python
            my_string = Str("cast_this_string_to_camel")
            my_string.camel
            ```
            castThisStringToCamel

        === "Pascal"
            ```python
            my_string = Str("Cast_this_string_TO_Pascal!")
            my_string.pascal
            ```
            CastThisStringToPascal


    !!! Tip "Use parentheses if you prefer!"

        ```python
        my_string = Str("HelloWorld")
        my_string.to_snake()

        ```
        hello_world

    """

    def __new__(cls, *args, **kwargs):
        if not all(isinstance(arg, str) for arg in args):
            raise TypeError("Str argument must be a string")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__()

        def __new__(cls, *args, **kwargs):
            return super().__new__(cls, *args, **kwargs)

    @property
    def pascal(self):
        """
        Cast itself to PascalCase!
        This attribute is an alias for [`to_pascal`][strplus.Str.to_pascal]
        """
        return self.to_pascal()

    @property
    def camel(self):
        """
        Cast itself to camelCase!
        This attribute is an alias for [`to_camel`][strplus.Str.to_camel]
        """
        return self.to_camel()

    @property
    def snake(self):
        """
        Cast itself to snake_case!
        This attribute is an alias for [`to_snake`][strplus.Str.to_snake]
        """
        return self.to_snake()

    @property
    def list(self):
        """
        Split itself into a list!
        This attribute is an alias for [`to_list`][strplus.Str.to_list]
        """
        return self.to_list()

    @property
    def split_by_sep(self):
        """
        Splits itself into a list of strings based on the built-in common separators.
        This attribute is an alias for the function[`split_by_separator`][strplus.Str.split_by_separator]

        Tip: Use
            - If you need to to inform a different list in can call the the function split_by_separator from this class
              and inform your custom list of separators!
            - You can find examples of use in menu examples.str_class

        """
        return self.split_by_separator(type_constraint=False)

    @property
    def separator_as_comma(self):
        """
        Looks for a separator in your own value and cast it to comma!
        separator_as_comma is an alias for [`cast_separator_to_comma`][strplus.Str.cast_separator_to_comma]
        """
        return self.cast_separator_to_comma()

    @property
    def print(self):
        """
        Print itself!
        This attribute is an alias for `str.print`
        """
        print(self)

    def to_pascal(self):
        """
        Simple method to converts a string to PascalCase.
        Implementation of [strplus.cases.to_pascal][]

        Returns:
            str: The PascalCase version of the input string.

        !!! Example

            ```python
            my_string = Str('some-mixed_string With spaces_underscores-and-hyphens')
            my_string.to_pascal()
            ```
            SomeMixedStringWithSpacesUnderscoresAndHyphens
        """
        return Str(to_pascal(self))

    def to_camel(self):
        """
        Converts a string from any case to CamelCase.
        Implementation of [strplus.cases.to_camel][]

        Returns:
            str: The converted string in CamelCase.

        !!! Example

            === "Example 01"
                ```
                my_string = Str('this_is-an_example')
                my_string.to_camel()
                ```
                thisIsAnExample

            === "Example 02"
                ```
                my_string = Str('This is a test!')
                my_string.to_camel()
                ```
                thisIsATest
        """
        return Str(to_camel(self))

    def to_snake(self):
        """
        Converts a string to snake_case.
        Implementation of [strplus.cases.to_snake][]

        Returns:
            str: The string converted to snake_case.

        !!! Example "Examples"

            === "Example 01"
                ```
                my_string = Str("HelloWorld")
                my_string.snake("HelloWorld")
                ```
                hello_world

            === "Example 02"
                ```
                my_string = Str("  AnotherString!  ")
                my_string.to_snake()
                ```
                another_string

            === "Example 03"
                ```
                my_string = Str("hello-world")
                my_string.to_snake()
                ```
                hello_world
        """
        return Str(to_snake(self))

    def to_list(self):
        """
        Converts a string to a list of strings, where each word is a separate element in the list.
        Implementation of [strplus.functions.to_list][]

        Returns:
            List[str]: A list of strings, where each word in the input string is a separate element in the list.

        !!! Example "Converting a string to a list"
            This example shows how to use `to_list()` to convert a string to a list.

            === "Example 1"
                ```python
                my_string = Str('hello world')
                my_string.to_list
                ```
                ['hello', 'world']


            === "Example 2"
                ```python
                my_string = Str('some-mixed_string With spaces_underscores-and-hyphens')
                my_string.to_list
                ```
                ['some', 'mixed', 'string', 'With', 'spaces', 'underscores', 'and', 'hyphens']

            === "Example 2"
                ```python
                my_string = Str('123abc')
                my_string.to_list
                ```
                ['123abc']

        Tip: Use tips
            - If you need to convert a string to a list of integers or floats, you can use list comprehension to convert each element to the desired type.
            - If you need to remove duplicates from the list, you can convert it to a set and then back to a list.

        Info: Important
            - For best results, avoid using punctuation or non-alphanumeric characters in the input string.
            - This function uses regular expressions to identify words in the input string.
        """
        return [Str(word) for word in to_list(self)]

    def split_by_separator(self, separator: Optional[Union[List[str], str]] = None, type_constraint=True):
        """
        Splits a string into a list of strings using the specified separator(s), base in the built-in common separators.
        Implementation of [strplus.functions.split_by_separator][]

        Args:
            input_string (str): The input string to split.
            separator (Optional[Union[List[str], str]], optional): The separator(s) to use when splitting the input string.
                This can be a single string, a list of strings, or None. If None, the function will attempt to determine
                the appropriate separator based on the input string. Defaults to None.

        Returns:
            List[str]: A list of strings resulting from splitting the input string using the specified separator(s).

        !!! Example "This example shows how to use `split_by_separator()` to split a string using a single separator"

            === "Example 1"
                ```python
                my_string = Str("one,two,three")
                my_string.split_by_separator(",")
                ```
                Returns:
                ```
                ["one", "two", "three"]
                ```

            === "Example 2"
                ```python
                my_string = Str("one-two three|four")
                my_string.split_by_separator(["-", " ", "|"])
                ```
                Returns:
                ```
                ['one', 'two three|four']
                ```
                !!! Warning
                    Only one separator frequency found in the list provided, so the priority will be respect!

            === "Example 3"
                ```python
                my_string = Str("one two three four")
                my_string.split_by_separator()
                ```
                Returns:
                ```
                ["one", "two", "three", "four"]
                ```

        Tips:
            - If the input string contains multiple consecutive instances of the specified separator(s), the resulting
            list may contain empty strings. To remove empty strings from the resulting list, you can use a list
            comprehension to filter out any empty strings.
            - See the `get_separator` for mor details about how the function will attempt to determine the appropriate separator.

        Info: Important
            - If the separator is a list of strings, the function will attempt to determine the appropriate separator
            to use based on the input string. If no appropriate separator is found, the function will return the
            original input string as a single-element list.
        """
        result = split_by_separator(self, separator=separator, type_constraint=type_constraint)
        result = [Str(word) for word in result] if isinstance(result, list) else result
        return result

    def cast_separator_to_comma(self, separator: Optional[str] = None):
        """
        Replaces a specified separator or the automatically detected one with a comma in the input string.
        Implementation of [strplus.functions.cast_separator_to_comma][]

        Args:
            input_string (str): The input string to replace separators in.
            separator (Optional[str], optional): The separator to replace with a comma. If None, the function will
                attempt to determine the appropriate separator based on the input string. Defaults to None.

        Returns:
            str: A string resulting from replacing the specified or detected separator with a comma.

        !!! Example "This example shows how to use `cast_separator_to_comma()` to replace a separator in a string"

            === "Example 1"
                ```python
                my_string = Str("one-two-three", "-")
                my_string.cast_separator_to_comma("-")
                ```
                Returns:
                ```
                "one,two,three"
                ```

            === "Example 2"
                ```python
                my_string = Str("one two three")
                my_string.cast_separator_to_comma()
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
        return cast_separator_to_comma(self, separator=separator)

    @staticmethod
    def cast(input_value: any, join_sep: str = ",", type_constraint: bool = True):
        """
        Casts the input value to Str+. If it's a list will be joined by comma or you can define you custom separator to join the elements.

        Args:
            input_value (any): The input value to cast.
            join_sep (str, optional): The separator to join list elements with. Defaults to ",".
            type_constraint (bool, optional): If True (default), raise a ValueError if the input value is not a string or a list.

        Returns:
            Str: A string or a string representation of a list of values joined by the specified separator.

        !!! Example "This example shows how to use `cast()` to cast an input value to a string"
            === "Example 1"
                ```python
                Str.cast("Hello, world!")
                ```
                Returns:
                ```
                "Hello, world!"
                ```
                Type: strplus.strplus.Str

            === "Example 2"
                ```python
                Str.cast(["apple", "banana", "orange"], join_sep="-")
                ```
                Returns:
                ```
                "apple-banana-orange"
                ```
                Type: strplus.strplus.Str

            === "Example 3"
                ```python
                Str.cast(123, type_constraint=False)
                ```
                Returns:
                ```
                Skipping: It's not possible to cast from type: <class 'int'>
                123
                ```
                Type: int

        Raises:
            ValueError: If the input value is not a string or a list and `type_constraint` is True.

        Tips:
            - If the input value is a list, the resulting string will be a string representation of the list elements joined by the specified separator.
        """
        if isinstance(input_value, str):
            return Str(input_value)
        elif isinstance(input_value, list):
            return Str(f"{join_sep}".join(input_value))
        else:
            if type_constraint:
                raise ValueError(f"Error: It's not possible to cast from type: {type(input_value)}")
            else:
                print(f"Skipping: It's not possible to cast from type: {type(input_value)}")
                return input_value


for name in dir(str):
    if not name.startswith("__"):
        original_method = getattr(str, name)
        setattr(Str, name, original_method)

        if callable(original_method):

            def wrapper(func):
                def wrapped(self, *args, **kwargs):
                    result = func(self, *args, **kwargs)
                    if isinstance(result, str):
                        return Str(result)
                    elif isinstance(result, list):
                        return [Str(s) for s in result]
                    return result

                # Use docstring from the original method
                wrapped.__doc__ = original_method.__doc__
                return wrapped

            # Replace method with wrapped version
            setattr(Str, name, wrapper(getattr(Str, name)))
