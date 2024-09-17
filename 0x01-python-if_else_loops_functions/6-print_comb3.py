#!/usr/bin/python3

# Problem: Trying to print all the numbers smaller than 100
#          that is combination of two different digits
# Ex: Right: 10 20 23 19 89 54 24
#     False: 11 22 99 55
# Note: 10 = 01, 20 = 02, 23 = 32, 25 = 52

# Numbers to print:
# * possible different combinations of two digits 09 12 23
# * only combinations where the first digit is smaller than the second
#   (e.g., 01, 12, 34) should be printed.
# * 01 and 10 are considered the same combination of the two digits 0 and 1


# Numbers to avoid:
# - 11 22 33 44 55 66 77 88 99 --> same digits
# - 21 10 20 30 31 32  40 41 42 43 51 52 53 54 61 62 63 64 65 -->

# 12 = 21 --> 12

# *****************************************************************************

# make nested loop
# Outer loop: for first digit and in range 1 to 9 --> i
# inner loop: for the second digit and in range
#             of the rest of numbers of the first digit (i+1, 9) --> j
# i should be less than j --> i < j

for i in range(0, 10):
    for j in range(i+1, 10):
        if i != j and i < j:
            print("{}{}".format(i, j), end=", " if i != 8 or j != 9 else "\n")