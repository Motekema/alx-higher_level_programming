#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json

def save_to_json_file(my_obj, filename):
    """
    Serialize an object to its JSON representation and save it to a text file.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write the JSON representation to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
