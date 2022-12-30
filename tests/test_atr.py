import pytest
from stock_indicators import indicators

class TestATR:
    def test_standard(self, quotes):
        results = indicators.get_atr(quotes, 14)

        assert 502 == len(results)
        assert 488 == len(list(filter(lambda x: x.atr, results)))

        r = results[13]
        assert 1.4500 == round(float(r.tr), 2)
        assert r.atr is None
        assert r.atrp is None

        r = results[14]
        assert 1.8200 == round(float(r.tr), 4)
        assert 1.3364 == round(float(r.atr), 4)
        assert 0.6215 == round(float(r.atrp), 4)

        r = results[24]
        assert 0.8800 == round(float(r.tr), 4)
        assert 1.3034 == round(float(r.atr), 4)
        assert 0.6026 == round(float(r.atrp), 4)

        r = results[249]
        assert 0.5800 == round(float(r.tr), 4)
        assert 1.3381 == round(float(r.atr), 4)
        assert 0.5187 == round(float(r.atrp), 4)

        r = results[501]
        assert 2.6700 == round(float(r.tr), 4)
        assert 6.1497 == round(float(r.atr), 4)
        assert 2.5072 == round(float(r.atrp), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_atr(bad_quotes, 20)

        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_atr(quotes, 14).remove_warmup_periods()

        assert 488 == len(results)

        last = results.pop()
        assert 2.6700 == round(float(last.tr), 4)
        assert 6.1497 == round(float(last.atr), 4)
        assert 2.5072 == round(float(last.atrp), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_atr(quotes, 1)
