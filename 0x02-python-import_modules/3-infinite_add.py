#!/usr/bin/python3
import sys

if __name__ == "__main__"
    total_sum = 0
    for arg in sys.argv[1:]:
        total_sum += int(arg)
    print("{}".format(total_sum))
