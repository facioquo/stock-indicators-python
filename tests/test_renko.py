import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import EndType

class TestRenko:
    def test_standard_close(self, quotes):
        results = indicators.get_renko(quotes, 2.5, EndType.CLOSE)
        
        assert 112 == len(results)
        assert  62 == len(list(filter(lambda x: x.is_up, results)))
        assert  50 == len(list(filter(lambda x: not x.is_up, results)))
        
        r = results[0]
        assert        213 == float(round(r.open, 0))
        assert     216.89 == float(round(r.high, 2))
        assert     212.53 == float(round(r.low, 2))
        assert      215.5 == float(round(r.close, 1))
        assert 1180981564 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results[5]
        assert      225.5 == float(round(r.open, 1))
        assert     228.15 == float(round(r.high, 2))
        assert     219.77 == float(round(r.low, 2))
        assert        228 == float(round(r.close, 0))
        assert 4192959240 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results.pop()
        assert     240.5 == float(round(r.open, 1))
        assert    243.68 == float(round(r.high, 2))
        assert    234.52 == float(round(r.low, 2))
        assert       243 == float(round(r.close, 0))
        assert 189794032 == float(round(r.volume, 0))
        assert   r.is_up == True
        
    def test_standard_high_low(self, quotes):
        results = indicators.get_renko(quotes, 2.5, EndType.HIGH_LOW)
        
        assert 159 == len(results)
        
        r = results[0]
        assert        213 == float(round(r.open, 0))
        assert     216.89 == float(round(r.high, 2))
        assert     212.53 == float(round(r.low, 2))
        assert      215.5 == float(round(r.close, 1))
        assert 1180981564 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results[25]
        assert      270.5 == float(round(r.open, 1))
        assert     273.16 == float(round(r.high, 2))
        assert     271.96 == float(round(r.low, 2))
        assert        273 == float(round(r.close, 0))
        assert  100801672 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results.pop()
        assert        243 == float(round(r.open, 0))
        assert     246.73 == float(round(r.high, 2))
        assert     241.87 == float(round(r.low, 2))
        assert      245.5 == float(round(r.close, 1))
        assert   51999637 == float(round(r.volume, 0))
        assert    r.is_up == True

    def test_renko_atr(self, quotes):
        results = indicators.get_renko_atr(quotes, 14, EndType.CLOSE)
        
        assert 29 == len(results)
        
        r = results[0]
        assert      212.8 == float(round(r.open, 1))
        assert     220.19 == float(round(r.high, 2))
        assert     212.53 == float(round(r.low, 2))
        assert   218.9497 == float(round(r.close, 4))
        assert 2090292272 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results.pop()
        assert   237.3990 == float(round(r.open, 4))
        assert     246.73 == float(round(r.high, 2))
        assert     229.42 == float(round(r.low, 2))
        assert   243.5487 == float(round(r.close, 4))
        assert  715446448 == float(round(r.volume, 0))
        assert    r.is_up == True

    def test_bad_data(self, bad_quotes):
        r = indicators.get_renko(bad_quotes, 100)
        assert 0 != len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_renko([], 0.01)
        assert 0 == len(r)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_renko(quotes, 0)
