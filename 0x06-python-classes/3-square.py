#!/usr/bin/python3
""" This module for square class """


class Square:
    """ for creating a square """
    def __init__(self, s=0):
        if type(s) is not int:
            raise TypeError("size must be an integer")
        elif s < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = s

    def area(self):
        area = self.__size * self.__size
        return area
