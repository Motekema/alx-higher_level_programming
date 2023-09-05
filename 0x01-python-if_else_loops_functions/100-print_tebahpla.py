#!/usr/bin/python3

for h in range(ord('z'), ord('a') - 1, -1):
    letter = chr(h)
    if letter.islower():
        print("{}".format(letter), end="")
        for h in range(ord('Z'), ord('A') - 1, -1):
            print("{}".format(chr(h)), end="")
            print()
