#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """
    Parse a JSON string and return the corresponding Python data structure.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
