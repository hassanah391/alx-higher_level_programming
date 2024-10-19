#!/usr/bin/python3
"""

Module 2-append_write contains:
append_write: a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
    Args:
        filename: name of the file
        text: text to be inserted
    Return:
          the number of characters added
    """
    chars_number = 0       # number of characters added
    with open(filename, mode="a", encoding="utf-8") as f:
        chars_number = (f.write(text))
    return chars_number
