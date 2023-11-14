#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    rets = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            rets += 1
        except IndexError:
            break
    print("")
    return (rets)
