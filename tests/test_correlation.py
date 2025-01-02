import pytest

from stock_indicators import indicators


class TestCorrelation:
    def test_standard(self, quotes, quotes_other):
        results = indicators.get_correlation(quotes, quotes_other, 20)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.correlation is not None, results)))

        r = results[18]
        assert r.correlation is None
        assert r.r_squared is None

        r = results[19]
        assert 0.6933 == round(float(r.correlation), 4)
        assert 0.4806 == round(float(r.r_squared), 4)

        r = results[257]
        assert -0.1347 == round(float(r.correlation), 4)
        assert 00.0181 == round(float(r.r_squared), 4)

        r = results[501]
        assert 0.8460 == round(float(r.correlation), 4)
        assert 0.7157 == round(float(r.r_squared), 4)

    def test_bad_data(self, quotes_bad):
        r = indicators.get_correlation(quotes_bad, quotes_bad, 15)
        assert 502 == len(r)

    def test_big_data(self, quotes_big):
        r = indicators.get_correlation(quotes_big, quotes_big, 150)
        assert 1246 == len(r)

    def test_removed(self, quotes, quotes_other):
        results = indicators.get_correlation(quotes, quotes_other, 20)
        results = results.remove_warmup_periods()

        assert 502 - 19 == len(results)

        last = results.pop()
        assert 0.8460 == round(float(last.correlation), 4)
        assert 0.7157 == round(float(last.r_squared), 4)

    def test_condense(self, quotes, quotes_other):
        results = indicators.get_correlation(quotes, quotes_other, 20).condense()

        assert 483 == len(results)

        last = results.pop()
        assert 0.8460 == round(float(last.correlation), 4)
        assert 0.7157 == round(float(last.r_squared), 4)

    def test_exceptions(self, quotes, quotes_other):
        from System import ArgumentOutOfRangeException

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_correlation(quotes, quotes_other, 0)
