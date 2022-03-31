import pytest
from stock_indicators import indicators

class TestPVO:
    def test_standard(self, quotes):
        results = indicators.get_pvo(quotes, 12, 26, 9)
        
        assert 502 == len(results)
        assert 477 == len(list(filter(lambda x: x.pvo is not None, results)))
        assert 469 == len(list(filter(lambda x: x.signal is not None, results)))
        assert 469 == len(list(filter(lambda x: x.histogram is not None, results)))
        
        r = results[24]
        assert r.pvo is None
        assert r.signal is None
        assert r.histogram is None
        
        r = results[33]
        assert  1.5795 == float(round(r.pvo, 4))
        assert -3.5530 == float(round(r.signal, 4))
        assert  5.1325 == float(round(r.histogram, 4))
        
        r = results[149]
        assert -7.1910 == float(round(r.pvo, 4))
        assert -5.1159 == float(round(r.signal, 4))
        assert -2.0751 == float(round(r.histogram, 4))
        
        r = results[249]
        assert -6.3667 == float(round(r.pvo, 4))
        assert  1.7333 == float(round(r.signal, 4))
        assert -8.1000 == float(round(r.histogram, 4))
        
        r = results[501]
        assert 10.4395 == float(round(r.pvo, 4))
        assert 12.2681 == float(round(r.signal, 4))
        assert -1.8286 == float(round(r.histogram, 4))
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_pvo(bad_quotes, 10, 20, 5)
        assert 502 == len(r)
    
    def test_no_quotes(self, quotes):
        r = indicators.get_pvo([])
        assert 0 == len(r)
        
        r = indicators.get_pvo(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        fast_periods = 12
        slow_periods = 26
        signal_periods = 9
        
        results = indicators.get_pvo(quotes, fast_periods, slow_periods, signal_periods)
        results = results.remove_warmup_periods()
        
        assert 502 - (slow_periods + signal_periods + 250) == len(results)
        
        last = results.pop()
        assert 10.4395 == float(round(last.pvo, 4))
        assert 12.2681 == float(round(last.signal, 4))
        assert -1.8286 == float(round(last.histogram, 4))
                
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pvo(quotes, 0, 26, 9)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pvo(quotes, 12, 12, 9)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pvo(quotes, 12, 26, -1)
