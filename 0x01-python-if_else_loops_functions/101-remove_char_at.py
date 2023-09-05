#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, g):
if g < 0:
return (str)
return (str[:g] + str[g+1:])
