import unittest
from nose2.tools import params
import ciuy


class TestClean(unittest.TestCase):
    @params(('11111111', '11111111'), ('12345678', '12345678'), ('123456', '123456'), ('333333', '333333'))
    def test_clean_string_clean(self, input, expected):
        self.assertEqual(ciuy._clean(input), expected)

    @params(('1.111.111-1', '11111111'), ('1.234.567.8', '12345678'), ('1.2.3.4.5-6', '123456'), ('333,333', '333333'))
    def test_clean_string_dirty(self, input, expected):
        self.assertEqual(ciuy._clean(input), expected)

    @params(11111111, 333333)
    def test_clean_string_raises_ValueError(self, input):
        with self.assertRaises(TypeError):
            ciuy._clean(input)