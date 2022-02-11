import pytest
from stock_indicators import indicators

class TestPMO:
    def test_standard(self, quotes):
        results = indicators.get_pmo(quotes, 35, 20, 10)
        
        assert 502 == len(results)
        assert 448 == len(list(filter(lambda x: x.pmo is not None, results)))
        assert 439 == len(list(filter(lambda x: x.signal is not None, results)))
        
        r = results[92]
        assert 0.6159 == round(float(r.pmo), 4)
        assert 0.5582 == round(float(r.signal), 4)
        
        r = results[501]
        assert -2.7016 == round(float(r.pmo), 4)
        assert -2.3117 == round(float(r.signal), 4)
           
    def test_bad_data(self, bad_quotes):
        r = indicators.get_pmo(bad_quotes, 25, 15, 5)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_pmo([])
        assert 0 == len(r)
        
        r = indicators.get_pmo(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_pmo(quotes, 35, 20, 10).remove_warmup_periods()
        
        assert 502 - (35 + 20 + 250) == len(results)   
        
        last = results.pop()
        assert -2.7016 == round(float(last.pmo), 4)
        assert -2.3117 == round(float(last.signal), 4)
           
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pmo(quotes, 1)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pmo(quotes, 5, 0)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pmo(quotes, 5, 5, 0)
