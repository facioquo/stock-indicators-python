import pytest
from stock_indicators import indicators

class TestMAMA:
    def test_standard(self, quotes):
        results = indicators.get_mama(quotes, 0.5, 0.05)
        
        assert 502 == len(results)
        assert 497 == len(list(filter(lambda x: x.mama is not None, results)))
        
        r = results[4]
        assert r.mama is None
        assert r.fama is None
        
        r = results[5]
        assert 213.73 == round(float(r.mama), 2)
        assert 213.73 == round(float(r.fama), 2)
        
        r = results[6]
        assert  213.7850 == round(float(r.mama), 4)
        assert 213.74375 == round(float(r.fama), 5)
        
        r = results[25]
        assert 215.9524 == round(float(r.mama), 4)
        assert 215.1407 == round(float(r.fama), 4)
        
        r = results[149]
        assert 235.6593 == round(float(r.mama), 4)
        assert 234.3660 == round(float(r.fama), 4)
        
        r = results[249]
        assert 256.8026 == round(float(r.mama), 4)
        assert 254.0605 == round(float(r.fama), 4)
        
        r = results[501]
        assert 244.1092 == round(float(r.mama), 4)
        assert 252.6139 == round(float(r.fama), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_mama(bad_quotes)
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_mama([])
        assert 0 == len(r)
        
        r = indicators.get_mama(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_mama(quotes, 0.5, 0.05)
        results = results.remove_warmup_periods()
        
        assert 502 - 50 == len(results)
        
        last = results.pop()        
        assert 244.1092 == round(float(last.mama), 4)
        assert 252.6139 == round(float(last.fama), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_mama(quotes, 0.5, 0.5)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_mama(quotes, 1, 0.5)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_mama(quotes, 0.5, 0)
