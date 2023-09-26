#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def area(self):
        return self._size * self._size

    def my_print(self):
        if self._size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()
            for _ in range(self._size):
                print(" " * self._position[0] + "#" * self._size)
