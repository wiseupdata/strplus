from strplus.cases import to_pascal, to_camel, to_snake, to_list

class Str(str):
    def __new__(cls, *args, **kwargs):
        if not all(isinstance(arg, str) for arg in args):
            raise TypeError("Str argument must be a string")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__()
        def __new__(cls, *args, **kwargs):
            return super().__new__(cls, *args, **kwargs)
    
    def pascal(self):
        return Str(to_pascal(self))
    def camel(self):
        return Str(to_camel(self))
    def snake(self):
        return Str(to_snake(self))
    def list(self):
        return [Str(word) for word in to_list(self) ]

def _convert_strings(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if isinstance(result, str):
            return Str(result)
        elif isinstance(result, list):
            return [Str(s) for s in result]
        return result
    return wrapper

for name in dir(str):
    if not name.startswith('__'):
        setattr(Str, name, _convert_strings(getattr(str, name)))