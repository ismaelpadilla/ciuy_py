'''
Package for validating Uruguayan identity document numbers.
The functions in this package work with strings and ignore any non-digit characters. Numbers are valid too.
'''

import re
from random import uniform


def validation_digit(ci):
    """
    Given a ci (without validation digit), returns it's validation digit as a string.
    The input string may have periods, dashes, or other characters (any non-digit characters are ignored).
    The input must be a number between 100.000 and 9.999.999, will raise ValueError otherwise.

    >>> validation_digit('1.111.111')
    '1'
    >>> validation_digit(1111111)
    '1'
    >>> validation_digit('333333')
    '9'
    >>> validation_digit('456.789')
    '0'
    """
    clean_ci = _clean(str(ci))

    # raise exception if ci is too low or too high
    if (int(clean_ci) < 100000 or int(clean_ci) > 9999999):
        raise ValueError("ci must be higher than 100.000 and lower than 9.999.999")

    digit_list = [int(i) for i in clean_ci]

    control = [8, 1, 2, 3, 4, 7, 6]

    digit_list.reverse()
    control.reverse()
    dot_product = sum(map(lambda x, y: x*y, digit_list, control))
    return str(dot_product % 10)


def validate_ci(ci):
    """
    Returns True if ci (including validation digit) is valid, returns False otherwise.
    The input string may have periods, dashes, or other characters (any non-digit characters are ignored).
    The input (not including validation digit) must be a number between 100.000 and 9.999.999,
    will raise ValueError otherwise.

    >>> validate_ci(11111111)
    True
    >>> validate_ci(11111112)
    False
    >>> validate_ci('1.234.567-2')
    True
    >>> validate_ci('1.234.567-1')
    False
    >>> validate_ci('456.789-0')
    True
    """
    clean_ci = _clean(str(ci))

    # raise exception if ci is too low or too high
    if (int(clean_ci) < 1000000 or int(clean_ci) > 99999999):
        raise ValueError("ci must be higher than 100.000 and lower than 9.999.999")

    return clean_ci[-1] == validation_digit(clean_ci[:-1])


def random_ci():
    """
    Returns a random ci in the 100.000-9.000.000 range, including the validation digit.
    The returned string does not contain any periods or dashes.
    """
    random_number = str(round(uniform(100000, 9999999)))
    v_digit = validation_digit(random_number)
    return random_number + v_digit


def _clean(ci):
    """
    Removes any non-digit character from the input string.
    Will raise TypeError if input isn't a string.

        >>> _clean('1.111.111')
        '1111111'
        >>> _clean('1.2.3.4.5.6.7-8')
        '12345678'
    """
    return re.sub("[^0-9]", "", ci)
