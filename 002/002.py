#! /usr/bin/env python3

# Written in Python 3.6.3
# Execute in bash using "./002.py"


# Project Euler
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10
# terms will be:
# 1, 2, 3, 4, 8, 13, 21, 34, 55, 89 ...
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

import functools

def next_fib_number(seq):
    '''(list) -> int
    Returns what the next number in a Fibonacci sequence would be.
    REQ: len(seq) >= 2
    >>> next_fib_number([1, 2])
    3
    >>> next_fib_number([1, 2, 3])
    5
    '''
    return seq[len(seq) - 1] + seq[len(seq) - 2]

print("Find the sum of even-numbers in the Fibonacci sequence (starting with 1 & 2)")
limit_number = int(input("limited by a given number:"))

sequence = [1, 2]

while next_fib_number(sequence) < limit_number:
    sequence.append(next_fib_number(sequence))

print(str(functools.reduce((lambda x, y: x + y), list(filter(lambda x: x % 2 == 0, sequence)))))