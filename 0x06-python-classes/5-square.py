#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """ Initialize the property size with the provided size."""
        self.size = size

    @property
    def size(self):
        """ Getter method for retrieving the size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """ Setter method for setting the size attribute and performing type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """ Calculate and return the area of the square."""
        return self._size * self._size

    def my_print(self):
        """ Print the square using the '#' character."""
        if self._size == 0:
            print()
        else:
            for _ in range(self._size):
                print("#" * self._size)
