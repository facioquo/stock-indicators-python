import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import EndType

class TestFractal:
    def test_standard_span_2(self, quotes):
        results = indicators.get_fractal(quotes)

        assert 502 == len(results)
        assert  63 == len(list(filter(lambda x: x.fractal_bear is not None, results)))
        assert  71 == len(list(filter(lambda x: x.fractal_bull is not None, results)))

        r = results[1]
        assert r.fractal_bear is None
        assert r.fractal_bull is None

        r = results[3]
        assert 215.17 == round(float(r.fractal_bear), 2)
        assert r.fractal_bull is None

        r = results[133]
        assert 234.53 == round(float(r.fractal_bear), 2)
        assert r.fractal_bull is None

        r = results[180]
        assert 239.74 == round(float(r.fractal_bear), 2)
        assert 238.52 == round(float(r.fractal_bull), 2)

        r = results[250]
        assert r.fractal_bear is None
        assert 256.81 == round(float(r.fractal_bull), 2)

        r = results[500]
        assert r.fractal_bear is None
        assert r.fractal_bull is None


    def test_standard_span_4(self, quotes):
        results = indicators.get_fractal(quotes, 4, 4, EndType.HIGH_LOW)

        assert 502 == len(results)
        assert  35 == len(list(filter(lambda x: x.fractal_bear is not None, results)))
        assert  34 == len(list(filter(lambda x: x.fractal_bull is not None, results)))
        
        r = results[3]
        assert r.fractal_bear is None
        assert r.fractal_bull is None

        r = results[7]
        assert r.fractal_bear is None
        assert 212.53 == round(float(r.fractal_bull), 2)
        
        r = results[120]
        assert 233.02 == round(float(r.fractal_bear), 2)
        assert r.fractal_bull is None

        r = results[180]
        assert 239.74 == round(float(r.fractal_bear), 2)
        assert r.fractal_bull is None

        r = results[250]
        assert r.fractal_bear is None
        assert 256.81 == round(float(r.fractal_bull), 2)

        r = results[500]
        assert r.fractal_bear is None
        assert r.fractal_bull is None

    def test_no_data(self, quotes):
        r = indicators.get_fractal([])
        assert 0 == len(r)

        r = indicators.get_fractal(quotes[:1])
        assert 1 == len(r)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_fractal(bad_quotes)

        assert 502 == len(r)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_fractal(quotes, 1)
