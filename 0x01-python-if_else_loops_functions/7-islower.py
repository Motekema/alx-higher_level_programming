#!/usr/bin/python3
# 7-islower.py


def islower(o):
    """Check for lowercase."""
    if ord(o) >= 97 and ord(o) <= 122:
        return True
    else:
        return False

