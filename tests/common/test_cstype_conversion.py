from datetime import datetime
from decimal import Decimal as PyDecimal
from numbers import Number

from stock_indicators._cslib import CsCultureInfo
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydatetime, to_pydecimal


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
        py_datetime = datetime.strptime(
            "2022-06-02 10:29:00-04:00", "%Y-%m-%d %H:%M:%S%z"
        )
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

        cs_double = CsDouble.Parse("1996.1012", CsCultureInfo.InvariantCulture)
        assert isinstance(cs_double, Number)
        assert isinstance(cs_double, float)
        assert 1996.1012 == cs_double

    def test_quote_constructor_retains_timezone(self):
        from decimal import Decimal

        from stock_indicators.indicators.common.quote import Quote

        dt = datetime.fromisoformat("2000-03-26T23:00:00+00:00")
        q = Quote(
            date=dt,
            open=Decimal("23"),
            high=Decimal("26"),
            low=Decimal("20"),
            close=Decimal("25"),
            volume=Decimal("323"),
        )

        assert str(q.date.tzinfo) == "UTC"
        assert str(q.date.time()) == "23:00:00"

    def test_decimal_conversion(self):
        py_decimal = 1996.1012
        cs_decimal = CsDecimal(py_decimal)

        assert str(py_decimal) == "1996.1012"
        assert to_pydecimal(cs_decimal) == PyDecimal(str(py_decimal))

    def test_decimal_conversion_expressed_in_exponential_notation(self):
        py_decimal = 0.000018
        cs_decimal = CsDecimal(py_decimal)

        assert str(py_decimal) == "1.8e-05"
        assert to_pydecimal(cs_decimal) == PyDecimal(str(py_decimal))

    def test_exponential_notation_decimal_conversion(self):
        py_decimal = 1.8e-05
        cs_decimal = CsDecimal(py_decimal)

        assert to_pydecimal(cs_decimal) == PyDecimal(str(py_decimal))

    def test_large_decimal_conversion(self):
        py_decimal = 12345678901234567890.123456789
        cs_decimal = CsDecimal(py_decimal)

        assert to_pydecimal(cs_decimal) == PyDecimal(str(py_decimal))
