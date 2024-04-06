import pytest
from stock_indicators import indicators

class TestDynamic:
    def test_standard(self, quotes):
        results = indicators.get_dynamic(quotes, 14)
        
        assert 502 == len(results)
        assert 501 == len(list(filter(lambda x: x.dynamic is not None, results)))
        
        r = results[1]
        assert 212.9465 == round(float(r.dynamic), 4)

        r = results[25]
        assert 215.4801 == round(float(r.dynamic), 4)

        r = results[250]
        assert 256.0554== round(float(r.dynamic), 4)

        r = results[501]
        assert 245.7356 == round(float(r.dynamic), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_dynamic(bad_quotes, 15)
        
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_dynamic([], 14)
        assert 0 == len(r)

        r = indicators.get_dynamic(quotes[:1], 14)
        assert 1 == len(r)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_dynamic(quotes, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_dynamic(quotes, 14, 0)
