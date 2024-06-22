from decimal import Decimal as PyDecimal

from stock_indicators._cslib import CsDecimal
from stock_indicators._cstypes import Decimal as CsDecimalConverter
from stock_indicators._cstypes.decimal import to_pydecimal

class TestLocale:
    '''
    These tests are for the environment with locale which uses comma as a decimal separator.
    Suppose that current system locale is ru_RU.UTF-8
    '''
    
    def test_conversion_to_Python_decimal_with_comma_decimal_separator(self):
        cs_decimal = CsDecimal.Parse('12345,6789')
        assert '12345,6789' == str(cs_decimal)
        assert PyDecimal('12345.6789') == to_pydecimal(cs_decimal)

    def test_conversion_to_CSharp_decimal_with_comma_decimal_separator(self):
        # Applied CultureInfo.InvariantCulture, comma as a decimal separator should be ignored. 
        cs_decimal = CsDecimalConverter('12345,6789.123456789')
        assert '123456789,123456789' == str(cs_decimal)
        assert PyDecimal('123456789.123456789') == to_pydecimal(cs_decimal)

    def test_re_conversion_to_CSharp_decimal_with_comma_decimal_separator(self):
        # result value will be distorted
        # if CsDecimal is converted into CsDecimal again, since comma as a decimal separator would be ignored.
        # Note: did not add validation logic to avoid performance loss.
        cs_decimal = CsDecimalConverter('12345,6789.123456789')
        assert '123456789,123456789' == str(cs_decimal)
        
        cs_decimal = CsDecimalConverter(cs_decimal)        
        assert '123456789123456789' == str(cs_decimal)
        
        