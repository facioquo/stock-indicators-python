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
        if not isinstance(datetime, PyDateTime):
            raise TypeError("Expected datetime.datetime instance")
            
        # Preserve timezone: normalize tz-aware datetimes to UTC and set Kind=Utc
        if datetime.tzinfo is not None and datetime.utcoffset() is not None:
            dt_utc = datetime.astimezone(PyTimezone.utc).replace(tzinfo=None)
            cs_dt = CsDateTime.Parse(dt_utc.isoformat())
            # Import DateTimeKind dynamically to avoid import issues
            from System import DateTimeKind
            return CsDateTime.SpecifyKind(cs_dt, DateTimeKind.Utc)
        # Naive: preserve full precision
        return CsDateTime.Parse(datetime.isoformat())


def to_pydatetime(cs_datetime: CsDateTime) -> PyDateTime:
    """
    Converts C#'s `System.DateTime` struct to a native Python datetime object.

    Parameter:
        cs_datetime : `System.DateTime` of C#.
    """
    # Check the Kind to determine if this should have timezone info
    kind = cs_datetime.Kind
    
    if str(kind) == 'Utc':
        # UTC DateTime - return with UTC timezone
        try:
            iso = cs_datetime.ToString("yyyy-MM-dd'T'HH:mm:ss.ffffff", CsCultureInfo.InvariantCulture)
            dt = PyDateTime.fromisoformat(iso)
            return dt.replace(tzinfo=PyTimezone.utc)
        except ValueError:
            iso_fallback = cs_datetime.ToString("yyyy-MM-dd'T'HH:mm:ss", CsCultureInfo.InvariantCulture)
            dt = PyDateTime.fromisoformat(iso_fallback)
            return dt.replace(tzinfo=PyTimezone.utc)
    else:
        # Unspecified or Local - return without timezone info
        try:
            iso = cs_datetime.ToString("yyyy-MM-dd'T'HH:mm:ss.ffffff", CsCultureInfo.InvariantCulture)
            return PyDateTime.fromisoformat(iso)
        except ValueError:
            iso_fallback = cs_datetime.ToString("yyyy-MM-dd'T'HH:mm:ss", CsCultureInfo.InvariantCulture)
            return PyDateTime.fromisoformat(iso_fallback)
