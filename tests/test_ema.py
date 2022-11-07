import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.chain import IndicatorChain
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.ema import get_ema
from stock_indicators.indicators.rsi import get_rsi
from stock_indicators.indicators.sma import get_sma

class TestEMA:
    def test_standard(self, quotes):
        results = indicators.get_ema(quotes, 20)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.ema is not None, results)))

        r = results[29]
        assert 216.6228 == round(float(r.ema), 4)

        r = results[249]
        assert 255.3873 == round(float(r.ema), 4)

        r = results[501]
        assert 249.3519 == round(float(r.ema), 4)

    def test_custom(self, quotes):
        results = IndicatorChain.use_quotes(quotes, CandlePart.OPEN).add(get_ema, 20).calc()
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.ema is not None, results)))

        r = results[29]
        assert 216.2643 == round(float(r.ema), 4)

        r = results[249]
        assert 255.4875 == round(float(r.ema), 4)

        r = results[501]
        assert 249.9157 == round(float(r.ema), 4)

    def test_chainee(self, quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(get_sma, 2)\
            .add(get_ema, 20)\
            .calc()
            
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.ema is not None, results)))
        
    def test_chainor(self, quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(get_ema, 20)\
            .add(get_sma, 10)\
            .calc()
            
        assert 502 == len(results)
        assert 474 == len(list(filter(lambda x: x.sma is not None, results)))
        
    def test_chaining(self, quotes):
        results = IndicatorChain.use_quotes(quotes).add(get_rsi, 14).add(get_ema, 20).calc()
        
        assert 502 == len(results)
        assert 469 == len(list(filter(lambda x: x.ema is not None, results)))
                
        r = results[32]
        assert r.ema is None

        r = results[33]
        assert 67.4565 == round(float(r.ema), 4)

        r = results[249]
        assert 70.4659 == round(float(r.ema), 4)

        r = results[501]
        assert 37.0728 == round(float(r.ema), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_ema(bad_quotes, 15)

        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_ema([], 10)
        assert 0 == len(r)
        
        r = indicators.get_ema(quotes[:1], 10)
        assert 1 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_ema(quotes, 20).remove_warmup_periods()

        assert 502 - (20 + 100) == len(results)

        last = results.pop()
        assert 249.3519 == round(float(last.ema), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ema(quotes, 0)
