import pytest
from stock_indicators import indicators

class TestUltimate:
    def test_standard(self, quotes):
        results = indicators.get_ultimate(quotes, 7, 14, 28)
        
        assert 502 == len(results)
        assert 474 == len(list(filter(lambda x: x.ultimate is not None, results)))
        
        r = results[74]
        assert 51.7770 == round(float(r.ultimate), 4)
        
        r = results[249]
        assert 45.3121 == round(float(r.ultimate), 4)
        
        r = results[501]
        assert 49.5257 == round(float(r.ultimate), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_ultimate(bad_quotes, 1, 2, 3)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_ultimate([])
        assert 0 == len(r)
        
        r = indicators.get_ultimate(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_ultimate(quotes, 7, 14, 28)
        results = results.remove_warmup_periods()
        
        assert 502 - 28 == len(results)
        
        last = results.pop()
        assert 49.5257 == round(float(last.ultimate), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ultimate(quotes, 0)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ultimate(quotes, 7, 6)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ultimate(quotes, 7, 14, 11)
