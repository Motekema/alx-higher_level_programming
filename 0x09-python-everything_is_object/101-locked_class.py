#!/usr/bin/python3
"""Defines locked class."""

class LockedClass:
    """
    Prevent  user from instantiating new LockedClass attribute
    for anything but attribute called 'first_name'.
    """

    __slots__ = ["first_name"]
