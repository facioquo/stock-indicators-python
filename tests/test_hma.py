import pytest

from stock_indicators import indicators


class TestHMA:
    def test_standard(self, quotes):
        results = indicators.get_hma(quotes, 20)

        assert 502 == len(results)
        assert 480 == len(list(filter(lambda x: x.hma is not None, results)))

        r = results[149]
        assert 236.0835 == round(float(r.hma), 4)

        r = results[501]
        assert 235.6972 == round(float(r.hma), 4)

    def test_bad_data(self, quotes_bad):
        r = indicators.get_hma(quotes_bad, 15)
        assert 502 == len(r)

    def test_quotes_no(self, quotes):
        r = indicators.get_hma([], 5)
        assert 0 == len(r)

        r = indicators.get_hma(quotes[:1], 5)
        assert 1 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_hma(quotes, 20).remove_warmup_periods()

        assert 480 == len(results)

        last = results.pop()
        assert 235.6972 == round(float(last.hma), 4)

    def test_condense(self, quotes):
        results = indicators.get_hma(quotes, 20).condense()

        assert 480 == len(results)

        last = results.pop()
        assert 235.6972 == round(float(last.hma), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_hma(quotes, 1)
