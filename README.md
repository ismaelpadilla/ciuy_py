# ciuy

![PyPI](https://img.shields.io/pypi/v/ciuy)
![PyPI - Status](https://img.shields.io/pypi/status/ciuy)
[![Build Status](https://travis-ci.com/ismaelpadilla/ciuy_py.svg?branch=master)](https://travis-ci.com/ismaelpadilla/ciuy_py)
[![Coverage Status](https://coveralls.io/repos/github/ismaelpadilla/ciuy_py/badge.svg?branch=master)](https://coveralls.io/github/ismaelpadilla/ciuy_py?branch=master)
[![Documentation Status](https://readthedocs.org/projects/ciuy/badge/?version=latest)](https://ciuy.readthedocs.io/en/latest/?badge=latest)
![PyPI - License](https://img.shields.io/pypi/l/ciuy)

🇺🇾 🇪🇸 Documentación en español disponible [aquí](https://ciuy.readthedocs.io/es/latest/) / Spanish documentation is available [here](https://ciuy.readthedocs.io/es/latest/).

----

Package for validating Uruguayan identity document numbers. Full documentation is available [here](https://ciuy.readthedocs.io/es/latest/).

The functions in this package work with strings and ignore any non-digit characters. Numbers are valid too. So for example, the following expressions represent the same document number:

```
'1.234.567-2'
'12345672'
12345672
```

This package includes the following functions:

`validate_ci(ci: str) -> bool`: Returns true if `ci` is a valid document number, returns false otherwise. `ci` is a string which represents a document number, including the validation digit. `ci` can be a number as well.

`validation_digit(ci: str) -> str`: Returns the validation digit for `ci`.

`random() -> str`: Returns a random document number (including validation digit) in the (100.000, 9.999.999) range.

# Installation

```
$ pip install ciuy
```

# Usage

```
>>> import ciuy
>>> ciuy.validate_ci("1.234.567-2")
True
>>> ciuy.validation_digit("1.234.567")
'2'
>>> ciuy.random()
'82405816'
```

# Testing

This package includes some doctests, as well as unit tests that can be run with `nose2`.

After cloning the repository, you can run the doctests with:

```
$ python3 -m doctest ./ciuy/__init__.py -v
 (several lines ommited)
11 passed and 0 failed.
Test passed.
```

Use `nose2` to run the unit tests:
```
$ python3 -m nose2
.........................................................................
----------------------------------------------------------------------
Ran 73 tests in 0.008s

OK
```

# Todo

- Add command line scripts.

---

Based on the ci_uy Ruby gem by Fernando Briano ([link](https://github.com/picandocodigo/ci_uy)).
