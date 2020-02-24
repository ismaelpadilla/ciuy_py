import pytest
import ciuy


@pytest.mark.parametrize("input, expected", [('1111111', '1'), ('2222222', '2'), ('3333333', '3'), ('333333', '9'),
                                             ('456789', '0')])
def test_validation_digit_string_clean(input, expected):
    """
    Validates that validation_digit returns the correct digit,
    when the input is a string without any non digit characters.
    """
    assert ciuy.validation_digit(input) == expected


@pytest.mark.parametrize("input, expected", [('1.111.111', '1'), ('2.2.2.2.2.2.2', '2'), ('3,333,333', '3'),
                                             ('333-333', '9'), ('456.789', '0')])
def test_validation_digit_string_dirty(input, expected):
    """
    Validates that validation_digit returns the correct digit,
    when the input is a string with some non digit characters.
    """
    assert ciuy.validation_digit(input) == expected


@pytest.mark.parametrize("input, expected", [(1111111, '1'), (2222222, '2'), (3333333, '3'), (333333, '9'),
                                             (456789, '0')])
def test_validation_digit_number(input, expected):
    """
    Validates that validation_digit returns the correct digit,
    when the input is a number.
    """
    assert ciuy.validation_digit(input) == expected


@pytest.mark.parametrize("input", ['10000', '10000000', '99999', '10000001', 10000, 10000000, 99999, 10000001])
def test_validation_digit_raises_ValueError(input):
    """
    Validates that validation_digit raises ValueError if the input is not within
    the valid range.
    """
    with pytest.raises(ValueError):
        ciuy.validation_digit(input)
