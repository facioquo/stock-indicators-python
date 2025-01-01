from datetime import datetime as PyDateTime, timezone as PyTimezone

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
        return CsDateTime.Parse(datetime.isoformat(timespec='seconds'))


def to_pydatetime(cs_datetime: CsDateTime) -> PyDateTime:
    """
    Converts C#'s `System.DateTime` struct to a native Python datetime object.

    Parameter:
        cs_datetime : `System.DateTime` of C#.
    """
    py_datetime = PyDateTime.fromisoformat(cs_datetime.ToString("o", CsCultureInfo.InvariantCulture))
    if cs_datetime.Kind == 1:  # 1 indicates UTC
        py_datetime = py_datetime.replace(tzinfo=PyTimezone.utc)
    return py_datetime
