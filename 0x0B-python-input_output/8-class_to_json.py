#!/usr/bin/python3
"""Defines the Python class-to-JSON function."""


def class_to_json(obj):
    """Return a dictionary represntation of a simple data structure."""
    return obj.__dict__
