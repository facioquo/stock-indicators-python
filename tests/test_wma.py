import pytest
from stock_indicators import indicators


class TestWMA:
    def test_standard(self, quotes):
        results = indicators.get_wma(quotes, 20)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.wma is not None, results)))
        
        r = results[149]
        assert 235.5253 == round(float(r.wma), 4)
        
        r = results[501]
        assert 246.5110 == round(float(r.wma), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_wma(bad_quotes, 15)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_wma([], 5)
        assert 0 == len(r)
        
        r = indicators.get_wma(quotes[:1], 5)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_wma(quotes, 20).remove_warmup_periods()

        assert 502 - 19 == len(results)
        
        last = results.pop()
        assert 246.5110 == round(float(last.wma), 4)
                
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_wma(quotes, 0)
