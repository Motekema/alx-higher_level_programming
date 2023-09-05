#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the ASCII alphabet, in lowercase, not followed by a new line."""
alphabet = [chr(letter) for letter in range(97, 123)]
print("".join(alphabet), end="")
