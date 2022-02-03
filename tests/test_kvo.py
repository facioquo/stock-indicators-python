import pytest
from stock_indicators import indicators

class TestKVO:
    def test_standard(self, quotes):
        results = indicators.get_kvo(quotes, 34, 55, 13)
        
        assert 502 == len(results)
        
        assert 446 == len(list(filter(lambda x: x.oscillator is not None, results)))
        assert 434 == len(list(filter(lambda x: x.signal is not None, results)))
        
        r = results[55]
        assert r.oscillator is None
        assert r.signal is None
        
        r = results[56]
        assert -2138454001 == round(float(r.oscillator), 0)
        assert r.signal is None
        
        r = results[57]
        assert -2265495450 == round(float(r.oscillator), 0)
        assert r.signal is None
        
        r = results[68]
        assert -1241548491 == round(float(r.oscillator), 0)
        assert -1489659254 == round(float(r.signal), 0)
        
        r = results[149]
        assert -62800843 == round(float(r.oscillator), 0)
        assert -18678832 == round(float(r.signal), 0)
        
        r = results[249]
        assert -51541005 == round(float(r.oscillator), 0)
        assert 135207969 == round(float(r.signal), 0)
        
        r = results[501]
        assert  -539224047 == round(float(r.oscillator), 0)
        assert -1548306127 == round(float(r.signal), 0)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_kvo(bad_quotes)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_kvo([])
        assert 0 == len(r)
        
        r = indicators.get_kvo(quotes[:1])
        assert 1 == len(r)
    
    def test_removed(self, quotes):
        results = indicators.get_kvo(quotes, 34, 55, 13).remove_warmup_periods()
        
        assert 502 - (55 + 150) == len(results)
        
        last = results.pop()
        assert  -539224047 == round(float(last.oscillator), 0)
        assert -1548306127 == round(float(last.signal), 0)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_kvo(quotes, 2)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_kvo(quotes, 20, 20)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_kvo(quotes, 34, 55, 0)
