#!/usr/bin/python3
"""Defines a object attribute lookup functions."""


def lookup(obj):
    """Return the list of an object available attributes."""
    return (dir(obj))
