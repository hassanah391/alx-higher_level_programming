#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0

if number < 0:
    last_digit = (-1 * number) % 10
    last_digit *= -1
    print(f"Last digit of {number} is {last_digit}", end="")

elif number > 0:
    last_digit = number % 10
    print(f"Last digit of {number} is {last_digit}", end="")
else:
    print(f"Last digit of {number} is 0", end="")

if last_digit > 5:
    print(" and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(" and is less than 6 and not 0")
else:
    print(" and is 0")
