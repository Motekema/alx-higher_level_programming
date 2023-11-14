#!/usr/bin/python3
"""
Module: 10-square

This module contains the Square class, which inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Args:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.__size = 0  # Initialize size
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The square description in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"

