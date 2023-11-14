#!/usr/bin/python3
"""Defines the file-appending function."""


def append_write(filename="", text=""):
    """Appends the string to the end of the UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
