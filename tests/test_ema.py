import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import CandlePart

class TestEMA:
    def test_standard(self, quotes):
        results = indicators.get_ema(quotes, 20)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.ema is not None, results)))

        r = results[29]
        assert 216.6228 == round(float(r.ema), 4)

        r = results[249]
        assert 255.3873 == round(float(r.ema), 4)

        r = results[501]
        assert 249.3519 == round(float(r.ema), 4)

    def test_custom(self, quotes):
        results = indicators.get_ema(quotes, 20, CandlePart.OPEN)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.ema is not None, results)))

        r = results[29]
        assert 216.2643 == round(float(r.ema), 4)

        r = results[249]
        assert 255.4875 == round(float(r.ema), 4)

        r = results[501]
        assert 249.9157 == round(float(r.ema), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_ema(bad_quotes, 15)

        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_ema([], 10)
        assert 0 == len(r)
        
        r = indicators.get_ema(quotes[:1], 10)
        assert 1 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_ema(quotes, 20).remove_warmup_periods()

        assert 502 - (20 + 100) == len(results)

        last = results.pop()
        assert 249.3519 == round(float(last.ema), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ema(quotes, 0)
