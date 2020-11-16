#!/usr/bin/env python3
# -*- coding: UTF=8 -*-

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def primes():
    prime = 13
    num = 6
    while num != 10001:
        prime += 2
        if isPrime(prime):
            num += 1
    return prime


if __name__ == '__main__':
    print(primes())
