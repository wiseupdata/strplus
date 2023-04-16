from strplus.cases import to_pascal, to_camel, to_snake, to_list
from strplus.decorators import copy_docstring

class Str(str):
    """A subclass of the built-in str class with additional string manipulation methods.

    This class provides several methods for converting strings to different cases, as well as a method for
    converting a string to a list of words.

    All methods that return strings return instances of the Str class, so they can be further manipulated
    with any of the methods provided by this class or by the built-in str class.

    Examples:
        >>> my_string = Str('hello_world')
        >>> my_string.pascal()
        'HelloWorld'

        >>> my_string = Str('this_is-an_example')
        >>> my_string.camel()
        'thisIsAnExample'

        >>> my_string = Str("HelloWorld")
        >>> my_string.snake()
        'hello_world'

        >>> my_string = Str("Hello, World!")
        >>> my_string.lower()
        'hello, world!'

    Note that all methods provided by the Str class are based on regular expressions, so they may not be
    appropriate for all string manipulation tasks.
    """
    def __new__(cls, *args, **kwargs):
        if not all(isinstance(arg, str) for arg in args):
            raise TypeError("Str argument must be a string")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__()
        def __new__(cls, *args, **kwargs):
            return super().__new__(cls, *args, **kwargs)
    
    def pascal(self):
        """
        Converts a string to PascalCase.
        
        Returns:
            str: The PascalCase version of the input string.
        
        Example:
            >>> my_string = Str('hello_world')
            >>> my_string.pascal()
            'HelloWorld'
            >>> my_string = Str('some-mixed_string With spaces_underscores-and-hyphens')
            >>> my_string.pascal()
            'SomeMixedStringWithSpacesUnderscoresAndHyphens'
        """
        return Str(to_pascal(self))
    
    def camel(self):
        """Converts a string from any case to CamelCase.

        Returns:
            str: The converted string in CamelCase.

        Examples:
            >>> my_string = Str('this_is-an_example')
            >>> my_string.camel()
            'thisIsAnExample'

            >>> my_string = Str('This is a test!')
            >>> my_string.camel()
            'thisIsATest'
        """
        return Str(to_camel(self))
    
    def snake(self):
        """Converts a string to snake_case.

        Returns:
            str: The string converted to snake_case.

        Examples:
            >>> my_string = Str("HelloWorld")
            >>> my_string.snake("HelloWorld")
            'hello_world'

            >>> my_string = Str("  AnotherString!  ")
            >>> my_string.snake()
            'another_string'

            >>>  my_string = Str("hello-world")
            >>> my_string.snake()
            'hello_world'
        """
        return Str(to_snake(self))
    
    def list(self):
        return [Str(word) for word in to_list(self) ]

for name in dir(str):
    if not name.startswith('__'):
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
