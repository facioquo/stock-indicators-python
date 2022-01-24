import pytest
from stock_indicators import indicators

class TestBollingerBands:
    def test_standard(self, quotes):
        results = indicators.get_bollinger_bands(quotes, 20, 2)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.sma is not None, results)))
        assert 483 == len(list(filter(lambda x: x.upper_band is not None, results)))
        assert 483 == len(list(filter(lambda x: x.lower_band is not None, results)))
        assert 483 == len(list(filter(lambda x: x.percent_b is not None, results)))
        assert 483 == len(list(filter(lambda x: x.z_score is not None, results)))
        assert 483 == len(list(filter(lambda x: x.width is not None, results)))
        
        r = results[249]
        assert 255.5500 == round(float(r.sma), 4)
        assert 259.5642 == round(float(r.upper_band), 4)
        assert 251.5358 == round(float(r.lower_band), 4)
        assert 0.803923 == round(float(r.percent_b), 6)
        assert 1.215692 == round(float(r.z_score), 6)
        assert 0.031416 == round(float(r.width), 6)

        r = results[501]
        assert 251.8600  == round(float(r.sma), 4)
        assert 273.7004  == round(float(r.upper_band), 4)
        assert 230.0196  == round(float(r.lower_band), 4)
        assert 0.349362  == round(float(r.percent_b), 6)
        assert -0.602552 == round(float(r.z_score), 6)
        assert 0.173433  == round(float(r.width), 6)


    def test_bad_data(self, bad_quotes):
        r = indicators.get_bollinger_bands(bad_quotes, 15, 3)

        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_bollinger_bands(quotes, 20, 2).remove_warmup_periods()

        assert 502 -19 == len(results)

        last = results.pop()
        assert 251.8600  == round(float(last.sma), 4)
        assert 273.7004  == round(float(last.upper_band), 4)
        assert 230.0196  == round(float(last.lower_band), 4)
        assert 0.349362  == round(float(last.percent_b), 6)
        assert -0.602552 == round(float(last.z_score), 6)
        assert 0.173433  == round(float(last.width), 6)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_bollinger_bands(quotes, 1)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_bollinger_bands(quotes, 2, 0)
