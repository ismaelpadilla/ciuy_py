"""
pytest-mock is required to run these tests
"""

from ciuy import command_line
import pytest


@pytest.mark.parametrize("input", ['11111111', '22222222', '33333333', '3333339', '4567890'])
def test_cmd_validate_ci_true(input, mocker, capfd):
    fake_args = ['', input]
    mocker.patch('sys.argv', fake_args)

    command_line.cmd_validate_ci()
    out, _ = capfd.readouterr()
    assert 'True' in out


@pytest.mark.parametrize("input", ['11111112', '22222223', '33333334', '3333330', '4567891'])
def test_cmd_validate_ci_false(input, mocker, capfd):
    fake_args = ['', input]
    mocker.patch('sys.argv', fake_args)

    command_line.cmd_validate_ci()
    out, _ = capfd.readouterr()
    assert 'False' in out


@pytest.mark.parametrize("input", ['100000', '100000000', '999999', '100000010'])
def test_cmd_validate_ci_err(input, mocker, capfd):
    fake_args = ['', input]
    mocker.patch('sys.argv', fake_args)

    command_line.cmd_validate_ci()
    out, _ = capfd.readouterr()
    assert 'Error' in out


@pytest.mark.parametrize("input, expected", [('1111111', '1'), ('2222222', '2'), ('3333333', '3'), ('333333', '9'),
                                             ('456789', '0')])
def test_cmd_validation_digit_ok(input, expected, mocker, capfd):
    fake_args = ['', input]
    mocker.patch('sys.argv', fake_args)

    command_line.cmd_validation_digit()
    out, _ = capfd.readouterr()
    assert expected in out


@pytest.mark.parametrize("input", ['10000', '10000000', '99999', '10000001'])
def test_cmd_validation_digit_err(input, mocker, capfd):
    fake_args = ['', input]
    mocker.patch('sys.argv', fake_args)

    command_line.cmd_validation_digit()
    out, _ = capfd.readouterr()
    assert 'Error' in out


def test_cmd_random_ci(mocker, capfd):
    """
    Validate that the output can be converted to an int
    This should be considered a smoke test only
    """
    fake_args = ['']
    mocker.patch('sys.argv', fake_args)
    command_line.cmd_random_ci()
    out, _ = capfd.readouterr()
    int(out)
