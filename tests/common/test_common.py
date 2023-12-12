from datetime import datetime
from stock_indicators import indicators

class TestCommon:
    def test_find(self, quotes):
        results = indicators.get_bollinger_bands(quotes)
        
        r = results.find(datetime(2018, 12, 28))
        assert 252.9625 == round(float(r.sma), 4)
        assert 230.3495 == round(float(r.lower_band), 4)
        
        r = results.find(datetime(2018, 12, 31))
        assert 251.8600 == round(float(r.sma), 4)
        assert 230.0196 == round(float(r.lower_band), 4)
        
    
    def test_remove_warmup_periods(self, quotes):
        results = indicators.get_adl(quotes)
        assert 502 == len(results)
        
        results = results.remove_warmup_periods(200)
        assert 302 == len(results)
        
        results = results.remove_warmup_periods(1000)
        assert 0 == len(results)
