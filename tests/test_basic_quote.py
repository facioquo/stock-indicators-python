from datetime import datetime

import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.chain import IndicatorChain
from stock_indicators.indicators.common.enums import CandlePart


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
    
    def test_chainor(self, quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_basic_quote, CandlePart.CLOSE)\
            .add(indicators.get_sma, 10)\
            .calc()

        assert 502 == len(results)
        assert 493 == len(list(filter(lambda x: x.sma is not None, results)))

    def test_chainee(self, quotes):
        with pytest.raises(ValueError):
            results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_sma)\
            .add(indicators.get_basic_quote)\
            .calc()
