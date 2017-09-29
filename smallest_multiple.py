# Project Euller - Problem 5 - Smallest Multiple
# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
from unittest import TestCase


def get_smallest_multiple(divisors):
    smallest_multiple = 0
    m = max(divisors)
    while True:
        divisor_count = 0
        smallest_multiple+=m
        for divisor in divisors:
            if n % divisor:
                divisor_count+=1
        if divisor_count == len(divisors):
            break
    return smallest_multiple


class Tests(TestCase):
    def test_smallest_multiple_from_1_to_10(self):
        self.assertEquals(2520, get_smallest_multiple(list(range(1,11))))
