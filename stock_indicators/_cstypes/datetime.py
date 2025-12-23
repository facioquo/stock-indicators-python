from datetime import datetime as PyDateTime
from datetime import timezone as PyTimezone

from System import DateTimeKind  # type: ignore

from stock_indicators._cslib import CsDateTime  # type: ignore

# Module-level constant: 1 second = 10,000,000 ticks (100ns per tick)
_TICKS_PER_SECOND = 10_000_000


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
        """Fast conversion from Python datetime to System.DateTime without string parsing.

        - If tz-aware, normalize to UTC and create DateTime with Kind=Utc
        - If naive, create DateTime with Kind=Unspecified
        - Preserve milliseconds, and add remaining microseconds via AddTicks
        """
        if not isinstance(datetime, PyDateTime):
            raise TypeError("Expected datetime.datetime instance")

        # Normalize timezone
        is_tz_aware = datetime.tzinfo is not None and datetime.utcoffset() is not None
        dt = datetime.astimezone(PyTimezone.utc) if is_tz_aware else datetime

        # Prepare components
        year, month, day = dt.year, dt.month, dt.day
        hour, minute, second = dt.hour, dt.minute, dt.second
        ms, extra_micro = divmod(dt.microsecond, 1000)

        kind = DateTimeKind.Utc if is_tz_aware else DateTimeKind.Unspecified
        # Construct with millisecond precision
        cs_dt = CsDateTime(year, month, day, hour, minute, second, ms, kind)
        # Add remaining microseconds as ticks (1 tick = 100 ns => 1 microsecond = 10 ticks)
        if extra_micro:
            cs_dt = cs_dt.AddTicks(extra_micro * 10)
        return cs_dt


def to_pydatetime(cs_datetime: CsDateTime) -> PyDateTime:
    """Fast conversion from System.DateTime to Python datetime without string formatting.

    Preserves microseconds using DateTime.Ticks and attaches timezone if Kind is Utc.
    """
    # Extract components directly
    year = cs_datetime.Year
    month = cs_datetime.Month
    day = cs_datetime.Day
    hour = cs_datetime.Hour
    minute = cs_datetime.Minute
    second = cs_datetime.Second

    # Microseconds within the second from ticks (1 tick = 100 ns)
    microsecond = int((cs_datetime.Ticks % _TICKS_PER_SECOND) // 10)

    # Attach tzinfo only for UTC
    if cs_datetime.Kind == DateTimeKind.Utc:
        return PyDateTime(
            year, month, day, hour, minute, second, microsecond, tzinfo=PyTimezone.utc
        )
    return PyDateTime(year, month, day, hour, minute, second, microsecond)
