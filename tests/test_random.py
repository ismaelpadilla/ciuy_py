import unittest
import ciuy


class TestClean(unittest.TestCase):
    """
    A word of caution:
    Due to the nature of the random() method, no unit test can guarantee that it's function correctly.
    The tests in this class should be considered nothing more than smoke tests.
    """

    def test_random_length(self):
        random_ci = ciuy.random()
        length_valid = len(random_ci) >= 7 and len(random_ci) <= 8
        self.assertTrue(length_valid)

    def test_random_valid(self):
        """
        Test that random produces a valid ci
        Note that this tests is dependant on validate_ci working correctly.
        """
        random_ci = ciuy.random()
        self.assertTrue(ciuy.validate_ci(random_ci))
