#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="\n" if count == x - 1 else " ")
                count += 1
    except (TypeError, IndexError):
        pass
    finally:
        print()
        return (count)
