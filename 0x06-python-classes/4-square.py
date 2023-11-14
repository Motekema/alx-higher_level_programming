#!/usr/bin/python3
"""Module documentation - Represents a square."""

class Square:
    """Class documentation - Represents a square."""

    def __init__(self, size=0):
        """Initialize the property size with the provided size."""
        self.size = size

    @property
    def size(self):
        """Getter method for retrieving the size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter method for setting the size attribute and performing type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size * self._size
