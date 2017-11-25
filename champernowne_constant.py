# An irrational decimal fraction is created by concatenating the positive
# integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of
# the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
from unittest import TestCase


def get_nth_digit(number, digit_position):
    str_number = str(number)
    if digit_position > 0 and digit_position <= len(str_number):
        return int(str_number[digit_position - 1])
    return None


class Tests(TestCase):
    def setUp(self):
        self.number = 1210567

    def test_get_nth_digit(self):
        self.assertEqual(0, get_nth_digit(number=self.number, digit_position=4))
        self.assertEqual(None, get_nth_digit(number=self.number, digit_position=100))
