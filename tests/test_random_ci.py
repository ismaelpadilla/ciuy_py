"""
A word of caution:
Due to the nature of the random() method, no unit test can guarantee that it's function correctly.
The tests in this class should be considered nothing more than smoke tests.
"""

import ciuy


def test_random_ci_length():
    random_ci = ciuy.random_ci()
    length_valid = len(random_ci) >= 7 and len(random_ci) <= 8
    assert length_valid


def test_random_ci_valid():
    """
    Test that random produces a valid ci
    Note that this tests is dependant on validate_ci working correctly.
    """
    random_ci = ciuy.random_ci()
    assert ciuy.validate_ci(random_ci)
