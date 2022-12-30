import pytest
from stock_indicators import indicators

class TestSuperTrend:
    def test_standard(self, quotes):
        results = indicators.get_super_trend(quotes, 14, 3)

        assert 502 == len(results)
        assert 488 == len(list(filter(lambda x: x.super_trend is not None, results)))

        r = results[13]
        assert r.super_trend is None
        assert r.upper_band is None
        assert r.lower_band is None

        r = results[14]
        assert 210.6157 == round(float(r.super_trend), 4)
        assert r.upper_band is None
        assert r.super_trend == r.lower_band

        r = results[151]
        assert 232.8520 == round(float(r.super_trend), 4)
        assert r.upper_band is None
        assert r.super_trend == r.lower_band

        r = results[152]
        assert 237.6436 == round(float(r.super_trend), 4)
        assert r.super_trend == r.upper_band
        assert r.lower_band is None

        r = results[249]
        assert 253.8008 == round(float(r.super_trend), 4)
        assert r.upper_band is None
        assert r.super_trend == r.lower_band

        r = results[501]
        assert 250.7954 == round(float(r.super_trend), 4)
        assert r.super_trend == r.upper_band
        assert r.lower_band is None

    def test_bitcoin(self, bitcoin_quotes):
        results = indicators.get_super_trend(bitcoin_quotes, 10, 3)

        assert 1246 == len(results)

        r = results[1208]
        assert 16242.2704 == round(float(r.lower_band), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_super_trend(bad_quotes, 7)

        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_super_trend(quotes, 14, 3).remove_warmup_periods()

        assert 488 == len(results)

        last = results.pop()
        assert 250.7954 == round(float(last.super_trend), 4)
        assert last.super_trend == last.upper_band
        assert last.lower_band is None

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_super_trend(quotes, 1)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_super_trend(quotes, 7, 0)
