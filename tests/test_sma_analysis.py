import pytest

from stock_indicators import indicators


class TestSMAExtended:
    def test_result_types(self, quotes):
        results = indicators.get_sma_analysis(quotes, 20)

        # Sample value.
        r = results[501]
        assert isinstance(r._csdata.Sma, float)
        assert isinstance(r._csdata.Mad, float)
        assert isinstance(r._csdata.Mse, float)
        assert isinstance(r._csdata.Mape, float)

    def test_extended(self, quotes):
        results = indicators.get_sma_analysis(quotes, 20)

        # proper quantities.
        # should always be the same number of results as there is quotes.
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.sma is not None, results)))

        # Sample value.
        r = results[501]
        assert 251.8600 == round(float(r.sma), 4)
        assert 9.4500 == round(float(r.mad), 4)
        assert 119.2510 == round(float(r.mse), 4)
        assert 0.037637 == round(float(r.mape), 6)

    def test_bad_data(self, quotes_bad):
        results = indicators.get_sma_analysis(quotes_bad, 15)

        # Assertions
        assert 502 == len(results)

    def test_removed(self, quotes):
        results = indicators.get_sma_analysis(quotes, 20).remove_warmup_periods()

        # Assertions
        assert 502 - 19 == len(results)
        assert 251.8600 == round(float(results[len(results) - 1].sma), 4)

    def test_condense(self, quotes):
        results = indicators.get_sma_analysis(quotes, 20).condense()

        assert 483 == len(results)
        assert 251.8600 == round(float(results[len(results) - 1].sma), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_sma_analysis(quotes, 0)
