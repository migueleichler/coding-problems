# An irrational decimal fraction is created by concatenating the positive
# integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of
# the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
from unittest import TestCase
import math


def get_nth_digit(number, digit_position):
    if digit_position > 0 and digit_position <= len(number):
        return int(number[digit_position - 1])
    return -1


def create_champernowne_constant(last_digit_position):
    champernowne_constant = ''
    for i in range(1, last_digit_position + 1):
        champernowne_constant = champernowne_constant + str(i)
    return champernowne_constant


def champernowne_constant():
    result = 1
    power = 1
    champernowne_constant = create_champernowne_constant(1000000)
    for i in range(0, len(champernowne_constant) + 1):
        if i == math.pow(10, power):
            power += 1
            result = result * get_nth_digit(champernowne_constant, i)

    return result


class Tests(TestCase):
    def setUp(self):
        self.number = '12345678910'

    def test_get_nth_digit(self):
        self.assertEqual(4, get_nth_digit(number=self.number, digit_position=4))
        self.assertEqual(-1, get_nth_digit(number=self.number, digit_position=100))

    def test_create_champernowne_constant(self):
        self.assertEqual(self.number, create_champernowne_constant(10))

    def test_champernowne_constant(self):
        self.assertEqual(210, champernowne_constant())
