import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.chain import IndicatorChain

class TestBOP:
    def test_standard(self, quotes):
        results = indicators.get_bop(quotes, 14)
        
        assert 502 == len(results)
        assert 489 == len(list(filter(lambda x: x.bop is not None, results)))
        
        r = results[12]
        assert r.bop is None
        
        r = results[13]
        assert 0.081822 == round(float(r.bop), 6)
        
        r = results[149]
        assert -0.016203 == round(float(r.bop), 6)
        
        r = results[249]
        assert -0.058682 == round(float(r.bop), 6)
        
        r = results[501]
        assert -0.292788 == round(float(r.bop), 6)

    def test_chainor(self, quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_bop, 14)\
            .add(indicators.get_sma, 10)\
            .calc()

        assert 502 == len(results)
        assert 480 == len(list(filter(lambda x: x.sma is not None, results)))

    def test_chainee(self, quotes):
        with pytest.raises(ValueError):
            results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_sma)\
            .add(indicators.get_bop)\
            .calc()

    def test_bad_data(self, bad_quotes):
        r = indicators.get_bop(bad_quotes)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_bop(quotes).remove_warmup_periods()
        
        assert 502 - 13 == len(results)
        
        last = results.pop()
        assert -0.292788 == round(float(last.bop), 6)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_bop(quotes, 0)
