import pytest
from stock_indicators import indicators

class TestDonchian:
    def test_standard(self, quotes):
        results = indicators.get_donchian(quotes, 20)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.center_line is not None, results)))
        assert 482 == len(list(filter(lambda x: x.upper_band is not None, results)))
        assert 482 == len(list(filter(lambda x: x.lower_band is not None, results)))
        assert 482 == len(list(filter(lambda x: x.width is not None, results)))
        
        r = results[19]
        assert r.center_line is None
        assert r.upper_band is None
        assert r.lower_band is None
        assert r.width is None
        
        r = results[20]
        assert 214.2700 == round(float(r.center_line), 4)
        assert 217.0200 == round(float(r.upper_band), 4)
        assert 211.5200 == round(float(r.lower_band), 4)
        assert 0.025669 == round(float(r.width), 6)
        
        r = results[249]
        assert 254.2850 == round(float(r.center_line), 4)
        assert 258.7000 == round(float(r.upper_band), 4)
        assert 249.8700 == round(float(r.lower_band), 4)
        assert 0.034725 == round(float(r.width), 6)
        
        r = results[485]
        assert 265.5350 == round(float(r.center_line), 4)
        assert 274.3900 == round(float(r.upper_band), 4)
        assert 256.6800 == round(float(r.lower_band), 4)
        assert 0.066696 == round(float(r.width), 6)
        
        r = results[501]
        assert 251.5050 == round(float(r.center_line), 4)
        assert 273.5900 == round(float(r.upper_band), 4)
        assert 229.4200 == round(float(r.lower_band), 4)
        assert 0.175623 == round(float(r.width), 6)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_donchian(bad_quotes, 20)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_donchian(quotes, 20).remove_warmup_periods()
        
        assert 502 - 20 == len(results)
        
        last = results.pop()
        assert 251.5050 == round(float(last.center_line), 4)
        assert 273.5900 == round(float(last.upper_band), 4)
        assert 229.4200 == round(float(last.lower_band), 4)
        assert 0.175623 == round(float(last.width), 6)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_donchian(quotes, 0)
