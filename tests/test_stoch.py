import pytest

from stock_indicators import indicators
from stock_indicators.indicators.common.enums import MAType


class TestStoch:
    def test_standard(self, quotes):
        results = indicators.get_stoch(quotes, 14, 3, 3)

        assert 502 == len(results)
        assert 487 == len(list(filter(lambda x: x.oscillator is not None, results)))
        assert 485 == len(list(filter(lambda x: x.signal is not None, results)))

        r = results[15]
        assert 81.1253 == round(float(r.oscillator), 4)
        assert r.signal is None
        assert r.percent_j is None

        r = results[17]
        assert 92.1307 == round(float(r.oscillator), 4)
        assert 88.4995 == round(float(r.signal), 4)
        assert 99.3929 == round(float(r.percent_j), 4)

        r = results[149]
        assert 81.6870 == round(float(r.oscillator), 4)
        assert 79.7935 == round(float(r.signal), 4)
        assert 85.4741 == round(float(r.percent_j), 4)

        r = results[249]
        assert 83.2020 == round(float(r.oscillator), 4)
        assert 83.0813 == round(float(r.signal), 4)
        assert 83.4435 == round(float(r.percent_j), 4)

        r = results[501]
        assert 43.1353 == round(float(r.oscillator), 4)
        assert 35.5674 == round(float(r.signal), 4)
        assert 58.2712 == round(float(r.percent_j), 4)

    def test_extended(self, quotes):
        results = indicators.get_stoch(quotes, 9, 3, 3, 5, 4, MAType.SMMA)

        assert 502 == len(results)
        assert 494 == len(list(filter(lambda x: x.k is not None, results)))
        assert 494 == len(list(filter(lambda x: x.d is not None, results)))

        r = results[7]
        assert r.k is None
        assert r.d is None
        assert r.j is None

        r = results[8]
        assert 81.9178 == round(float(r.k), 4)
        assert 81.9178 == round(float(r.d), 4)
        assert 81.9178 == round(float(r.j), 4)

        r = results[17]
        assert 82.5181 == round(float(r.k), 4)
        assert 76.2603 == round(float(r.d), 4)
        assert 107.5491 == round(float(r.j), 4)

        r = results[149]
        assert 77.1571 == round(float(r.k), 4)
        assert 72.8206 == round(float(r.d), 4)
        assert 94.5030 == round(float(r.j), 4)

        r = results[249]
        assert 74.3652 == round(float(r.k), 4)
        assert 75.5660 == round(float(r.d), 4)
        assert 69.5621 == round(float(r.j), 4)

        r = results[501]
        assert 46.9807 == round(float(r.k), 4)
        assert 32.0413 == round(float(r.d), 4)
        assert 106.7382 == round(float(r.j), 4)

    def test_no_signal(self, quotes):
        results = indicators.get_stoch(quotes, 5, 1, 3)

        r = results[487]
        assert r.oscillator == r.signal
        assert r.k == r.d

        r = results[501]
        assert r.oscillator == r.signal
        assert r.k == r.d

    def test_fast(self, quotes):
        results = indicators.get_stoch(quotes, 5, 10, 1)

        r = results[487]
        assert 25.0353 == round(float(r.oscillator), 4)
        assert 60.5706 == round(float(r.signal), 4)

        r = results[501]
        assert 91.6233 == round(float(r.oscillator), 4)
        assert 36.0608 == round(float(r.signal), 4)

    def test_fast_small(self, quotes):
        results = indicators.get_stoch(quotes, 1, 10, 1)

        r = results[70]
        assert 0 == round(float(r.oscillator), 4)

        r = results[71]
        assert 100 == round(float(r.oscillator), 4)

    def test_bad_data(self, quotes_bad):
        r = indicators.get_stoch(quotes_bad, 15)
        assert 502 == len(r)

    def test_quotes_no(self, quotes):
        r = indicators.get_stoch([])
        assert 0 == len(r)

        r = indicators.get_stoch(quotes[:1])
        assert 1 == len(r)

    def test_boundary(self, quotes):
        results = indicators.get_stoch(quotes, 14, 3, 3)

        assert 0 == len(
            list(filter(lambda x: x.k is not None and (x.k < 0 or x.k > 100), results))
        )
        assert 0 == len(
            list(filter(lambda x: x.d is not None and (x.d < 0 or x.d > 100), results))
        )

    def test_removed(self, quotes):
        results = indicators.get_stoch(quotes, 14, 3, 3).remove_warmup_periods()

        assert 502 - (14 + 3 - 2) == len(results)

        last = results.pop()
        assert 43.1353 == round(float(last.oscillator), 4)
        assert 35.5674 == round(float(last.signal), 4)
        assert 58.2712 == round(float(last.percent_j), 4)

    def test_condense(self, quotes):
        results = indicators.get_stoch(quotes, 14, 3, 3).condense()

        assert 487 == len(results)

        last = results.pop()
        assert 43.1353 == round(float(last.oscillator), 4)
        assert 35.5674 == round(float(last.signal), 4)
        assert 58.2712 == round(float(last.percent_j), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stoch(quotes, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stoch(quotes, 14, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stoch(quotes, 14, 3, 0)
