import locale
from decimal import Decimal as PyDecimal

import pytest

from stock_indicators._cslib import CsDecimal
from stock_indicators._cstypes import Decimal as CsDecimalConverter
from stock_indicators._cstypes.decimal import to_pydecimal


def _uses_comma_decimal_separator() -> bool:
    """Return True if the environment's decimal separator is a comma.

    Prefers .NET CultureInfo when pythonnet is available; otherwise, falls back to
    Python's locale settings.
    """
    # First try .NET CurrentCulture
    try:
        # Importing clr is optional but helps ensure pythonnet is initialized
        import clr  # type: ignore  # noqa: F401
        from System.Globalization import CultureInfo  # type: ignore

        return CultureInfo.CurrentCulture.NumberFormat.NumberDecimalSeparator == ","
    except Exception:
        pass

    # Fallback: Python locale
    try:
        # Ensure locale is set to the user default; ignore failures
        try:
            locale.setlocale(locale.LC_ALL, "")
        except Exception:
            pass
        return locale.localeconv().get("decimal_point", ".") == ","
    except Exception:
        return False


uses_comma_decimal = _uses_comma_decimal_separator()


@pytest.mark.localization
@pytest.mark.skipif(
    not uses_comma_decimal,
    reason="Localization tests require a comma decimal separator culture (e.g., ru-RU)",
)
class TestLocale:
    """
    These tests are intended for environments where a comma is used as the decimal separator,
    such as when the current system locale is ru_RU.UTF-8.
    """

    def test_conversion_to_Python_decimal_with_comma_decimal_separator(self):
        cs_decimal = CsDecimal.Parse("1996,1012")
        assert "1996,1012" == str(cs_decimal)
        assert PyDecimal("1996.1012") == to_pydecimal(cs_decimal)

    def test_conversion_to_CSharp_decimal_with_comma_decimal_separator(self):
        # Applied CultureInfo.InvariantCulture, comma as a decimal separator should be ignored.
        cs_decimal = CsDecimalConverter("1996,10.12")
        assert "199610,12" == str(cs_decimal)
        assert PyDecimal("199610.12") == to_pydecimal(cs_decimal)

    def test_re_conversion_to_CSharp_decimal_with_comma_decimal_separator(self):
        # result value will be distorted
        # if CsDecimal is converted into CsDecimal again, since comma as a decimal separator would be ignored.
        # Note: did not add defensive logic to avoid performance loss.
        cs_decimal = CsDecimalConverter("1996,10.12")
        assert "199610,12" == str(cs_decimal)

        cs_decimal = CsDecimalConverter(cs_decimal)
        assert "19961012" == str(cs_decimal)

    def test_conversion_to_double_with_comma_decimal_separator(self):
        from System import Double as CsDouble  # type: ignore

        cs_double = CsDouble.Parse("1996,1012")
        assert 1996.1012 == cs_double  # should be period-separated float.
