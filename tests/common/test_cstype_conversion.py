from datetime import datetime
from numbers import Number

from stock_indicators._cslib import CsCultureInfo
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators._cstypes import to_pydatetime

class TestCsTypeConversion:
    def test_datetime_conversion(self):
        py_datetime = datetime.now()
        converted_datetime = to_pydatetime(CsDateTime(py_datetime))

        assert py_datetime.year == converted_datetime.year
        assert py_datetime.month == converted_datetime.month
        assert py_datetime.day == converted_datetime.day
        assert py_datetime.hour == converted_datetime.hour
        assert py_datetime.minute == converted_datetime.minute
        assert py_datetime.second == converted_datetime.second
        # Ignore microsecond.
        # assert py_datetime.microsecond == converted_datetime.microsecond

    def test_timezone_aware_datetime_conversion(self):
        py_datetime = datetime.strptime('2022-06-02 10:29:00-04:00', '%Y-%m-%d %H:%M:%S%z')
        converted_datetime = to_pydatetime(CsDateTime(py_datetime))

        assert py_datetime.year == converted_datetime.year
        assert py_datetime.month == converted_datetime.month
        assert py_datetime.day == converted_datetime.day
        # hour, minute can be different.
        # assert py_datetime.hour == converted_datetime.hour
        # assert py_datetime.minute == converted_datetime.minute
        assert py_datetime.second == converted_datetime.second
        # Ignore microsecond.
        # assert py_datetime.microsecond == converted_datetime.microsecond

    def test_auto_conversion_from_double_to_float(self):
        from System import Double as CsDouble

        cs_double = CsDouble.Parse('1996.1012', CsCultureInfo.InvariantCulture)
        assert isinstance(cs_double, Number)
        assert isinstance(cs_double, float)
        assert 1996.1012 == cs_double
