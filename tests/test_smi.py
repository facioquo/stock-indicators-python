import pytest
from stock_indicators import indicators

class TestSMI:
    def test_standard(self, quotes):
        results = indicators.get_smi(quotes, 14, 20, 5, 3)
        
        assert 502 == len(results)
        assert 489 == len(list(filter(lambda x: x.smi is not None, results)))
        assert 489 == len(list(filter(lambda x: x.signal is not None, results)))
        
        r = results[12]
        assert r.smi is None
        assert r.signal is None
        
        r = results[13]
        assert 17.2603 == round(float(r.smi), 4)
        assert 17.2603 == round(float(r.signal), 4)
        
        r = results[14]
        assert 18.6086 == round(float(r.smi), 4)
        assert 17.9344 == round(float(r.signal), 4)
        
        r = results[28]
        assert 51.0417 == round(float(r.smi), 4)
        assert 47.1207 == round(float(r.signal), 4)
        
        r = results[150]
        assert 65.6692 == round(float(r.smi), 4)
        assert 66.3292 == round(float(r.signal), 4)
        
        r = results[250]
        assert 67.2534 == round(float(r.smi), 4)
        assert 67.6261 == round(float(r.signal), 4)
        
        r = results[501]
        assert -52.6560 == round(float(r.smi), 4)
        assert -54.1903 == round(float(r.signal), 4)
        
    def test_no_signal(self, quotes):
        results = indicators.get_smi(quotes, 5, 20, 20, 1)
        
        r = results[487]
        assert r.smi == r.signal
        
        r = results[501]
        assert r.smi == r.signal
        
    def test_small_periods(self, quotes):
        results = indicators.get_smi(quotes, 1, 1, 1, 5)
        
        r = results[51]
        assert     -100 == round(float(r.smi), 4)
        assert -20.8709 == round(float(r.signal), 4)
        
        r = results[81]
        assert        0 == round(float(r.smi), 4)
        assert -14.7101 == round(float(r.signal), 4)
        
        r = results[88]
        assert     100 == round(float(r.smi), 4)
        assert 47.2291 == round(float(r.signal), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_smi(bad_quotes, 5, 5, 1, 5)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_smi([], 5, 5, 2)
        assert 0 == len(r)
        
        r = indicators.get_smi(quotes[:1], 5, 5, 3)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_smi(quotes, 14, 20, 5, 3).remove_warmup_periods()
        
        assert 501 - (14 + 100) == len(results)   
        
        last = results.pop()
        assert -52.6560 == round(float(last.smi), 4)
        assert -54.1903 == round(float(last.signal), 4)
           
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_smi(quotes, 0, 5, 5, 5)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_smi(quotes, 14, 0, 5, 5)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_smi(quotes, 14, 3, 0, 5)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_smi(quotes, 9, 3, 1, 0)
