#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    Returns: peak integer
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
