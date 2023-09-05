#!/usr/bin/python3
for t in range(0, 9):
    for z in range(t + 1, 10):
        if z < 9:
            print("{:02d}, ".format(t), end='')
        else:
            print("{:02d}".format(t), end='')
        print("{:02d}".format(z), end=', ')
        print("{:02d}".format(89))
