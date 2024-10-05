#!/usr/bin/python3
""" This module for square class """


class Square:
    """ for creating a square """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (isinstance(position, tuple) and
                len(position) == 2 and
                all(isinstance(i, int) and i >= 0 for i in position)):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            [print() for _ in range(self.__position[1])]
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
