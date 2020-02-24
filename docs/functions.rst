Functions and examples
======================

.. py:function:: ciuy.validate_ci(ci)

   Validates the document number passed as a paremeter.

   :param str ci: The document number to validate. Any non-digit characters are ignored. A number can be passed as a parameter as well.
   :return: ``True`` if the document number is valid, ``False`` otherwise.
   :rtype: bool
   :raises ValueError: if ``ci``\ , without including the validation digit, is lower than 100.000 or higher than 9.999.999.

>>> ciuy.validate_ci(1.234.567-2)
True

.. py:function:: ciuy.validation_digit(ci)

   Returns the validation digit for a given document number.

   :param str ci: The document number for which one wants to find the validation digit. Any non-digit characters are ignored. A number can be passed as a parameter as well.
   :return: The validation digit.
   :rtype: bool
   :raises ValueError: if ``ci``\ is lower than 100.000 or higher than 9.999.999.

>>> ciuy.validation_digit(1.234.567)
'2'

.. py:function:: ciuy.random()

   Returns a random document number, including validation digit. The document number is in the (100.000, 9.999.999) range.

   :return: A random valid document number.
   :rtype: str

>>> ciuy.random()
'82405816'
