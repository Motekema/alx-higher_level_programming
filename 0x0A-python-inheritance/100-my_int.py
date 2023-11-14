#!/usr/bin/python3
"""
Module: my_int

This module contains the MyInt class.
"""

class MyInt(int):
    """
    MyInt class, inherits from int.

    MyInt has == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Inverts the equality (==) operator.

        Args:
            other: The value to compare.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality (!=) operator.

        Args:
            other: The value to compare.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)

