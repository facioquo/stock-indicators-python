import pytest
from stock_indicators import indicators

class TestStochRSI:
    def test_fast_rsi(self, quotes):
        rsi_periods = 14
        stoch_periods = 14
        signal_periods = 3
        smooth_periods = 1

        results = indicators.get_stoch_rsi(quotes, rsi_periods, stoch_periods, signal_periods, smooth_periods)

        assert 502 == len(results)
        assert 475 == len(list(filter(lambda x: x.stoch_rsi is not None, results)))
        assert 473 == len(list(filter(lambda x: x.signal is not None, results)))

        r = results[31]
        assert 93.3333 == round(float(r.stoch_rsi), 4)
        assert 97.7778 == round(float(r.signal), 4)

        r = results[152]
        assert 0 == round(float(r.stoch_rsi), 4)
        assert 0 == round(float(r.signal), 4)

        r = results[249]
        assert 36.5517 == round(float(r.stoch_rsi), 4)
        assert 27.3094 == round(float(r.signal), 4)

        r = results[501]
        assert 97.5244 == round(float(r.stoch_rsi), 4)
        assert 89.8385 == round(float(r.signal), 4)

    def test_slow_rsi(self, quotes):
        rsi_periods = 14
        stoch_periods = 14
        signal_periods = 3
        smooth_periods = 3

        results = indicators.get_stoch_rsi(quotes, rsi_periods, stoch_periods, signal_periods, smooth_periods)

        assert 502 == len(results)
        assert 473 == len(list(filter(lambda x: x.stoch_rsi is not None, results)))
        assert 471 == len(list(filter(lambda x: x.signal is not None, results)))

        r = results[31]
        assert 97.7778 == round(float(r.stoch_rsi), 4)
        assert 99.2593 == round(float(r.signal), 4)

        r = results[152]
        assert 00.0000 == round(float(r.stoch_rsi), 4)
        assert 20.0263 == round(float(r.signal), 4)

        r = results[249]
        assert 27.3094 == round(float(r.stoch_rsi), 4)
        assert 33.2716 == round(float(r.signal), 4)

        r = results[501]
        assert 89.8385 == round(float(r.stoch_rsi), 4)
        assert 73.4176 == round(float(r.signal), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_stoch_rsi(bad_quotes, 15, 20, 3, 2)
        
        assert 502 == len(r)

    def test_removed(self, quotes):
        rsi_periods = 14
        stoch_periods = 14
        signal_periods = 3
        smooth_periods = 3

        results = indicators.get_stoch_rsi(quotes, rsi_periods, stoch_periods, signal_periods, smooth_periods)\
            .remove_warmup_periods()

        removed_qty = rsi_periods + stoch_periods + smooth_periods + 100
        assert 502 - removed_qty == len(results)

        last = results.pop()
        assert 89.8385 == round(float(last.stoch_rsi), 4)
        assert 73.4176 == round(float(last.signal), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stoch_rsi(quotes, 0, 14, 3, 1)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stoch_rsi(quotes, 14, 0, 3, 3)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stoch_rsi(quotes, 14, 14, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stoch_rsi(quotes, 14, 14, 3, 0)
