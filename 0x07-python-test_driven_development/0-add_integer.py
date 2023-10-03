#!/usr/bin/python3

"""
This module defines the add_integer function.
"""

def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): The first number.
        b (int or float, default 98): The second number.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or a float.

    Example:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98

    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

