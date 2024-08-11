from decimal import Decimal as PyDecimal

from stock_indicators._cslib import CsDecimal
from stock_indicators._cslib import CsFormatException
from stock_indicators._cslib import CsCultureInfo

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
            return CsDecimal.Parse(str(decimal), CsCultureInfo.InvariantCulture)
        except CsFormatException as e:
            raise ValueError("You may be using numeric data that is incompatible with your locale environment settings.\n"
                             "For example, you may be using decimal points instead of commas.") from e


def to_pydecimal(cs_decimal):
    """
    Converts an object to a native Python decimal object.

    Parameter:
        cs_decimal : `System.Decimal` of C# or any `object` that can be represented as a number.
    """
    if cs_decimal is not None:
        return PyDecimal(cs_decimal.ToString(CsCultureInfo.InvariantCulture))
