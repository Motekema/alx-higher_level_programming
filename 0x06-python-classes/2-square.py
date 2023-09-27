#!/usr/bin/python3
"""Module documentation - Represents a square."""

class Square:
    """Class documentation - Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # Check if size is not an integer, and raise a TypeError if it's not.
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if size is less than 0, and raise a ValueError if it is.
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            # Initialize the private attribute _size with the provided size.
            self._size = size

