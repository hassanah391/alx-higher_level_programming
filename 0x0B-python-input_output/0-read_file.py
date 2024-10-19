#!/usr/bin/python3
"""

Module 0-read_file contains:
read_file: a function to read a text file and prints
          its content.
"""


def read_file(filename=""):
    """ reads from a text file and prints its content
    Args:
        filename (string): the name of the file to read
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end="")
