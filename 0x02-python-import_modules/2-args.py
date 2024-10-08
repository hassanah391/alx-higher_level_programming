#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    if len(argv) <= 1:
        print("{} arguments".format(len(argv) - 1), end=".\n")
    else:
        print("{} argument".format(len(argv) - 1), end=":\n"
              if len(argv) == 2 else "s:\n")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
