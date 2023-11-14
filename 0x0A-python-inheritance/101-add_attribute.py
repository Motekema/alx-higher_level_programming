#!/usr/bin/python3
"""Defines the function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add the new attributes to an object if is possible.

    Args:
        obj (any): The object to add the attributes to.
        att (str): The name of the attribute to the add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute can not be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("cannot add new attribute")
    setattr(obj, att, value)
