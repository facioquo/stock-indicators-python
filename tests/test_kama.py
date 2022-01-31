import pytest
from stock_indicators import indicators

class TestKAMA:
    def test_standard(self, quotes):
        results = indicators.get_kama(quotes, 10, 2, 30)
        
        assert 502 == len(results)
        assert 492 == len(list(filter(lambda x: x.efficiency_ratio is not None, results)))
        assert 493 == len(list(filter(lambda x: x.kama is not None, results)))
        
        r = results[8]
        assert r.efficiency_ratio is None
        assert r.kama is None
        
        r = results[9]
        assert r.efficiency_ratio is None
        assert 213.75 == round(float(r.kama), 2)
        
        r = results[10]
        assert   0.2465 == round(float(r.efficiency_ratio), 4)
        assert 213.7713 == round(float(r.kama), 4)
        
        r = results[24]
        assert   0.2136 == round(float(r.efficiency_ratio), 4)
        assert 214.7423 == round(float(r.kama), 4)
        
        r = results[149]
        assert   0.3165 == round(float(r.efficiency_ratio), 4)
        assert 235.5510 == round(float(r.kama), 4)
        
        r = results[249]
        assert   0.3182 == round(float(r.efficiency_ratio), 4)
        assert 256.0898 == round(float(r.kama), 4)
        
        r = results[501]
        assert   0.2214 == round(float(r.efficiency_ratio), 4)
        assert 240.1138 == round(float(r.kama), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_kama(bad_quotes)
        assert 502 == len(r)
    
    def test_no_quotes(self, quotes):
        r = indicators.get_kama([])
        assert 0 == len(r)
        
        r = indicators.get_kama(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        er_periods = 10
        fast_periods = 2
        slow_periods = 30
        
        results = indicators.get_kama(quotes, er_periods, fast_periods, slow_periods)
        results = results.remove_warmup_periods()
        
        assert 502 - max(er_periods + 100, er_periods * 10) == len(results)
        
        last = results.pop()
        
        assert   0.2214 == round(float(last.efficiency_ratio), 4)
        assert 240.1138 == round(float(last.kama), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_kama(quotes, 0, 2, 30)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_kama(quotes, 10, 0, 30)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_kama(quotes, 10, 5, 5)
