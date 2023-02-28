import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.chain import IndicatorChain

class TestCorrelation:
    def test_standard(self, quotes, other_quotes):
        results = indicators.get_correlation(quotes, other_quotes, 20)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.correlation is not None, results)))
        
        r = results[18]
        assert r.correlation is None
        assert r.r_squared is None
        
        r = results[19]
        assert 0.6933 == round(float(r.correlation), 4)
        assert 0.4806 == round(float(r.r_squared), 4)
        
        r = results[257]
        assert -0.1347 == round(float(r.correlation), 4)
        assert 00.0181 == round(float(r.r_squared), 4)
        
        r = results[501]
        assert 0.8460 == round(float(r.correlation), 4)
        assert 0.7157 == round(float(r.r_squared), 4)
        
    def test_chainor(self, quotes, other_quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_correlation, other_quotes, 20)\
            .add(indicators.get_sma, 10)\
            .calc()

        assert 502 == len(results)
        assert 474 == len(list(filter(lambda x: x.sma is not None, results)))

    def test_chainee(self, quotes, other_quotes):
        sma_results = indicators.get_sma(other_quotes, 2)
        
        results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_sma, 2)\
            .add(indicators.get_correlation, sma_results, 20)\
            .calc()
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.correlation is not None, results)))
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_correlation(bad_quotes, bad_quotes, 15)
        assert 502 == len(r)
        
    def test_big_data(self, big_quotes):
        r = indicators.get_correlation(big_quotes, big_quotes, 150)
        assert 1246 == len(r)
        
    def test_removed(self, quotes, other_quotes):
        results = indicators.get_correlation(quotes, other_quotes, 20)
        results = results.remove_warmup_periods()
        
        assert 502 - 19 == len(results)
        
        last = results.pop()
        assert 0.8460 == round(float(last.correlation), 4)
        assert 0.7157 == round(float(last.r_squared), 4)
        
    def test_exceptions(self, quotes, other_quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_correlation(quotes, other_quotes, 0)
