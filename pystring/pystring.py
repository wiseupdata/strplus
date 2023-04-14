class Str(str):
    def __init__(self, wrapped_str):
        if not isinstance(wrapped_str, str):
            raise TypeError("wrapped_str must be a string")
        super().__init__()
        self.update(wrapped_str)

    def __getattr__(self, attr):
        return getattr(self, attr)

    def __getitem__(self, key):
        item = super().__getitem__(key)
        if isinstance(item, str):
            return Str(item)
        return item

    def __instancecheck__(self, instance):
        return isinstance(instance, str)

    def __subclasscheck__(self, subclass):
        return issubclass(subclass, str)
