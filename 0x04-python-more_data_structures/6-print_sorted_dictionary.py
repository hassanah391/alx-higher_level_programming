#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedBykeys = dict(sorted(a_dictionary.items()))
    for k, v in sortedBykeys.items():
        print("{}: {}".format(k, v))
