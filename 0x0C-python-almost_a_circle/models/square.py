#!/usr/bin/python3
"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square.

    Attributes:
        size (int): The size of the square.
        x (int): The x coordinate of the square.
        y (int): The y coordinate of the square.
        id (int): The identity of the square.

    Methods:
        update(self, *args, **kwargs): Update the square's attributes.
        to_dictionary(self): Return a dictionary representation of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square's attributes.

        Args:
            *args (ints): New attribute values in the order id, size, x, y.
            **kwargs (dict): New key-value pairs of attributes.
        """
        if args:
            attribute_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attribute_names):
                    setattr(self, attribute_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the Square's attributes.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a string representation of the Square for print() and str()."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

