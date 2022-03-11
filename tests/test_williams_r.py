import pytest
from stock_indicators import indicators


class TestWilliamsR:
    def test_standard(self, quotes):
        results = indicators.get_williams_r(quotes, 14)
        
        assert 502 == len(results)
        assert 489 == len(list(filter(lambda x: x.williams_r is not None, results)))
        
        r = results[343]
        assert -19.8211 == round(float(r.williams_r), 4)
        
        r = results[501]
        assert -52.0121 == round(float(r.williams_r), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_williams_r(bad_quotes)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_williams_r([])
        assert 0 == len(r)
        
        r = indicators.get_williams_r(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_williams_r(quotes, 14).remove_warmup_periods()

        assert 502 - 13 == len(results)
        
        last = results.pop()
        assert -52.0121 == round(float(last.williams_r), 4)
                
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_williams_r(quotes, 0)
