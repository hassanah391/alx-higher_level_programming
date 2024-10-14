#!/usr/bin/python3
""" This module has a class called MyList """


class MyList(list):
    """ mylist :) """
    def print_sorted(self):
        """ print a sorted list """
        print(sorted(self))
