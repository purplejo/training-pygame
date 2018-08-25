# coding: utf-8


def singleton(parameters=False):
    """
    Return the singleton class decorator.
    -------------------------------------
    Arguments:
    - parameters: True if the instance returned by the singleton class
    decorator has to depend on the class arguments, False otherwise.
    ----------------------------------------------------------------
    Return:
    - function: the singleton class decorator.
    ------------------------------------------
    Usage:
    > import decorators
    >
    >
    > @decorators.singleton(parameters=True)
    > class Singleton(object):
    >     def __init__(self, id):
    >         pass
    >
    >
    > A = Singleton(1)
    > B = Singleton(1)
    > C = Singleton(3)
    > print(A is B)  # True
    > print(A is C)  # False
    """

    def decorator(cls):
        """Return the singleton class wrapper."""
        instances = {}

        def wrapper(*args, **kwargs):
            """Return the single instance of the cls class, depends on args."""
            key = (cls, args, str(kwargs)) if parameters else cls
            if key not in instances:
                instances[key] = cls(*args, **kwargs)
            return instances[key]

        return wrapper

    return decorator
