#!/usr/bin/python3
for t in range(0, 8):
for z in range(t + 1, 10):
print("{:d}{:d}".format(t, z), end=', ')
print("{:d}{:d}".format(t + 1, z))
