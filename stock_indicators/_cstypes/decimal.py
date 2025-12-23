from decimal import Decimal as PyDecimal
from typing import Optional, Union

from stock_indicators._cslib import CsCultureInfo, CsDecimal, CsNumberStyles


class Decimal:
    """
    Class for converting a number into C#'s `System.Decimal` class.

    Parameters:
        decimal : `int`, `float`, `PyDecimal`, or any `object` that can be represented as a number string.

    Example:
        Constructing `System.Decimal` from `float` of Python.

        >>> cs_decimal = Decimal(2.5)
        >>> cs_decimal
        2.5
    """

    cs_number_styles = (
        CsNumberStyles.AllowDecimalPoint
        | CsNumberStyles.AllowExponent
        | CsNumberStyles.AllowLeadingSign
        | CsNumberStyles.AllowThousands
    )

    def __new__(cls, decimal: Union[int, float, PyDecimal, str, None]) -> CsDecimal:
        if decimal is None:
            from stock_indicators.exceptions import ValidationError

            raise ValidationError("Cannot convert None to C# Decimal")

        # Convert to string first to preserve precision for all numeric types
        try:
            return CsDecimal.Parse(
                str(decimal), cls.cs_number_styles, CsCultureInfo.InvariantCulture
            )
        except Exception as e:
            from stock_indicators.exceptions import TypeConversionError

            raise TypeConversionError(
                f"Cannot convert {decimal} (type: {type(decimal)}) to C# Decimal: {e}"
            ) from e


def to_pydecimal(cs_decimal: Optional[CsDecimal]) -> Optional[PyDecimal]:
    """
    Converts an object to a native Python decimal object.

    Parameter:
        cs_decimal : `System.Decimal` of C# or None.

    Returns:
        Python Decimal object or None if input is None.
    """
    if cs_decimal is None:
        return None

    try:
        return PyDecimal(cs_decimal.ToString(CsCultureInfo.InvariantCulture))
    except Exception as e:
        from stock_indicators.exceptions import TypeConversionError

        raise TypeConversionError(
            f"Cannot convert C# Decimal to Python Decimal: {e}"
        ) from e
