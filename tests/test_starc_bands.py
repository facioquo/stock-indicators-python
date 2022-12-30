import pytest
from stock_indicators import indicators

class TestSTARCBands:
    def test_standard(self, quotes):
        sma_periods = 20
        multiplier = 2
        atr_periods = 14
        lookback_periods = max(sma_periods, atr_periods)

        results = indicators.get_starc_bands(quotes, sma_periods,
                                         multiplier, atr_periods)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.center_line is not None, results)))
        assert 483 == len(list(filter(lambda x: x.upper_band  is not None, results)))
        assert 483 == len(list(filter(lambda x: x.lower_band is not None, results)))

        r = results[18]
        assert r.center_line is None
        assert r.upper_band is None
        assert r.lower_band is None

        r = results[19]
        assert 214.5250 == round(float(r.center_line), 4)
        assert 217.2345 == round(float(r.upper_band), 4)
        assert 211.8155 == round(float(r.lower_band), 4)

        r = results[249]
        assert 255.5500 == round(float(r.center_line), 4)
        assert 258.2261 == round(float(r.upper_band), 4)
        assert 252.8739 == round(float(r.lower_band), 4)

        r = results[485]
        assert 265.4855 == round(float(r.center_line), 4)
        assert 275.1161 == round(float(r.upper_band), 4)
        assert 255.8549 == round(float(r.lower_band), 4)

        r = results[501]
        assert 251.8600 == round(float(r.center_line), 4)
        assert 264.1595 == round(float(r.upper_band), 4)
        assert 239.5605 == round(float(r.lower_band), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_starc_bands(bad_quotes, 10, 3, 15)
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_starc_bands([])
        assert 0 == len(r)

        r = indicators.get_starc_bands(quotes[:1])
        assert 1 == len(r)

    def test_removed(self, quotes):
        sma_periods = 20
        multiplier = 2
        atr_periods = 14
        lookback_periods = max(sma_periods, atr_periods)

        results = indicators.get_starc_bands(quotes, sma_periods,
                                         multiplier, atr_periods)
        results = results.remove_warmup_periods()

        assert 502 - (lookback_periods + 150) == len(results)

        last = results.pop()
        assert 251.8600 == round(float(last.center_line), 4)
        assert 264.1595 == round(float(last.upper_band), 4)
        assert 239.5605 == round(float(last.lower_band), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_starc_bands(quotes, 1, 2, 10)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_starc_bands(quotes, 20, 2, 1)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_starc_bands(quotes, 20, 0, 10)
