#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a) + [0, 0]
    list_b = list(tuple_b) + [0, 0]
    result = [list_a[0] + list_b[0], list_a[1] + list_b[1]]
    return tuple(result)
