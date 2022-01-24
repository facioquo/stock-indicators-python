import pytest
from stock_indicators import indicators

class TestElderRay:
    def test_standard(self, quotes):
        results = indicators.get_elder_ray(quotes, 13)
        
        assert 502 == len(results)
        assert 490 == len(list(filter(lambda x: x.bull_power is not None, results)))
        assert 490 == len(list(filter(lambda x: x.bear_power is not None, results)))
        
        r = results[11]
        assert r.ema is None
        assert r.bull_power is None
        assert r.bear_power is None
        
        r = results[12]
        assert 214.0000 == round(float(r.ema), 4)
        assert 000.7500 == round(float(r.bull_power), 4)
        assert -00.5100 == round(float(r.bear_power), 4)
        
        r = results[24]
        assert 215.5426 == round(float(r.ema), 4)
        assert   1.4274 == round(float(r.bull_power), 4)
        assert 000.5474 == round(float(r.bear_power), 4)
        
        r = results[149]
        assert 235.3970 == round(float(r.ema), 4)
        assert 000.9430 == round(float(r.bull_power), 4)
        assert 000.4730 == round(float(r.bear_power), 4)
        
        r = results[249]
        assert 256.5206 == round(float(r.ema), 4)
        assert   1.5194 == round(float(r.bull_power), 4)
        assert   1.0694 == round(float(r.bear_power), 4)
        
        r = results[501]
        assert 246.0129 == round(float(r.ema), 4)
        assert -00.4729 == round(float(r.bull_power), 4)
        assert  -3.1429 == round(float(r.bear_power), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_elder_ray(bad_quotes)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_elder_ray(quotes, 13).remove_warmup_periods()
        
        assert 502 - (100 + 13) == len(results)
        
        last = results.pop()
        assert 246.0129 == round(float(last.ema), 4)
        assert -00.4729 == round(float(last.bull_power), 4)
        assert  -3.1429 == round(float(last.bear_power), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_elder_ray(quotes, 0)
