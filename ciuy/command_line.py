import argparse
import ciuy


def cmd_validate_ci():
    parser = argparse.ArgumentParser(description='Validate Uruguayan identity document numbers.')
    parser.add_argument('ci', help='Document number to validate.')
    args = parser.parse_args()

    try:
        result = ciuy.validate_ci(args.ci)
    except ValueError as err:
        result = "Error: {0}".format(err)
    print(result, end="")


def cmd_validation_digit():
    parser = argparse.ArgumentParser(description='Validate Uruguayan identity document numbers.')
    parser.add_argument('ci', help='Document number for which you want to find the validation digit.')
    args = parser.parse_args()

    try:
        result = ciuy.validation_digit(args.ci)
    except ValueError as err:
        result = "Error: {0}".format(err)
    print(result, end="")


def cmd_random_ci():
    parser = argparse.ArgumentParser(description='Generate a random Uruguayan document number.')
    parser.parse_args()
    print(ciuy.random_ci(), end="")
