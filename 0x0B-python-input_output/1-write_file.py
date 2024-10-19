#!/usr/bin/python3
"""

Module 1-write_file contains:
- write_file: a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    Args:
        filename: name of the file
        text: text to be inserted
    Return:
          the number of characters written
    """
    chars_written = 0
    with open(filename, encoding="utf-8", mode="w") as f:
       chars_written = f.write(text)

    return chars_written
