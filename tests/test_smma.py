import pytest
from stock_indicators import indicators

class TestSMMA:
    def test_standard(self, quotes):
        results = indicators.get_smma(quotes, 20)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.smma is not None, results)))
        
        r = results[18]
        assert r.smma is None
        
        r = results[19]
        assert r.smma is not None
        
        r = results[19]
        assert 214.52500 == round(float(r.smma), 5)
        
        r = results[20]
        assert 214.55125 == round(float(r.smma), 5)
        
        r = results[21]
        assert 214.58319 == round(float(r.smma), 5)
        
        r = results[100]
        assert 225.78071 == round(float(r.smma), 5)
        
        r = results[501]
        assert 255.67462 == round(float(r.smma), 5)
       
    def test_bad_data(self, bad_quotes):
        r = indicators.get_smma(bad_quotes, 15)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_smma([], 5)
        assert 0 == len(r)
        
        r = indicators.get_smma(quotes[:1], 5)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_smma(quotes, 20).remove_warmup_periods()
        
        assert 502 - (20 + 100) == len(results)
        
        last = results.pop()
        assert 255.67462 == round(float(last.smma), 5)
        
    def test_exceptions(self, quotes, other_quotes, mismatch_quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_smma(quotes, 0)
