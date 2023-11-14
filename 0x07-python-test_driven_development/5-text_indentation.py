#!/usr/bin/python3
"""
This the "5-test_indentation" module.

5-test_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Splits a text into lines along '?', ':', and '.' followed by two new lines.

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If text is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be string")
    
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")

