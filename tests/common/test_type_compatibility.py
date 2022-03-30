
from stock_indicators._cslib import CsQuote, CsCandleProperties
from stock_indicators.indicators.common.candles import CandleProperties
from stock_indicators.indicators.common.quote import Quote

class TestTypeCompat:
    def test_quote_based_class(self):
        # Quote
        assert issubclass(Quote, CsQuote)
        
        # CandleProperties
        assert issubclass(CandleProperties, Quote)
        assert issubclass(CandleProperties, CsQuote)
        assert issubclass(CandleProperties, CsCandleProperties)