class Str(str):
    def __new__(cls, wrapped_str):
        if not isinstance(wrapped_str, str):
            raise TypeError("wrapped_str must be a string")
        return super().__new__(cls, wrapped_str)

    def __getattr__(self, attr):
        return super().__getattribute__(attr)

    def __getitem__(self, key):
        if isinstance(key, int):
            item = super().__getitem__(key)
            if isinstance(item, str):
                return Str(item)
            return item
        elif isinstance(key, slice):
            return Str(super().__getitem__(key))
        else:
            raise TypeError("indices must be integers")
