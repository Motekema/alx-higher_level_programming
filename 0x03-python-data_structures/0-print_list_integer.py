#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for integer in my_list:
        print("{:d}".format(integer))

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
