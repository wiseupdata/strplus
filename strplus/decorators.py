def copy_docstring(func):
    def wrapper(to_func):
        if to_func.__doc__ is None:
            to_func.__doc__ = func.__doc__
        return to_func

    return wrapper
