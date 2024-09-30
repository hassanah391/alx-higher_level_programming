#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    real_number = 0

    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                real_number += 1
        print("")
        return real_number
    except IndexError:
        raise IndexError
        return real_number
