import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import ChandelierType

class TestChandelier:
    def test_standard(self, quotes):
        long_results = indicators.get_chandelier(quotes, 22, 3)

        assert 502 == len(long_results)
        assert 480 == len(list(filter(lambda x: x.chandelier_exit is not None, long_results)))

        r = long_results[501]
        assert 256.5860 == round(float(r.chandelier_exit), 4)

        r = long_results[492]
        assert 259.0480 == round(float(r.chandelier_exit), 4)

        short_results = indicators.get_chandelier(quotes, 22, 3, ChandelierType.SHORT)

        r = short_results[501]
        assert 246.4240 == round(float(r.chandelier_exit), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_chandelier(bad_quotes, 15, 2)
        assert 502 == len(r)

    def test_no_data(self, quotes):
        r = indicators.get_chandelier([])
        assert 0 == len(r)

        r = indicators.get_chandelier(quotes[:1])
        assert 1 == len(r)

    def test_removed(self, quotes):
        long_results = indicators.get_chandelier(quotes, 22, 3).remove_warmup_periods()

        assert 480 == len(long_results)

        last = long_results.pop()
        assert 256.5860 == round(float(last.chandelier_exit), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_chandelier(quotes, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_chandelier(quotes, 25, 0)
