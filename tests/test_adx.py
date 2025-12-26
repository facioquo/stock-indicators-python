import pytest

from stock_indicators import indicators


class TestAdx:
    def test_standard(self, quotes):
        results = indicators.get_adx(quotes, 14)

        # proper quantities
        # should always be the same number of results as there is quotes
        assert 502 == len(results)
        assert 488 == len(list(filter(lambda x: x.dx is not None, results)))
        assert 475 == len(list(filter(lambda x: x.adx is not None, results)))
        assert 461 == len(list(filter(lambda x: x.adxr is not None, results)))

        # sample values
        r = results[13]
        assert r.pdi is None
        assert r.mdi is None
        assert r.dx is None
        assert r.adx is None

        r = results[14]
        assert 21.9669 == round(float(r.pdi), 4)
        assert 18.5462 == round(float(r.mdi), 4)
        assert 8.4433 == round(float(r.dx), 4)
        assert r.adx is None

        r = results[19]
        assert 21.0361 == round(float(r.pdi), 4)
        assert 25.0124 == round(float(r.mdi), 4)
        assert 8.6351 == round(float(r.dx), 4)
        assert r.adx is None

        r = results[26]
        assert r.adx is None

        r = results[27]
        assert 15.9459 == round(float(r.adx), 4)

        r = results[29]
        assert 37.9719 == round(float(r.pdi), 4)
        assert 14.1658 == round(float(r.mdi), 4)
        assert 45.6600 == round(float(r.dx), 4)
        assert 19.7949 == round(float(r.adx), 4)

        r = results[39]
        assert r.adxr is None

        r = results[40]
        assert r.adxr is None

        r = results[41]
        assert r.adxr is not None

        r = results[248]
        assert 32.3167 == round(float(r.pdi), 4)
        assert 18.2471 == round(float(r.mdi), 4)
        assert 27.8255 == round(float(r.dx), 4)
        assert 30.5903 == round(float(r.adx), 4)
        assert r.adxr is not None

        r = results[501]
        assert 17.7565 == round(float(r.pdi), 4)
        assert 31.1510 == round(float(r.mdi), 4)
        assert 27.3873 == round(float(r.dx), 4)
        assert 34.2987 == round(float(r.adx), 4)
        assert r.adxr is not None

    def test_bad_data(self, quotes_bad):
        results = indicators.get_adx(quotes_bad, 20)

        assert 502 == len(results)

    def test_removed(self, quotes):
        results = indicators.get_adx(quotes).remove_warmup_periods()

        assert 502 - (2 * 14 + 100) == len(results)

        r = results[len(results) - 1]
        assert 17.7565 == round(float(r.pdi), 4)
        assert 31.1510 == round(float(r.mdi), 4)
        assert 34.2987 == round(float(r.adx), 4)

    def test_condense(self, quotes):
        results = indicators.get_adx(quotes, 14).condense()

        assert 475 == len(results)

        r = results[-1]
        assert 17.7565 == round(float(r.pdi), 4)
        assert 31.1510 == round(float(r.mdi), 4)
        assert 34.2987 == round(float(r.adx), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_adx(quotes, 1)
