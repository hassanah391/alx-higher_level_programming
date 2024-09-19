#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for c in my_string:
        if c not in "Cc":
            result += c
    return result
