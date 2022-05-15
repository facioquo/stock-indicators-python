import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import Match

class TestDoji:
    def test_standard(self, quotes):
        results = indicators.get_doji(quotes, 0.1)

        assert 502 == len(results)
        assert 112 == len(list(filter(lambda x: x.match != Match.NONE, results)))

        r = results[1]
        assert r.price is None
        assert Match.NONE == r.match

        r = results[23]
        assert 216.28 == round(float(r.price), 2)
        assert Match.NEUTRAL == r.match

        r = results[46]
        assert r.price is None
        assert Match.NONE == r.match

        r = results[34]
        assert r.price is None
        assert Match.NONE == r.match

        r = results[392]
        assert r.price is None
        assert Match.NONE == r.match

        r = results[451]
        assert 273.64 == round(float(r.price), 2)
        assert Match.NEUTRAL == r.match

        r = results[477]
        assert 256.86 == round(float(r.price), 2)
        assert Match.NEUTRAL == r.match

    def test_bad_data(self, bad_quotes):
        r = indicators.get_doji(bad_quotes)
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_doji([])
        assert 0 == len(r)

        r = indicators.get_doji(quotes[:1])
        assert 1 == len(r)

    def test_condense(self, quotes):
        r = indicators.get_doji(quotes, 0.1).condense()
        assert 112 == len(r)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_doji(quotes, -0.001)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_doji(quotes, 0.50001)
