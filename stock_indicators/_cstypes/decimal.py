from decimal import Decimal as PyDecimal

from stock_indicators._cslib import CsDecimal, CsCultureInfo, CsNumberStyles


class Decimal:
    """
    Class for converting a number into C#'s `System.Decimal` class.

    Parameters:
        decimal : `int`, `float` or any `object` that can be represented as a number string.

    Example:
        Constructing `System.Decimal` from `float` of Python.

        >>> cs_decimal = Decimal(2.5)
        >>> cs_decimal
        2.5
    """
    cs_number_styles = CsNumberStyles.AllowDecimalPoint | CsNumberStyles.AllowExponent \
        | CsNumberStyles.AllowLeadingSign | CsNumberStyles.AllowThousands

    def __new__(cls, decimal) -> CsDecimal:
        return CsDecimal.Parse(str(decimal), cls.cs_number_styles, CsCultureInfo.InvariantCulture)


def to_pydecimal(cs_decimal: CsDecimal) -> PyDecimal:
    """
    Converts an object to a native Python decimal object.

    Parameter:
        cs_decimal : `System.Decimal` of C# or any `object` that can be represented as a number.
    """
    if cs_decimal is not None:
        return PyDecimal(cs_decimal.ToString(CsCultureInfo.InvariantCulture))
