import pytest
from stock_indicators import indicators

class TestBOP:
    def test_standard(self, quotes):
        results = indicators.get_bop(quotes, 14)
        
        assert 502 == len(results)
        assert 489 == len(list(filter(lambda x: x.bop is not None, results)))
        
        r = results[12]
        assert r.bop is None
        
        r = results[13]
        assert 0.081822 == round(float(r.bop), 6)
        
        r = results[149]
        assert -0.016203 == round(float(r.bop), 6)
        
        r = results[249]
        assert -0.058682 == round(float(r.bop), 6)
        
        r = results[501]
        assert -0.292788 == round(float(r.bop), 6)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_bop(bad_quotes)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_bop(quotes).remove_warmup_periods()
        
        assert 502 - 13 == len(results)
        
        last = results.pop()
        assert -0.292788 == round(float(last.bop), 6)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_bop(quotes, 0)
