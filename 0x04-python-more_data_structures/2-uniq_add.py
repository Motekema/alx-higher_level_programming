#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num1 = 0

    for i in uniq_list:
        num1 += i

    return (num1)
