
def safe_print_list_integers(my_list=[], x=0):
    output = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            output += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (output)

