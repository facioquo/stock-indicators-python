import pytest
from stock_indicators import indicators

class TestTSI:
    def test_standard(self, quotes):
        results = indicators.get_tsi(quotes, 25, 13, 7)
        
        assert 502 == len(results)
        assert 465 == len(list(filter(lambda x: x.tsi is not None, results)))
        assert 459 == len(list(filter(lambda x: x.signal is not None, results)))
        
        r = results[37]
        assert 53.1204 == round(float(r.tsi), 4)
        assert r.signal is None
        
        r = results[43]
        assert 46.0960 == round(float(r.tsi), 4)
        assert 51.6916 == round(float(r.signal), 4)
        
        r = results[44]
        assert 42.5121 == round(float(r.tsi), 4)
        assert 49.3967 == round(float(r.signal), 4)
        
        r = results[149]
        assert 29.0936 == round(float(r.tsi), 4)
        assert 28.0134 == round(float(r.signal), 4)
        
        r = results[249]
        assert 41.9232 == round(float(r.tsi), 4)
        assert 42.4063 == round(float(r.signal), 4)
        
        r = results[501]
        assert -28.3513 == round(float(r.tsi), 4)
        assert -29.3597 == round(float(r.signal), 4)
                
    def test_bad_data(self, bad_quotes):
        r = indicators.get_tsi(bad_quotes)
        assert 502 == len(r)
        
    def test_big_data(self, big_quotes):
        r = indicators.get_tsi(big_quotes)
        assert 1246 == len(r)
        
    def test_no_data(self, quotes):
        r = indicators.get_tsi([])
        assert 0 == len(r)
        
        r = indicators.get_tsi(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_tsi(quotes, 25, 13, 7)
        results = results.remove_warmup_periods()
        
        assert 502 - (25 + 13 + 250) == len(results)
        
        last = results.pop()
        assert -28.3513 == round(float(last.tsi), 4)
        assert -29.3597 == round(float(last.signal), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_tsi(quotes, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_tsi(quotes, 25, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_tsi(quotes, 25, 13, -1)
