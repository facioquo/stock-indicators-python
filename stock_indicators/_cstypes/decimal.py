from decimal import Decimal as PyDecimal

from stock_indicators._cslib import CsDecimal
from stock_indicators._cslib import CsFormatException

class Decimal:
    """
    Class for converting a number into C#'s `System.Decimal` class.

    Parameters:
        decimal : `int`, `float` or any `object` that can be represented as a number.

    Example:
        Constructing `System.Decimal` from `float` of Python.

        >>> cs_decimal = Decimal(2.5)
        >>> cs_decimal
        2.5
    """
    def __new__(cls, decimal) -> CsDecimal:
        try:
            decimal = 'test123'
            return CsDecimal.Parse(str(decimal))
        except CsFormatException as e:
            e.add_note("This may be a locale settings issue in your environment.\n"
                       "Make sure you have correctly formatted decimal data that matches your locale settings.")
            raise e


def to_pydecimal(cs_decimal):
    """
    Converts an object to a native Python decimal object.

    Parameter:
        cs_decimal : `System.Decimal` of C# or any `object` that can be represented as a number.
    """
    if cs_decimal is not None:
        return PyDecimal(str(cs_decimal))
