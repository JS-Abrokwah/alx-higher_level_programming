#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            ret += 1

        except (TypeError, ValueError, IndexError):
            continue
    print("")
    return (ret)
