from datetime import datetime as PyDateTime
from typing import Optional

from stock_indicators._cslib import CsDateTime
from stock_indicators._cslib import CsCultureInfo


class DateTime:
    """
    Class for constructing C#'s `System.DateTime` object from Python's `datetime.datetime` instance.

    Parameters:
        datetime : `datetime.datetime`.

    Example:
        Constructing `System.DateTime` from `datetime.datetime` of Python.

        >>> now = datetime.now()
        >>> cs_now = DateTime(now)
        >>> cs_now
        3/26/2021 10:02:22 PM
    """
    def __new__(cls, datetime: PyDateTime) -> CsDateTime:
        if not isinstance(datetime, PyDateTime):
            raise TypeError("Expected datetime.datetime instance")

        # Use direct constructor instead of string parsing for better performance
        try:
            return CsDateTime(
                datetime.year,
                datetime.month,
                datetime.day,
                datetime.hour,
                datetime.minute,
                datetime.second,
                datetime.microsecond // 1000  # Convert microseconds to milliseconds
            )
        except Exception as e:
            # Fallback to string parsing if direct construction fails
            try:
                return CsDateTime.Parse(datetime.isoformat())
            except Exception:
                from stock_indicators.exceptions import TypeConversionError
                raise TypeConversionError(f"Cannot convert datetime {datetime} to C# DateTime: {e}") from e


def to_pydatetime(cs_datetime: Optional[CsDateTime]) -> Optional[PyDateTime]:
    """
    Converts C#'s `System.DateTime` struct to a native Python datetime object.

    Parameter:
        cs_datetime : `System.DateTime` of C# or None.

    Returns:
        Python datetime object or None if input is None.
    """
    if cs_datetime is None:
        return None

    try:
        # Use direct property access for better performance
        return PyDateTime(
            cs_datetime.Year,
            cs_datetime.Month,
            cs_datetime.Day,
            cs_datetime.Hour,
            cs_datetime.Minute,
            cs_datetime.Second,
            cs_datetime.Millisecond * 1000  # Convert milliseconds to microseconds
        )
    except Exception as e:
        # Fallback to string conversion if direct access fails
        try:
            return PyDateTime.fromisoformat(cs_datetime.ToString("s", CsCultureInfo.InvariantCulture))
        except Exception:
            from stock_indicators.exceptions import TypeConversionError
            raise TypeConversionError(f"Cannot convert C# DateTime to Python datetime: {e}") from e
