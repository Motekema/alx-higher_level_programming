#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

# Define the values for a and b
a = 10
b = 5

# Call and print the results of each function using the specified format
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
