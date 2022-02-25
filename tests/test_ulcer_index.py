import pytest
from stock_indicators import indicators

class TestUlcerIndex:
    def test_standard(self, quotes):
        results = indicators.get_ulcer_index(quotes, 14)
        
        assert 502 == len(results)
        assert 489 == len(list(filter(lambda x: x.ui is not None, results)))
        
        r = results[501]
        assert 5.7255 == round(float(r.ui), 4)
                
    def test_bad_data(self, bad_quotes):
        r = indicators.get_ulcer_index(bad_quotes, 15)
        assert 502 == len(r)
        
    def test_no_data(self, quotes):
        r = indicators.get_ulcer_index([])
        assert 0 == len(r)
        
        r = indicators.get_ulcer_index(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_ulcer_index(quotes, 14)
        results = results.remove_warmup_periods()
        
        assert 502 - 13 == len(results)
        
        last = results.pop()
        assert 5.7255 == round(float(last.ui), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ulcer_index(quotes, 0)
