#!/usr/bin/python3
"""
Module: base_geometry

This module contains the BaseGeometry class.
"""

class BaseGeometry:
    """
    BaseGeometry class.

    Public instance method:
        - area(self): Raises an Exception with the message "area() is not implemented."

    """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

