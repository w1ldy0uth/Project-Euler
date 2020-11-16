#!/usr/bin/env python3
# -*- coding: UTF=8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def largestprime():
    largest = None
    n = 600851475143
    for i in range(2, n):
        while n % i == 0:
            largest = i
            n //= i

        if n == 1:
            return largest

    if n > 1:
        return n


if __name__ == "__main__":
    print(largestprime())
