import pytest
from stock_indicators import indicators

class TestCCI:
    def test_standard(self, quotes):
        results = indicators.get_cci(quotes, 20)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.cci is not None, results)))
        
        r = results[501]
        assert -52.9946 == round(float(r.cci), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_cci(bad_quotes, 15)
        assert 502 == len(r)
    
    def test_removed(self, quotes):
        results = indicators.get_cci(quotes, 20).remove_warmup_periods()
        
        assert 502 - 19 == len(results)
        
        last = results.pop()
        assert -52.9946 == round(float(last.cci), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_cci(quotes, 0)
