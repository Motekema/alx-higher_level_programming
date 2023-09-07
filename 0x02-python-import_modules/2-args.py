#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    coun_num = len(sys.argv) - 1
    if count_num == 0:
        print("0 arguments.")
    elif count_num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count_num))
    for i in range(count_num):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
