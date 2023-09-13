#!/usr/bin/python3
def search_replace(my_list, search, replace):
    old_list = [replace if x == search else x for x in my_list]
    return (old_list)
