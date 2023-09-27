#!/usr/bin/python3
"""Define a Square class."""

class Square:
    """Class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of two positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position as a tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the square using the '#' character and position."""
        if self._size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()
            for _ in range(self._size):
                print(" " * self._position[0] + "#" * self._size)

    def __str__(self):
        """Convert the square to a string for printing."""
        result = []
        for _ in range(self._position[1]):
            result.append("")
        for _ in range(self._size):
            result.append(" " * self._position[0] + "#" * self._size)
        return "\n".join(result) 
