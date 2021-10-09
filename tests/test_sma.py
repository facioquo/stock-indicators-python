import pytest
from SkenderStockIndicators import indicators

class TestSMA:
    def test_standard(self, quotes):
        results = indicators.get_sma(quotes, 20)

        # proper quantities
        # should always be the same number of results as there is quotes
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.sma is not None, results)))

        # sample values
        assert results[18].sma is None
        assert 214.5250 == round(float(results[19].sma), 4)
        assert 215.0310 == round(float(results[24].sma), 4)
        assert 234.9350 == round(float(results[149].sma), 4)
        assert 255.5500 == round(float(results[249].sma), 4)
        assert 251.8600 == round(float(results[501].sma), 4)

    def test_bad_data(self, bad_quotes):
        results = indicators.get_sma_extended(bad_quotes, 15)

        assert 502 == len(results)

    def test_removed(self, quotes):
        results = indicators.get_sma(quotes, 20).remove_warmup_periods()

        assert 483 == len(results)
        assert 251.8600 == round(float(results[len(results)-1].sma), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_sma(quotes, 0)

        from Skender.Stock.Indicators import BadQuotesException
        with pytest.raises(BadQuotesException):
            indicators.get_sma(quotes[:9], 10)
