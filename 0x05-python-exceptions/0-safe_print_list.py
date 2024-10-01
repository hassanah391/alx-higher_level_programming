#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    real_number = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            real_number += 1
        print("")
    except IndexError:
        print("")
        return real_number
    else:
        return real_number
