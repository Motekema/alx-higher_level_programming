#!/usr/bin/python3
"""Define a Square class."""

class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize a square with a specified size.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The size to set.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size * self._size

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Check if two squares have unequal areas."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Check if one square's area is greater than the other's."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Check if one square's area is greater than or equal to the other's."""
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """Check if one square's area is less than the other's."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Check if one square's area is less than or equal to the other's."""
        return self.__lt__(other) or self.__eq__(other)
