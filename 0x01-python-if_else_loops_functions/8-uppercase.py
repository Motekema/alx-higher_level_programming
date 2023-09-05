#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
"""Print a string with uppercase."""
for o in str:
if ord(o) >= 97 and ord(o) <= 122:
o = chr(ord(o) - 32)
print("{}".format(o), end="")
print("")


