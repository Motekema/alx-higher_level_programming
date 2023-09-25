#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
ret = 0
for i in range(x):
try:
print("Element {}: {}".format(i + 1, my_list[i]), end=" ")
ret += 1
except IndexError:
break
print("")
return ret
if __name__ == "__main__":
my_list = ["apple", "banana", "cherry", "date"]
elements_printed = safe_print_list(my_list, 3)
print("Number of elements printed:", elements_printed)
