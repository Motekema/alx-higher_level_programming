#!/usr/bin/python3

def uppercase(str):
    for j in str:
        if ord(j) >= 97 and ord(j) <= 122:
            j = chr(ord(j) - 32)
            print("{}".format(j), end="")
            print("")
