import argparse
import ciuy


def cmd_validate_ci():
    parser = argparse.ArgumentParser(prog='ciuy',
                                     description='Validate Uruguayan identity document numbers.')
    parser.add_argument('ci', help='Document number to validate.')
    args = parser.parse_args()

    try:
        result = ciuy.validate_ci(args.ci)
    except ValueError as err:
        result = "Error: {0}".format(err)
    print(result, end="")
