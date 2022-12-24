import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.chain import IndicatorChain

class TestAwesome:
    def test_standard(self, quotes):
        results = indicators.get_awesome(quotes, 5, 34)

        assert 502 == len(results)
        assert 469 == len(list(filter(lambda x: x.oscillator is not None,results)))

        r = results[32]
        assert r.oscillator is None
        assert r.normalized is None

        r = results[33]
        assert 5.4756 == round(float(r.oscillator), 4)
        assert 2.4548 == round(float(r.normalized), 4)

        r = results[249]
        assert 5.0618 == round(float(r.oscillator), 4)
        assert 1.9634 == round(float(r.normalized), 4)

        r = results[501]
        assert -17.7692 == round(float(r.oscillator), 4)
        assert -7.2763  == round(float(r.normalized), 4)

    def test_chainor(self, quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_awesome)\
            .add(indicators.get_sma, 10)\
            .calc()
                
        assert 502 == len(results)
        assert 460 == len(list(filter(lambda x: x.sma is not None, results)))
    
    def test_chainee(self, quotes):
        results = IndicatorChain.use_quotes(quotes)\
            .add(indicators.get_sma, 2)\
            .add(indicators.get_awesome)\
            .calc()
        
        assert 502 == len(results)
        assert 468 == len(list(filter(lambda x: x.oscillator is not None, results)))

    def test_bad_data(self, bad_quotes):
        r = indicators.get_awesome(bad_quotes, 5, 34)

        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_awesome(quotes, 5, 34).remove_warmup_periods()

        assert 502 - 33 == len(results)

        last = results.pop()
        assert -17.7692 == round(float(last.oscillator), 4)
        assert -7.2763  == round(float(last.normalized), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_awesome(quotes, 0, 34)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_awesome(quotes, 25, 25)
