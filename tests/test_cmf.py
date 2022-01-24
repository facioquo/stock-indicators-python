import pytest
from stock_indicators import indicators

class TestCMF:
    def test_standard(self, quotes):
        results = indicators.get_cmf(quotes, 20)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.cmf is not None, results)))
        
        r = results[49]
        assert 000.5468 == round(float(r.money_flow_multiplier), 4)
        assert 55609259 == round(float(r.money_flow_volume), 2)
        assert 0.350596 == round(float(r.cmf), 6)
        
        r = results[249]
        assert      0.7778 == round(float(r.money_flow_multiplier), 4)
        assert 36433792.89 == round(float(r.money_flow_volume), 2)
        assert   -0.040226 == round(float(r.cmf), 6)
        
        r = results[501]
        assert       0.8052 == round(float(r.money_flow_multiplier), 4)
        assert 118396116.25 == round(float(r.money_flow_volume), 2)
        assert    -0.123754 == round(float(r.cmf), 6)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_cmf(bad_quotes, 15)
        assert 502 == len(r)
        
    def test_big_data(self, big_quotes):
        r = indicators.get_cmf(big_quotes, 150)
        assert 1246 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_cmf(quotes, 20).remove_warmup_periods()
        
        assert 502 - 19 == len(results)
        
        last = results.pop()
        assert       0.8052 == round(float(last.money_flow_multiplier), 4)
        assert 118396116.25 == round(float(last.money_flow_volume), 2)
        assert    -0.123754 == round(float(last.cmf), 6)
   
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_cmf(quotes, 0)
