import pytest
from stock_indicators import indicators

class TestTripleEMA:
    def test_standard(self, quotes):
        results = indicators.get_triple_ema(quotes, 20)
        
        assert 502 == len(results)
        assert 445 == len(list(filter(lambda x: x.tema is not None, results)))
        
        r = results[67]
        assert 222.9105 == round(float(r.tema), 4)
        
        r = results[249]
        assert 258.6208 == round(float(r.tema), 4)
        
        r = results[501]
        assert 238.7690 == round(float(r.tema), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_triple_ema(bad_quotes, 15)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_triple_ema(quotes, 20).remove_warmup_periods()
        
        assert 502 - (3 * 20 + 100) == len(results)
        
        last = results.pop()
        assert 238.7690 == round(float(last.tema), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_triple_ema(quotes, 0)
