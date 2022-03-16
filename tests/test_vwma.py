import pytest
from stock_indicators import indicators


class TestVWMA:
    def test_standard(self, quotes):
        results = indicators.get_vwma(quotes, 10)
        
        assert 502 == len(results)
        assert 493 == len(list(filter(lambda x: x.vwma is not None, results)))
        
        r = results[8]
        assert r.vwma is None
        
        r = results[9]
        assert 213.981942 == round(float(r.vwma), 6)
        
        r = results[24]
        assert 215.899211 == round(float(r.vwma), 6)
        
        r = results[99]
        assert 226.302760 == round(float(r.vwma), 6)
        
        r = results[249]
        assert 257.053654 == round(float(r.vwma), 6)
        
        r = results[501]
        assert 242.101548 == round(float(r.vwma), 6)
        
    def test_bad_data(self, quotes):
        r = indicators.get_vwma(quotes, 15)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_vwma([], 4)
        assert 0 == len(r)
        
        r = indicators.get_vwma(quotes[:1], 4)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_vwma(quotes, 10).remove_warmup_periods()
        
        assert 502 - 9 == len(results)
        
        last = results.pop()
        assert 242.101548 == round(float(last.vwma), 6)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_vwma(quotes, 0)
