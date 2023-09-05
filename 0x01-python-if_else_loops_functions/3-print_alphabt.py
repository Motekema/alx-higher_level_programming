#!/usr/bin/python3
output_string = ""
for letters in range(97, 123):
    if chr(letters) != 'q' and chr(letters) != 'e':
        output_string += chr(letters)

print(output_string)
