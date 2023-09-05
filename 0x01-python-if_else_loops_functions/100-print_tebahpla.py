#!/usr/bin/python3

for h in range(ord('z'), ord('a') - 1, -1):
    letters = chr(h)
    uppercase_letter = letters.upper()
    print("{}".format(uppercase_letter), end="")
