import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import Signal

class TestMarubozu:
    def test_standard(self, quotes):
        results = indicators.get_marubozu(quotes, 0.95)
        
        assert 502 == len(results)
        assert 6 == len(list(filter(lambda x: x.signal != Signal.NONE, results)))
        
        r = results[31]
        assert r.price is None
        assert r.signal == 0
        
        r = results[32]
        assert 222.10 == round(float(r.price), 2)
        assert Signal.BULL_SIGNAL == r.signal
        
        r = results[33]
        assert r.price is None
        assert Signal.NONE == r.signal
        
        r = results[34]
        assert r.price is None
        assert Signal.NONE == r.signal
        
        r = results[274]
        assert r.price is None
        assert Signal.NONE == r.signal
        
        r = results[277]
        assert 248.13 == round(float(r.price), 2)
        assert Signal.BEAR_SIGNAL == r.signal
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_marubozu(bad_quotes)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_marubozu([])
        assert 0 == len(r)
        
        r = indicators.get_marubozu(quotes[:1])
        assert 1 == len(r)
        
    def test_condense(self, quotes):
        r = indicators.get_marubozu(quotes, 0.95).condense()
        assert 6 == len(r)
 
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_marubozu(quotes, 0.799)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_marubozu(quotes, 1.001)
