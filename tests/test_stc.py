import pytest
from stock_indicators import indicators

class TestSTC:
    def test_standard(self, quotes):
        cycle_periods = 9
        fast_periods = 12
        slow_periods = 26
        
        results = indicators.get_stc(quotes, cycle_periods, fast_periods, slow_periods)
        
        r = results[34]
        assert r.stc is None
        
        r = results[35]
        assert 100 == round(float(r.stc), 4)
        
        r = results[49]
        assert 0.8370 == round(float(r.stc), 4)
        
        r = results[249]
        assert 27.7340 == round(float(r.stc), 4)
        
        r = results.pop()
        assert 19.2544 == round(float(r.stc), 4)
     
    def test_bad_data(self, bad_quotes):
        r = indicators.get_stc(bad_quotes, 10, 23, 50)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_stc([])
        assert 0 == len(r)
        
        r = indicators.get_stc(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        cycle_periods = 9
        fast_periods = 12
        slow_periods = 26
        
        results = indicators.get_stc(quotes, cycle_periods, fast_periods, slow_periods)
        results = results.remove_warmup_periods()
        
        last = results.pop()
        assert 19.2544 == round(float(last.stc), 4)
    
    def test_exceptions(self, quotes, other_quotes, mismatch_quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stc(quotes, 9, 0, 26)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stc(quotes, 9, 12, 12)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stc(quotes, -1, 12, 26)
