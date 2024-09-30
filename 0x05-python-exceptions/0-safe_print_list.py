#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    real_number = 0

    try:
        for real_number in range(x):
            print("{}".format(my_list[real_number]), end="")
        print("")
    except IndexError:
        print("")
        return real_number
    else:
        return real_number + 1
