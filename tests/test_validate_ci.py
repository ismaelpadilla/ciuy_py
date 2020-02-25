import pytest
import ciuy


@pytest.mark.parametrize("input", ['11111111', '22222222', '33333333', '3333339', '4567890'])
def test_validate_ci_string_clean_true(input):
    """
    Validates that validate_ci returns True if the input is a valid ci,
    when the input is a string without any non digit characters.
    """
    assert ciuy.validate_ci(input)


@pytest.mark.parametrize("input", ['11111112', '22222223', '33333334', '3333330', '4567891'])
def test_validate_ci_string_clean_false(input):
    """
    Validates that validate_ci returns False if the input is not a valid ci,
    when the input is a string without any non digit characters.
    """
    assert not ciuy.validate_ci(input)


@pytest.mark.parametrize("input", ['1.111.111-1', '2.2.2.2.2.2.2.2', '3,333,333-3', '333-333.9', '456.789-0'])
def test_validate_ci_string_dirty_true(input):
    """
    Validates that validate_ci returns true if the input is a valid ci,
    when the input is a string with some non digit characters.
    """
    assert ciuy.validate_ci(input)


@pytest.mark.parametrize("input", ['1.111.111-2', '2.2.2.2.2.2.2.3', '3,333,333-4', '333-333.0', '456.789-1'])
def test_validate_ci_string_dirty_false(input):
    """
    Validates that validate_ci returns False if the input is not a valid ci,
    when the input is a string with some non digit characters.
    """
    assert not ciuy.validate_ci(input)


@pytest.mark.parametrize("input", [11111111, 22222222, 33333333, 3333339, 4567890])
def test_validate_ci_number_true(input):
    """
    Validates that validate_ci returns True if the input is a valid ci,
    when the input is a number.
    """
    assert ciuy.validate_ci(input)


@pytest.mark.parametrize("input", [11111112, 22222223, 33333334, 3333330, 4567891])
def test_validate_ci_number_false(input):
    """
    Validates that validate_ci returns False if the input is not a valid ci,
    when the input is a number with some non digit characters.
    """
    assert not ciuy.validate_ci(input)


@pytest.mark.parametrize("input", ['1', '100000', '100000000', '999999', '100000010', 100000, 100000000, 999999, 100000010])
def test_validate_ci_raises_ValueError(input):
    """
    Validates that validate_ci raises ValueError if the input is not within
    the valid range.
    """
    with pytest.raises(ValueError):
        ciuy.validate_ci(input)
