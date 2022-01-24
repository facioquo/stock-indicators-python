import pytest
from stock_indicators import indicators

class TestChaikinOsc:
    def test_standard(self, quotes):
        fast_periods = 3
        slow_periods = 10
        
        results = indicators.get_chaikin_osc(quotes, fast_periods, slow_periods)
        
        assert 502 == len(results)
        assert 502 - slow_periods + 1 == len(list(filter(lambda x: x.oscillator is not None, results)))
        
        r = results[501]
        assert 3439986548.42 == round(float(r.adl), 2)
        assert        0.8052 == round(float(r.money_flow_multiplier), 4)
        assert  118396116.25 == round(float(r.money_flow_volume), 2)
        assert  -19135200.72 == round(float(r.oscillator), 2)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_chaikin_osc(bad_quotes, 5, 15)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        fast_periods = 3
        slow_periods = 10
        
        results = indicators.get_chaikin_osc(quotes, fast_periods, slow_periods).remove_warmup_periods()
        
        assert 502 - (slow_periods + 100) == len(results)
        
        last = results.pop()
        assert 3439986548.42 == round(float(last.adl), 2)
        assert        0.8052 == round(float(last.money_flow_multiplier), 4)
        assert  118396116.25 == round(float(last.money_flow_volume), 2)
        assert  -19135200.72 == round(float(last.oscillator), 2)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_chaikin_osc(quotes, 0)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_chaikin_osc(quotes, 10, 5)
