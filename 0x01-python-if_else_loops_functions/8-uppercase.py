#!/usr/bin/python3


def uppercase(str):
    if len(str) == 0:  # Check if the string is empty
        return
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print("{}".format(chr(ord(str[i]) - 32)), end="" if
                  i != len(str) - 1 else "\n")
        else:
            print("{}".format(str[i]), end="" if i != len(str) - 1 else "\n")
