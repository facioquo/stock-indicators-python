from decimal import Decimal as PyDecimal

import pytest

from stock_indicators._cslib import CsDecimal
from stock_indicators._cstypes import Decimal as CsDecimalConverter
from stock_indicators._cstypes.decimal import to_pydecimal

@pytest.mark.locale_specific
class TestLocale:
    '''
    These tests are intended for environments where a comma is used as the decimal separator,
    such as when the current system locale is ru_RU.UTF-8.
    '''
    def test_conversion_to_Python_decimal_with_comma_decimal_separator(self):
        cs_decimal = CsDecimal.Parse('1996,1012')
        assert '1996,1012' == str(cs_decimal)
        assert PyDecimal('1996.1012') == to_pydecimal(cs_decimal)

    def test_conversion_to_CSharp_decimal_with_comma_decimal_separator(self):
        # Applied CultureInfo.InvariantCulture, comma as a decimal separator should be ignored. 
        cs_decimal = CsDecimalConverter('1996,10.12')
        assert '199610,12' == str(cs_decimal)
        assert PyDecimal('199610.12') == to_pydecimal(cs_decimal)

    def test_re_conversion_to_CSharp_decimal_with_comma_decimal_separator(self):
        # result value will be distorted
        # if CsDecimal is converted into CsDecimal again, since comma as a decimal separator would be ignored.
        # Note: did not add validation logic to avoid performance loss.
        cs_decimal = CsDecimalConverter('1996,10.12')
        assert '199610,12' == str(cs_decimal)
        
        cs_decimal = CsDecimalConverter(cs_decimal)        
        assert '19961012' == str(cs_decimal)
        
    def test_conversion_to_double_with_comma_decimal_separator(self):
        from System import Double as CsDouble

        cs_double = CsDouble.Parse('1996,1012')
        assert 1996.1012 == cs_double # should be period-separated float.
