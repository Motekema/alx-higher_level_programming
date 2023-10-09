#!/usr/bin/python3
"""
Module: my_module

This module contains the is_kind_of_class function.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if it's an instance of a class that
    inherited from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of the specified class or its subclass;
        False otherwise.
    """
    return isinstance(obj, a_class)

