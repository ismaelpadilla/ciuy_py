import unittest
from nose2.tools import params
import ciuy


class TestClean(unittest.TestCase):
    @params(('11111111', '11111111'), ('12345678', '12345678'), ('123456', '123456'), ('333333', '333333'))
    def test_clean_string_clean(self, input, expected):
        """
        Validates that _clean returns the correct string,
        when the input is a string without any non digit characters.
        """
        self.assertEqual(ciuy._clean(input), expected)

    @params(('1.111.111-1', '11111111'), ('1.234.567.8', '12345678'), ('1.2.3.4.5-6', '123456'), ('333,333', '333333'))
    def test_clean_string_dirty(self, input, expected):
        """
        Validates that _clean returns the correct string,
        when the input is a string with some non digit characters.
        """
        self.assertEqual(ciuy._clean(input), expected)

    @params(11111111, 333333)
    def test_clean_string_raises_TypeError(self, input):
        """
        Validates that _clean raises TypeError,
        when the input is a number.
        """
        with self.assertRaises(TypeError):
            ciuy._clean(input)
