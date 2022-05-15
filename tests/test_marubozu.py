import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import Match

class TestMarubozu:
    def test_standard(self, quotes):
        results = indicators.get_marubozu(quotes, 0.95)

        assert 502 == len(results)
        assert 6 == len(list(filter(lambda x: x.Match != Match.NONE, results)))

        r = results[31]
        assert r.price is None
        assert r.Match == Match.NONE

        r = results[32]
        assert 222.10 == round(float(r.price), 2)
        assert Match.BULL_SIGNAL == r.Match

        r = results[33]
        assert r.price is None
        assert Match.NONE == r.Match

        r = results[34]
        assert r.price is None
        assert Match.NONE == r.Match

        r = results[274]
        assert r.price is None
        assert Match.NONE == r.Match

        r = results[277]
        assert 248.13 == round(float(r.price), 2)
        assert Match.BEAR_SIGNAL == r.Match

    def test_bad_data(self, bad_quotes):
        r = indicators.get_marubozu(bad_quotes)
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_marubozu([])
        assert 0 == len(r)

        r = indicators.get_marubozu(quotes[:1])
        assert 1 == len(r)

    def test_condense(self, quotes):
        r = indicators.get_marubozu(quotes, 0.95).condense()
        assert 6 == len(r)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_marubozu(quotes, 0.799)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_marubozu(quotes, 1.001)
