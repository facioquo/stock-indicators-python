import pytest
from stock_indicators import indicators

class TestEPMA:
    def test_standard(self, quotes):
        results = indicators.get_epma(quotes, 20)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.epma is not None, results)))
        
        r = results[18]
        assert r.epma is None
        
        r = results[19]
        assert 215.6189 == round(float(r.epma), 4)
        
        r = results[149]
        assert 236.7060 == round(float(r.epma), 4)
        
        r = results[249]
        assert 258.5179 == round(float(r.epma), 4)
        
        r = results[501]
        assert 235.8131 == round(float(r.epma), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_epma(bad_quotes, 15)
        
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_epma(quotes, 20).remove_warmup_periods()
        
        assert 502 - 19 == len(results)
        
        last = results.pop()
        assert 235.8131 == round(float(last.epma), 4)
        

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_epma(quotes, 0)
