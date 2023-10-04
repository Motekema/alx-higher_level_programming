#!/usr/bin/python3
"""
This is  "0-add_integer" module.

The 0-add_integer module supply function, add_integer(a, b).
"""


def add_integer(a, b):
    """
    Return the addition of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int: The sum of a and b, cast to an integer.

    Raises:
        TypeError: If a or b is not an integer or a float.

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

