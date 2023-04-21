from strplus.cases import to_camel, to_pascal, to_snake
from strplus.functions import to_list


class Str(str):
    """

    !!! info

        The Str Class is a Wrapper class that extends the str Class, giving it superpowers
        to handle strings and making it easy to use the strplus functions! You don't need to import, only if you want!
        All methods from Str are recursive and return the Str object itself, so you always have the same features in the result.

    !!! example "Never was so easy! Simple no parentheses! "

        === "Snake case"
            ```python
            my_string = Str("Cast_this_StringToSnake")

            my_string.snake
            ```
            'cast_this_string_to_snake'

        === "Camel case"
            ```python
            my_string = Str("cast_this_string_to_camel")

            my_string.camel
            ```
            'castThisStringToCamel'

        === "Pascal"
            ```python
            my_string = Str("Cast_this_string_TO_Pascal!")

            my_string.pascal
            ```
            'CastThisStringToPascal'


    !!! tip "Use parentheses if you prefer!"

        === "Snake case"
            ```python
            my_string = Str("HelloWorld")

            my_string.to_snake()

            ```
            'hello_world'
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
        !!! info
            Simple method to converts a string to PascalCase.
            Extend the method: to_pascal

        Returns:
            str: The PascalCase version of the input string.


        !!! example

            ```python
            my_string = Str('some-mixed_string With spaces_underscores-and-hyphens')

            my_string.to_pascal()
            ```
            'SomeMixedStringWithSpacesUnderscoresAndHyphens'

        """
        return Str(to_pascal(self))

    def to_camel(self):
        """Converts a string from any case to CamelCase.

        Returns:
            str: The converted string in CamelCase.

        Examples:

            >>> my_string = Str('this_is-an_example')
            >>> my_string.to_camel()
            'thisIsAnExample'

            >>> my_string = Str('This is a test!')
            >>> my_string.to_camel()
            'thisIsATest'

        """
        return Str(to_camel(self))

    def to_snake(self):
        """Converts a string to snake_case.

        Returns:
            str: The string converted to snake_case.

        Examples:

            >>> my_string = Str("HelloWorld")
            >>> my_string.snake("HelloWorld")
            'hello_world'

            >>> my_string = Str("  AnotherString!  ")
            >>> my_string.to_snake()
            'another_string'

            >>>  my_string = Str("hello-world")
            >>> my_string.to_snake()
            'hello_world'

        """
        return Str(to_snake(self))

    def to_list(self):
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
