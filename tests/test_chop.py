import pytest
from stock_indicators import indicators

class TestChop:
    def test_standard(self, quotes):
        results = indicators.get_chop(quotes, 14)
        
        assert 502 == len(results)
        assert 488 == len(list(filter(lambda x: x.chop is not None, results)))
        
        r = results[13]
        assert r.chop is None
        
        r = results[14]
        assert 69.9967 == round(float(r.chop), 4)
        
        r = results[249]
        assert 41.8499 == round(float(r.chop), 4)
        
        r = results[501]
        assert 38.6526 == round(float(r.chop), 4)
        
    def test_small_lookback(self, quotes):
        results = indicators.get_chop(quotes, 2)
        
        assert 502 == len(results)
        assert 500 == len(list(filter(lambda x: x.chop is not None, results)))
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_chop(bad_quotes, 20)
        assert 502 == len(r)
    
    def test_removed(self, quotes):
        results = indicators.get_chop(quotes, 14).remove_warmup_periods()
        
        assert 502 - 14 == len(results)
        
        last = results.pop()
        assert 38.6526 == round(float(last.chop), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_chop(quotes, 1)
