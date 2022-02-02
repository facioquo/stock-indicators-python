import pytest
from stock_indicators import indicators

class TestMFI:
    def test_standard(self, quotes):
        results = indicators.get_mfi(quotes, 14)
        
        assert 502 == len(results)
        assert 488 == len(list(filter(lambda x: x.mfi is not None, results)))
        
        r = results[439]
        assert 69.0622 == round(float(r.mfi), 4)
        
        r = results[501]
        assert 39.9494 == round(float(r.mfi), 4)
        
    def test_small_lookback(self, quotes):
        results = indicators.get_mfi(quotes, 4)
        
        assert 502 == len(results)
        assert 498 == len(list(filter(lambda x: x.mfi is not None, results)))
        
        r = results[31]
        assert 100 == round(float(r.mfi), 4)
        
        r = results[43]
        assert 0 == round(float(r.mfi), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_mfi(bad_quotes, 15)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_mfi([])
        assert 0 == len(r)
        
        r = indicators.get_mfi(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_mfi(quotes, 14).remove_warmup_periods()
        
        assert 502 - 14 == len(results)
        
        last = results.pop()
        assert 39.9494 == round(float(last.mfi), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_mfi(quotes, 1)
