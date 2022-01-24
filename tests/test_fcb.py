import pytest
from stock_indicators import indicators

class TestFCB:
    def test_standard(self, quotes):
        results = indicators.get_fcb(quotes, 2)
        
        assert 502 == len(results)
        assert 497 == len(list(filter(lambda x: x.upper_band is not None, results)))
        assert 493 == len(list(filter(lambda x: x.lower_band is not None, results)))
        
        r = results[4]
        assert r.upper_band is None
        assert r.lower_band is None
        
        r = results[10]
        assert 214.84 == round(float(r.upper_band), 2)
        assert 212.53 == round(float(r.lower_band), 2)
        
        r = results[120]
        assert 233.35 == round(float(r.upper_band), 2)
        assert 231.14 == round(float(r.lower_band), 2)
        
        r = results[180]
        assert 236.78 == round(float(r.upper_band), 2)
        assert 233.56 == round(float(r.lower_band), 2)
        
        r = results[250]
        assert 258.70 == round(float(r.upper_band), 2)
        assert 257.04 == round(float(r.lower_band), 2)
        
        r = results[501]
        assert 262.47 == round(float(r.upper_band), 2)
        assert 229.42 == round(float(r.lower_band), 2)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_fcb(bad_quotes)
        
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_fcb(quotes, 2).remove_warmup_periods()
        
        assert 502 - 5 == len(results)
        
        last = results.pop()
        assert 262.47 == round(float(last.upper_band), 2)
        assert 229.42 == round(float(last.lower_band), 2)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_fcb(quotes, 1)
