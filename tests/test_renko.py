import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import EndType

class TestRenko:
    def test_standard_close(self, quotes):
        results = indicators.get_renko(quotes, 2.5, EndType.CLOSE)
        
        assert 154 == len(results)
        
        r = results[0]
        assert        213 == float(round(r.open, 0))
        assert     216.89 == float(round(r.high, 2))
        assert     212.53 == float(round(r.low, 2))
        assert      215.5 == float(round(r.close, 1))
        assert 1180981564 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results[5]
        assert      225.5 == float(round(r.open, 1))
        assert     226.34 == float(round(r.high, 2))
        assert     221.64 == float(round(r.low, 2))
        assert        223 == float(round(r.close, 0))
        assert 1150862992 == float(round(r.volume, 0))
        assert    r.is_up == False
        
        r = results[35]
        assert     270.5 == float(round(r.open, 1))
        assert    272.85 == float(round(r.high, 2))
        assert    265.25 == float(round(r.low, 2))
        assert       268 == float(round(r.close, 0))
        assert 132286411 == float(round(r.volume, 0))
        assert   r.is_up == False
        
        r = results[153]
        assert     240.5 == float(round(r.open, 1))
        assert    243.68 == float(round(r.high, 2))
        assert    234.52 == float(round(r.low, 2))
        assert       243 == float(round(r.close, 0))
        assert 189794032 == float(round(r.volume, 0))
        assert   r.is_up == True
        
    def test_standard_high_low(self, quotes):
        results = indicators.get_renko(quotes, 2.5, EndType.HIGH_LOW)
        
        assert 248 == len(results)
        
        r = results[0]
        assert        213 == float(round(r.open, 0))
        assert     216.89 == float(round(r.high, 2))
        assert     212.53 == float(round(r.low, 2))
        assert      215.5 == float(round(r.close, 1))
        assert 1180981564 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results[25]
        assert      240.5 == float(round(r.open, 1))
        assert     244.04 == float(round(r.high, 2))
        assert      240.8 == float(round(r.low, 1))
        assert        243 == float(round(r.close, 0))
        assert  256003600 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results[233]
        assert      240.5 == float(round(r.open, 1))
        assert     245.07 == float(round(r.high, 2))
        assert     235.52 == float(round(r.low, 2))
        assert        238 == float(round(r.close, 0))
        assert  260180208 == float(round(r.volume, 0))
        assert    r.is_up == False
        
        r = results[247]
        assert      245.5 == float(round(r.open, 1))
        assert     245.54 == float(round(r.high, 2))
        assert     242.87 == float(round(r.low, 2))
        assert        243 == float(round(r.close, 0))
        assert  147031456 == float(round(r.volume, 0))
        assert    r.is_up == False
        
    def test_renko_atr(self, quotes):
        results = indicators.get_renko_atr(quotes, 14, EndType.CLOSE)
        
        assert 43 == len(results)
        
        r = results[0]
        assert      212.8 == float(round(r.open, 1))
        assert     220.19 == float(round(r.high, 2))
        assert     212.53 == float(round(r.low, 2))
        assert   218.9497 == float(round(r.close, 4))
        assert 2090292272 == float(round(r.volume, 0))
        assert    r.is_up == True
        
        r = results[10]
        assert   274.2975 == float(round(r.open, 4))
        assert     275.87 == float(round(r.high, 2))
        assert     265.25 == float(round(r.low, 2))
        assert   268.1477 == float(round(r.close, 4))
        assert  627270200 == float(round(r.volume, 0))
        assert    r.is_up == False
        
        r = results[25]
        assert   268.1477 == float(round(r.open, 4))
        assert     270.25 == float(round(r.high, 2))
        assert     261.38 == float(round(r.low, 2))
        assert   261.9980 == float(round(r.close, 4))
        assert 1233408112 == float(round(r.volume, 0))
        assert    r.is_up == False
        
        r = results[42]
        assert   237.3990 == float(round(r.open, 4))
        assert     246.73 == float(round(r.high, 2))
        assert     234.52 == float(round(r.low, 2))
        assert   243.5487 == float(round(r.close, 4))
        assert  492824400 == float(round(r.volume, 0))
        assert    r.is_up == True
        
    # def test_to_quotes(self, quotes):
    #     new_quotes = indicators.get_renko(quotes, 2.5).to_quotes()
        
    #     assert 154 == len(new_quotes)
        
    #     q = new_quotes[153]
    #     assert      240.5 == float(round(q.open, 1))
    #     assert     243.68 == float(round(q.high, 2))
    #     assert     234.52 == float(round(q.low, 2))
    #     assert        243 == float(round(q.close, 0))
    #     assert  189794032 == float(round(q.volume, 0))
        
    # def test_use_as_quotes(self, quotes):
    #     renko_quotes = indicators.get_renko(quotes, 0.5).to_quotes()
    #     renko_sma = indicators.get_sma(renko_quotes, 5)
    #     assert 1124 == len(list(filter(lambda x: x.sma is not None, renko_sma)))
        
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
