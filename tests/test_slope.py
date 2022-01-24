import pytest
from stock_indicators import indicators

class TestSlope:
    def test_standard(self, quotes):
        results = indicators.get_slope(quotes, 20)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.slope is not None, results)))
        assert 483 == len(list(filter(lambda x: x.stdev is not None, results)))
        assert  20 == len(list(filter(lambda x: x.line is not None, results)))
        
        r = results[249]
        assert 0.312406 == round(float(r.slope), 6)
        assert 180.4164 == round(float(r.intercept), 4)
        assert 000.8056 == round(float(r.r_squared), 4)
        assert   2.0071 == round(float(r.stdev), 4)
        assert r.line is None
        
        r = results[482]
        assert -0.337015 == round(float(r.slope), 6)
        assert  425.1111 == round(float(r.intercept), 4)
        assert 0000.1730 == round(float(r.r_squared), 4)
        assert    4.6719 == round(float(r.stdev), 4)
        assert  267.9069 == round(float(r.line), 4)
        
        r = results[501]
        assert -1.689143 == round(float(r.slope), 6)
        assert 1083.7629 == round(float(r.intercept), 4)
        assert 0000.7955 == round(float(r.r_squared), 4)
        assert   10.9202 == round(float(r.stdev), 4)
        assert  235.8131 == round(float(r.line), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_slope(bad_quotes, 20)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_slope(quotes, 20).remove_warmup_periods()
        assert 502 - 19 == len(results)
        
        last = results.pop()
        assert -1.689143 == round(float(last.slope), 6)
        assert 1083.7629 == round(float(last.intercept), 4)
        assert 0000.7955 == round(float(last.r_squared), 4)
        assert   10.9202 == round(float(last.stdev), 4)
        assert  235.8131 == round(float(last.line), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_slope(quotes, 0)
