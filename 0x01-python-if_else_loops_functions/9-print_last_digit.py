#!/usr/bin/python3

def print_last_digit(numbers):
    last_digit = abs(numbers) % 10
    print(last_digit, end="")
    return last_digit
