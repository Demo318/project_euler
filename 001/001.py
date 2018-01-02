#! /usr/bin/env python3

# Written in Python 3.6.3
# Execute in bash using "./001.py"


# Project Euler
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import functools
import operator

print("Find the sum of all natural numbers which are multiples")
print("of 3 or 5 up to a given number.")
user_number = int(input("Please enter a number:"))

eligible_numbers = []

for i in range(user_number):
    if i % 3 == 0 or i % 5 == 0:
        eligible_numbers.append(i)

final_sum = functools.reduce(operator.add, eligible_numbers)

print("All natural numbers below " + str(user_number) + ":")
print(str(eligible_numbers))

print("Your final result is: " + str(final_sum))
