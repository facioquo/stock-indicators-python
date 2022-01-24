import pytest
from stock_indicators import indicators

class TestBeta:
    def test_beta(self, quotes, other_quotes):
        results = indicators.get_beta(quotes, other_quotes, 20)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.beta is not None, results)))

        r = results[501]
        assert 1.6759 == round(float(r.beta), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_beta(bad_quotes, bad_quotes, 20)

        assert 502 == len(r)

    def test_removed(self, quotes, other_quotes):
        results = indicators.get_beta(quotes, other_quotes, 20).remove_warmup_periods()

        assert 502 - 19 == len(results)

        last = results.pop()
        assert 1.6759 == round(float(last.beta), 4)

    def test_same_same(self, quotes):
        results = indicators.get_beta(quotes, quotes, 20)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.beta is not None, results)))

        r = results[501]
        assert 1 == round(float(r.beta), 4)

    def test_exceptions(self, quotes, other_quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_beta(quotes, other_quotes, 0)
