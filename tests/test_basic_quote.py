from datetime import datetime

from stock_indicators import indicators
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.quote import Quote

class TestBasicQuote:
    def test_standard(self, quotes):
        o = indicators.get_basic_quote(quotes, CandlePart.OPEN)
        h = indicators.get_basic_quote(quotes, CandlePart.HIGH)
        l = indicators.get_basic_quote(quotes, CandlePart.LOW)
        c = indicators.get_basic_quote(quotes, CandlePart.CLOSE)
        v = indicators.get_basic_quote(quotes, CandlePart.VOLUME)
        hl = indicators.get_basic_quote(quotes, CandlePart.HL2)
        hlc = indicators.get_basic_quote(quotes, CandlePart.HLC3)
        oc = indicators.get_basic_quote(quotes, CandlePart.OC2)
        ohl = indicators.get_basic_quote(quotes, CandlePart.OHL3)
        ohlc = indicators.get_basic_quote(quotes, CandlePart.OHLC4)
        
        assert 502 == len(c)
        
        assert datetime(2018, 12, 31) == c[-1].date
        
        assert 244.92       ==  o[-1].value
        assert 245.54       ==  h[-1].value
        assert 242.87       ==  l[-1].value
        assert 245.28       ==  c[-1].value
        assert 147031456    ==  v[-1].value
        assert 244.205      ==  hl[-1].value
        assert 244.5633     ==  round(float(hlc[-1].value), 4)
        assert 245.1        ==  oc[-1].value
        assert 244.4433     ==  round(float(ohl[-1].value), 4)
        assert 244.6525     ==  ohlc[-1].value
        
    def test_use(self, quotes):
        results = Quote.use(quotes, CandlePart.CLOSE)
        results = list(results)
        
        assert 502 == len(results)
