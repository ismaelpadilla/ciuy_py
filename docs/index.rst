.. ciuy documentation master file, created by
   sphinx-quickstart on Tue Feb 18 20:53:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ciuy
================================


.. .. toctree::
..    :hidden:

   



Package for validating Uruguayan identity document numbers. 

The functions in this package work with strings and ignore any non-digit characters. Numbers are valid too. So for example, the following expressions represent the same document number::

   '1.234.567-2'
   '12345672'
   12345672

Installation
------------

``ciuy`` can be installed with :any:`pip<pip:index>`:

.. code-block::

   pip install ciuy


Usage
-----

>>> import ciuy
>>> ciuy.validate_ci("1.234.567-2")
True
>>> ciuy.validation_digit("1.234.567")
'2'
>>> ciuy.random()
'82405816'

See :doc:`/functions` for more detailed documentation of each function.

Testing
-------

This package includes some doctests, as well as unit tests that can be run with :any:`pytest<pytest:index>`.

After cloning the repository, you can run the doctests with:

::

   $ python3 -m doctest ./ciuy/__init__.py -v
   (several lines ommited)
   11 passed and 0 failed.
   Test passed.

Use :any:`pytest<pytest:index>` to run the unit tests:

::

   $ py.test
   ============================= test session starts ==============================
   platform linux -- Python 3.8.1, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
   rootdir: /home/ciuy
   collected 98 items                                                             

   tests\test_clean.py ..........                                           [ 10%]
   tests\test_command_line.py ........................                      [ 34%]
   tests\test_random_ci.py ..                                               [ 36%]
   tests\test_validate_ci.py .......................................        [ 76%]
   tests\test_validation_digit.py .......................                   [100%]

   ============================== 98 passed in 1.09s =============================

You can also use :any:`pytest<pytest:index>` to run all tests, including doctests, with:

::

   $ py.test --doctest-modules

Command line
------------

After installation, the following commands become available:

::

   $ validate_ci 1.234.567-2
   True
   $ validation_digit 1.234.567
   2
   $ random_ci
   82405816


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Home <self>
   functions
   about

.. toctree::
   :hidden:
   :caption: Useful links:

   ciuy @ PyPI <https://pypi.org/project/ciuy/>
   ciuy @ GitHub <https://github.com/ismaelpadilla/ciuy_py/>

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
