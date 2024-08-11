from datetime import datetime as PyDateTime

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
    def __new__(cls, datetime) -> CsDateTime:
        if isinstance(datetime, PyDateTime):
            return CsDateTime.Parse(datetime.isoformat())


def to_pydatetime(cs_datetime):
    """
    Converts C#'s `System.DateTime` struct to a native Python datetime object.

    Parameter:
        cs_datetime : `System.DateTime` of C#.
    """
    if isinstance(cs_datetime, CsDateTime):
        return PyDateTime.fromisoformat(cs_datetime.ToString("s", CsCultureInfo.InvariantCulture))
