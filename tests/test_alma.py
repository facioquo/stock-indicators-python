import pytest
from stock_indicators import indicators

class TestALMA:
    def test_standard(self, quotes):
        results = indicators.get_alma(quotes, lookback_periods=10, offset= .85, sigma=6)

        # assertions

        # proper quantities
        # should always be the same number of results as there is quotes
        r = results[8]
        assert r.alma is None 

        r = results[9]
        assert 214.1839 == round(float(r.alma), 4)

        r = results[24]
        assert 216.0619 == round(float(r.alma), 4)

        r = results[149]
        assert 235.8609 == round(float(r.alma), 4)

        r = results[249]
        assert 257.5787 == round(float(r.alma), 4)

        r = results[501]
        assert 242.1871 == round(float(r.alma), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_alma(bad_quotes, 14, .5, 3)

        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_alma(quotes, 10, .85, 6).remove_warmup_periods()

        assert 502 - 9 == len(results)
        
        last = results.pop()
        assert 242.1871 == round(float(last.alma), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_alma(quotes, 0, 1, 5)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_alma(quotes, 15, 1.1, 3)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_alma(quotes, 10, .5, 0)
