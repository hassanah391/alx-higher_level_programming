#!/usr/bin/python3
from sys import argv


def sum_all(argv):
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    return sum


if __name__ == "__main__":
    print("{}".format(sum_all(argv)))
