#!/usr/bin/python3
"""Module documentation - Define a class Square."""

class Square:
    """Class documentation - Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size and position properties with the provided values.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method for retrieving the position attribute."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter method for setting the position attribute and performing type and value validation."""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the square using the '#' character, considering the position."""
        if self._size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()
            for _ in range(self._size):
                print(" " * self._position[0] + "#" * self._size)

