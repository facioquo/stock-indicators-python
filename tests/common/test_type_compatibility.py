
from enum import Enum, IntEnum
from stock_indicators._cslib import CsQuote, CsCandleProperties
from stock_indicators.indicators.common.candles import CandleProperties
from stock_indicators.indicators.common.enums import PivotPointType
from stock_indicators.indicators.common.quote import Quote

class TestTypeCompat:
    def test_quote_based_class(self):
        # Quote
        assert issubclass(Quote, CsQuote)
        
        # CandleProperties
        assert issubclass(CandleProperties, Quote)
        assert issubclass(CandleProperties, CsQuote)
        assert issubclass(CandleProperties, CsCandleProperties)

    def test_cs_compatible_enum(self):
        assert isinstance(PivotPointType.STANDARD, Enum)
        assert isinstance(PivotPointType.STANDARD, IntEnum)
        assert isinstance(PivotPointType.STANDARD.value, int)

        assert int(PivotPointType.STANDARD) == 0
        assert PivotPointType.STANDARD == 0
        assert PivotPointType.STANDARD == PivotPointType.STANDARD
