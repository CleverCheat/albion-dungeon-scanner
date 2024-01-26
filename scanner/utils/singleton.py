kwd_mark = object()


class Singleton(type):
    """
    Metaclass for creating singleton classes.

    This metaclass ensures that only one instance of a class is created and returned on subsequent calls.

    Args:
        cls: The class object.

    Returns:
        The instance of the class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        key = (cls, *args, kwd_mark, *sorted(kwargs.items()))
        if key not in cls._instances:
            cls._instances[key] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[key]

    @classmethod
    def remove_instance(cls, *args, **kwargs):
        key = (cls, *args, kwd_mark, *sorted(kwargs.items()))
        if key in cls._instances:
            del cls._instances[key]
