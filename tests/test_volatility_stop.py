import pytest
from stock_indicators import indicators

class TestVolatilityStop:
    def test_standard(self, quotes):
        results = indicators.get_volatility_stop(quotes, 14, 3)

        assert 502 == len(results)
        assert 448 == len(list(filter(lambda x: x.sar is not None, results)))

        r = results[53]
        assert r.sar is None
        assert r.is_stop is None
        assert r.lower_band is None
        assert r.upper_band is None

        r = results[54]
        assert 226.2118 == round(float(r.sar), 4)
        assert r.is_stop is False
        assert 226.2118 == round(float(r.upper_band), 4)
        assert r.lower_band is None

        r = results[55]
        assert 226.2124 == round(float(r.sar), 4)
        assert r.is_stop is False
        assert 226.2124 == round(float(r.upper_band), 4)
        assert r.lower_band is None

        r = results[168]
        assert r.is_stop is True

        r = results[282]
        assert 261.8687 == round(float(r.sar), 4)
        assert r.is_stop is True
        assert 261.8687 == round(float(r.upper_band), 4)
        assert r.lower_band is None

        r = results[283]
        assert 249.3219 == round(float(r.sar), 4)
        assert r.is_stop is False
        assert 249.3219 == round(float(r.lower_band), 4)
        assert r.upper_band is None

        r = results[284]
        assert 249.7460 == round(float(r.sar), 4)
        assert r.is_stop is False
        assert 249.7460 == round(float(r.lower_band), 4)
        assert r.upper_band is None

        last = results.pop()
        assert 249.2423 == round(float(last.sar), 4)
        assert last.is_stop is False
        assert 249.2423 == round(float(last.upper_band), 4)
        assert last.lower_band is None

    def test_bad_data(self, bad_quotes):
        r = indicators.get_volatility_stop(bad_quotes)
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_volatility_stop([])
        assert 0 == len(r)

        r = indicators.get_volatility_stop(quotes[:1])
        assert 1 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_volatility_stop(quotes, 14, 3)
        results = results.remove_warmup_periods()

        assert 402 == len(results)

        last = results.pop()
        assert 249.2423 == round(float(last.sar), 4)
        assert last.is_stop is False

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_volatility_stop(quotes, 1)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_volatility_stop(quotes, 20, 0)
