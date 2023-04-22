from strplus.cases import to_camel, to_pascal, to_snake
from strplus.functions import to_list


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
        return self.to_pascal()

    @property
    def camel(self):
        return self.to_camel()

    @property
    def snake(self):
        return self.to_snake()

    @property
    def list(self):
        return self.to_list()

    @property
    def print(self):
        print(self)

    def to_pascal(self):
        """

        Simple method to converts a string to PascalCase.
        Extend the method: to_pascal

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
