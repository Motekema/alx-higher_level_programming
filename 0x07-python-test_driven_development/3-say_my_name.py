#!/usr/bin/python3
"""
This is "3-say_my-name" module.

3-say_my_name  module supplies one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is" followed by the first names and optional last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be string")
    if type(last_name) is not str:
        raise TypeError("last_name must be string")
    print("My name is", first_name, last_name)
