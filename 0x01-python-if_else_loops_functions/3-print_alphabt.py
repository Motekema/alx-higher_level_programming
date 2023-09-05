#!/usr/bin/python3
output_string = ""
for letter_code in range(97, 123):
    letter = chr(letter_code)
    if letter != 'q' and letter != 'e':
        output_string += "{}".format(letter)
print(output_string)
