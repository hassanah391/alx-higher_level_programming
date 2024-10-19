#!/usr/bin/python3
"""
Module 7-add_item: A python script that adds all arguments to a Python list,
                   and then saves them to a file.
"""
from sys import argv

# Importing the required functions from the provided modules
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    # Try to load the existing list from the file
    pylist = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, initialize an empty list
    pylist = []

# Extend the list with the new command-line arguments
pylist.extend(argv[1:])

# Save the updated list back to the file
save_to_json_file(pylist, filename)
