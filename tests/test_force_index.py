import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.chain import IndicatorChain

class TestForceIndex:
    def test_standard(self, quotes):
        r = indicators.get_force_index(quotes, 13)
        
        assert 502 == len(r)
        assert 489 == len(list(filter(lambda x: x.force_index is not None, r)))
        
        assert r[12].force_index is None
        
        assert  10668240.778 == round(float(r[13].force_index), 3)
        assert  15883211.364 == round(float(r[24].force_index), 3)
        assert   7598218.196 == round(float(r[149].force_index), 3)
        assert  23612118.994 == round(float(r[249].force_index), 3)
        assert -16824018.428 == round(float(r[501].force_index), 3)

    def test_chainor(self, quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_force_index, 13)\
            .add(indicators.get_sma, 10)\
            .calc()

        assert 502 == len(results)
        assert 480 == len(list(filter(lambda x: x.sma is not None, results)))

    def test_chainee(self, quotes):
        with pytest.raises(ValueError):
            results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_sma)\
            .add(indicators.get_force_index, 10)\
            .calc()

    def test_bad_data(self, bad_quotes):
        r = indicators.get_force_index(bad_quotes, 2)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_force_index([], 5)
        assert 0 == len(r)
        
        r = indicators.get_force_index(quotes[:1], 5)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_force_index(quotes, 13).remove_warmup_periods()
        
        assert 502 - (13 + 100) == len(results)
        
        last = results.pop()
        assert -16824018.428 == round(float(last.force_index), 3)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_force_index(quotes, 0)
