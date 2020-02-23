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

See :doc:`/functions` for more detailed documentation of each functions.

Testing
-------

This package includes some doctests, as well as unit tests that can be run with :any:`nose2<nose2:index>`.

After cloning the repository, you can run the doctests with:

.. code-block::

   $ python3 -m doctest ./ciuy/__init__.py -v
   (several lines ommited)
   11 passed and 0 failed.
   Test passed.

Use :any:`nose2<nose2:index>` to run the unit tests:

.. code-block::

   $ python3 -m nose2
   .........................................................................
   ----------------------------------------------------------------------
   Ran 73 tests in 0.008s

   OK


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Home <self>
   functions
   about

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
