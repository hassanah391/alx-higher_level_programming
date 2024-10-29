#!/usr/bin/python3
"""
This Module 0-add_integer holds add_integer()
"""


def add_integer(a, b=98):
    """ Returns summtion of 2 integers
    Example:

    >>> add_integer(1, 2)
    3

    >>> add_integer(100, -2)
    98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)

    return a + b
