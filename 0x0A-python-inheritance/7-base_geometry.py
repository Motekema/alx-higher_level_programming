#!/usr/bin/python3
"""
Module: base_geometry

This module contains the BaseGeometry class.
"""

class BaseGeometry:
    """
    BaseGeometry class.

    Public instance methods:
        - area(self): Raises an Exception with the message "area() is not implemented."
        - integer_validator(self, name, value): Validates the value.

    """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name: A string representing the name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

