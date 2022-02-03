import pytest
from stock_indicators import indicators

class TestKeltner:
    def test_standard(self, quotes):
        ema_periods = 20
        multiplier = 2
        atr_periods = 10
        
        results = indicators.get_keltner(quotes, ema_periods,
                                         multiplier, atr_periods)
        
        assert 502 == len(results)
        
        warmup_periods = 502 - max(ema_periods, atr_periods) + 1
        assert warmup_periods == len(list(filter(lambda x: x.center_line is not None, results)))
        assert warmup_periods == len(list(filter(lambda x: x.upper_band  is not None, results)))
        assert warmup_periods == len(list(filter(lambda x: x.lower_band is not None, results)))
        assert warmup_periods == len(list(filter(lambda x: x.width is not None, results)))
        
        r = results[485]
        assert 275.4260 == round(float(r.upper_band), 4)
        assert 265.4599 == round(float(r.center_line), 4)
        assert 255.4938 == round(float(r.lower_band), 4)
        assert 0.075085 == round(float(r.width), 6)
        
        r = results[501]
        assert 262.1873 == round(float(r.upper_band), 4)
        assert 249.3519 == round(float(r.center_line), 4)
        assert 236.5165 == round(float(r.lower_band), 4)
        assert 0.102950 == round(float(r.width), 6)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_keltner(bad_quotes, 10, 3, 15)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_keltner([])
        assert 0 == len(r)
        
        r = indicators.get_keltner(quotes[:1])
        assert 1 == len(r)
    
    def test_removed(self, quotes):
        ema_periods = 20
        multiplier = 2
        atr_periods = 10
        n = max(ema_periods, atr_periods)
        
        results = indicators.get_keltner(quotes, ema_periods,
                                         multiplier, atr_periods)
        results = results.remove_warmup_periods()
        
        assert 502 - max(2 * n, n + 100) == len(results)
        
        last = results.pop()
        assert 262.1873 == round(float(last.upper_band), 4)
        assert 249.3519 == round(float(last.center_line), 4)
        assert 236.5165 == round(float(last.lower_band), 4)
        assert 0.102950 == round(float(last.width), 6)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_keltner(quotes, 1, 2, 10)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_keltner(quotes, 20, 2, 1)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_keltner(quotes, 20, 0, 10)
        