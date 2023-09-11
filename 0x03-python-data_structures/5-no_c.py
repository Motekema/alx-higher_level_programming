#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters 'c' and 'C' from a string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return "".join(copy)

if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
