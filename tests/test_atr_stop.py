import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import EndType

class TestAtrStop:
    def test_standard(self, quotes):
        results = indicators.get_atr_stop(quotes, 21, 3, EndType.CLOSE)
        
        assert 502 == len(results)
        assert 481 == len(list(filter(lambda x: x.atr_stop is not None, results)))
        
        r = results[20]
        assert r.atr_stop is None
        assert r.buy_stop is None
        assert r.sell_stop is None

        r = results[21]
        assert 211.13 == round(float(r.atr_stop), 4)
        assert r.buy_stop is None
        assert r.atr_stop == r.sell_stop

        r = results[151]
        assert 232.7861 == round(float(r.atr_stop), 4)
        assert r.buy_stop is None
        assert r.atr_stop == r.sell_stop

        r = results[152]
        assert 236.3913 == round(float(r.atr_stop), 4)
        assert r.atr_stop == r.buy_stop
        assert r.sell_stop is None

        r = results[249]
        assert 253.8863 == round(float(r.atr_stop), 4)
        assert r.buy_stop is None
        assert r.atr_stop == r.sell_stop

        r = results[501]
        assert 246.3232 == round(float(r.atr_stop), 4)
        assert r.atr_stop == r.buy_stop
        assert r.sell_stop is None

    def test_high_low(self, quotes):
        results = indicators.get_atr_stop(quotes, 21, 3, EndType.HIGH_LOW)
        
        assert 502 == len(results)
        assert 481 == len(list(filter(lambda x: x.atr_stop is not None, results)))
        
        r = results[20]
        assert r.atr_stop is None
        assert r.buy_stop is None
        assert r.sell_stop is None

        r = results[21]
        assert 210.23 == round(float(r.atr_stop), 4)
        assert r.buy_stop is None
        assert r.atr_stop == r.sell_stop

        r = results[69]
        assert 221.0594 == round(float(r.atr_stop), 4)
        assert r.buy_stop is None
        assert r.atr_stop == r.sell_stop

        r = results[70]
        assert 226.4624 == round(float(r.atr_stop), 4)
        assert r.atr_stop == r.buy_stop
        assert r.sell_stop is None

        r = results[249]
        assert 253.4863 == round(float(r.atr_stop), 4)
        assert r.buy_stop is None
        assert r.atr_stop == r.sell_stop

        r = results[501]
        assert 252.6932 == round(float(r.atr_stop), 4)
        assert r.atr_stop == r.buy_stop
        assert r.sell_stop is None


    def test_bad_data(self, bad_quotes):
        r = indicators.get_atr_stop(bad_quotes, 7)
        
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_atr_stop([])
        assert 0 == len(r)

        r = indicators.get_atr_stop(quotes[:1])
        assert 1 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_atr_stop(quotes, 21, 3).remove_warmup_periods()

        assert 481 == len(results)

        last = results.pop()
        assert 246.3232 == round(float(last.atr_stop), 4)
        assert last.atr_stop == last.buy_stop
        assert last.sell_stop is None

    def test_condense(self, quotes):
        results = indicators.get_atr_stop(quotes, 21, 3).condense()

        assert 481 == len(results)

        r = results[-1]
        assert 246.3232 == round(float(r.atr_stop), 4)
        assert r.atr_stop == r.buy_stop
        assert r.sell_stop is None

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_atr_stop(quotes, 1)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_atr_stop(quotes, 7, 0)
