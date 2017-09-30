# Project Euller - Problem 5 - Smallest Multiple
# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
import functools
from unittest import TestCase


def get_smallest_multiple(divisors):
    smallest_multiple = 0
    max_divisor = max(divisors)
    floor = functools.reduce(lambda x, y: x*y, divisors)
    multiple_count = 0

    for n in range(max_divisor, floor, max_divisor):
        for divisor in divisors:
            if n % divisor == 0:
                multiple_count+=1
            else:
                multiple_count = 0
                break

        if multiple_count == len(divisors):
            smallest_multiple = n
            break

    return smallest_multiple


class Tests(TestCase):
    def test_smallest_multiple_from_1_to_10(self):
        self.assertEqual(2520, get_smallest_multiple(list(range(1,11))))

    def test_smallest_multiple_from_1_to_20(self):
        self.assertEqual(232792560, get_smallest_multiple(list(range(1,21))))
