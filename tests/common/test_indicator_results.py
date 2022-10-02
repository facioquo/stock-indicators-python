from datetime import datetime

import pytest
from stock_indicators import indicators

class TestIndicatorResults:
    def test_add_results(self, quotes):
        results = indicators.get_sma(quotes, 20)
        r4 = results + results + results + results
        
        assert len(r4) == len(results) * 4
        
        for i in range(4):
            idx = len(results)*i
            assert r4[18+idx].sma is None
            assert 214.5250 == round(float(r4[19+idx].sma), 4)
            assert 215.0310 == round(float(r4[24+idx].sma), 4)
            assert 234.9350 == round(float(r4[149+idx].sma), 4)
            assert 255.5500 == round(float(r4[249+idx].sma), 4)
            assert 251.8600 == round(float(r4[501+idx].sma), 4)
    
    def test_mul_results(self, quotes):
        results = indicators.get_sma(quotes, 20)
        r4 = results * 4
        
        assert len(r4) == len(results) * 4

        for i in range(4):
            idx = len(results)*i
            assert r4[18+idx].sma is None
            assert 214.5250 == round(float(r4[19+idx].sma), 4)
            assert 215.0310 == round(float(r4[24+idx].sma), 4)
            assert 234.9350 == round(float(r4[149+idx].sma), 4)
            assert 255.5500 == round(float(r4[249+idx].sma), 4)
            assert 251.8600 == round(float(r4[501+idx].sma), 4)
            
    def test_done_and_reload(self, quotes):
        results = indicators.get_sma(quotes, 20)
        results.done()
        
        with pytest.raises(ValueError):
            results * 2

        results.reload()
        r2 = results * 2
        
        assert len(r2) == len(results) * 2
        
    def test_find(self, quotes):
        results = indicators.get_sma(quotes, 20)
        
        # r[18]
        r = results.find(datetime(2017, 1, 30))
        assert r.sma is None

    def test_remove_with_period(self, quotes):
        results = indicators.get_sma(quotes, 20)
        length = len(results)
        
        results = results.remove_warmup_periods(50)
        assert len(results) == length - 50
