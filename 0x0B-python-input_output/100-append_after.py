#!/usr/bin/python3
"""Defines the text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing the given string in an file.

    Args:
        filename (str): the name of the file.
        search_string (str): the string to search for within the file.
        new_string (str): the string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
