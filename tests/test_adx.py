import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.chain import IndicatorChain

class TestAdx:
    def test_standard(self, quotes):
        results = indicators.get_adx(quotes, 14)

        # proper quantities
        # should always be the same number of results as there is quotes
        assert 502 == len(results)
        assert 475 == len(list(filter(lambda x: x.adx is not None, results)))
        assert 462 == len(list(filter(lambda x: x.adxr is not None, results)))

        # sample values
        r = results[19]
        assert 21.0361 == round(float(r.pdi), 4)
        assert 25.0124 == round(float(r.mdi), 4)
        assert r.adx is None

        r  = results[29]
        assert 37.9719 == round(float(r.pdi), 4)
        assert 14.1658 == round(float(r.mdi), 4)
        assert 19.7949 == round(float(r.adx), 4)

        r = results[39]
        assert r.adxr is None

        r = results[40]
        assert 29.1062 == round(float(r.adxr), 4)

        r = results[248]
        assert 32.3167 == round(float(r.pdi), 4)
        assert 18.2471 == round(float(r.mdi), 4)
        assert 30.5903 == round(float(r.adx), 4)
        assert 29.1252 == round(float(r.adxr), 4)

        r = results[501]
        assert 17.7565 == round(float(r.pdi), 4)
        assert 31.1510 == round(float(r.mdi), 4)
        assert 34.2987 == round(float(r.adx), 4)

    def test_chainor(self, quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_adx, 14)\
            .add(indicators.get_sma, 10)\
            .calc()
                
        assert 502 == len(results)
        assert 466 == len(list(filter(lambda x: x.sma is not None, results)))
    
    def test_chainee(self, quotes):
        with pytest.raises(ValueError):
            results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_sma)\
            .add(indicators.get_adx)\
            .calc()

    def test_bad_data(self, bad_quotes):
        results = indicators.get_adx(bad_quotes, 20)

        assert 502 == len(results)

    def test_removed(self, quotes):
        results = indicators.get_adx(quotes).remove_warmup_periods()

        assert 502 - (2 * 14 + 100) == len(results)

        r = results[len(results)-1]
        assert 17.7565 == round(float(r.pdi), 4)
        assert 31.1510 == round(float(r.mdi), 4)
        assert 34.2987 == round(float(r.adx), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_adx(quotes, 1)
