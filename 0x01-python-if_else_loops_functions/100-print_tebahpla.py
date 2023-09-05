#!/usr/bin/python3

h = 0
for h in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(h - h)), end="")
    h = 32 if h == 0 else 0
