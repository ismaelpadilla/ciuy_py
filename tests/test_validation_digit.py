import unittest
from nose2.tools import params
import ciuy


class TestValidationDigit(unittest.TestCase):
    @params(('1111111', '1'), ('2222222', '2'), ('3333333', '3'), ('333333', '9'), ('456789', '0'))
    def test_validation_digit_string_clean(self, input, expected):
        self.assertEqual(ciuy.validation_digit(input), expected)

    @params(('1.111.111', '1'), ('2.2.2.2.2.2.2', '2'), ('3,333,333', '3'), ('333-333', '9'), ('456.789', '0'))
    def test_validation_digit_string_dirty(self, input, expected):
        self.assertEqual(ciuy.validation_digit(input), expected)

    @params((1111111, '1'), (2222222, '2'), (3333333, '3'), (333333, '9'), (456789, '0'))
    def test_validation_digit_number(self, input, expected):
        self.assertEqual(ciuy.validation_digit(input), expected)

    @params('10000', '10000000', '99999', '10000001', 10000, 10000000, 99999, 10000001)
    def test_validation_digit_raises_ValueError(self, input):
        with self.assertRaises(ValueError):
            ciuy.validation_digit(input)