from datetime import datetime
import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import CandlePart

class TestSMA:    
    def test_standard(self, quotes):
        results = indicators.get_sma(quotes, 20)

        # proper quantities
        # should always be the same number of results as there is quotes
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.sma is not None, results)))

        # sample values
        assert results[18].sma is None
        assert 214.5250 == round(float(results[19].sma), 4)
        assert 215.0310 == round(float(results[24].sma), 4)
        assert 234.9350 == round(float(results[149].sma), 4)
        assert 255.5500 == round(float(results[249].sma), 4)
        assert 251.8600 == round(float(results[501].sma), 4)

    def test_open_candle_part(self, quotes):
        results = indicators.get_sma(quotes, 20 , CandlePart.OPEN)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.sma is not None, results)))

        # sample values
        assert results[18].sma is None
        assert 214.3795 == round(float(results[19].sma), 4)
        assert 214.9535 == round(float(results[24].sma), 4)
        assert 234.8280 == round(float(results[149].sma), 4)
        assert 255.6915 == round(float(results[249].sma), 4)
        assert 253.1725 == round(float(results[501].sma), 4)

    def test_volume_candle_part(self, quotes):
        results = indicators.get_sma(quotes, 20 , CandlePart.VOLUME)
        
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.sma is not None, results)))

        # sample values
        r = results[24]
        assert 77293768.2 == round(float(r.sma), 1)
        
        r = results[290]
        assert 157958070.8 == round(float(r.sma), 1)
        
        r = results[501]
        assert datetime(2018, 12, 31) == r.date
        assert 163695200 == round(float(r.sma), 0)

    def test_bad_data(self, bad_quotes):
        results = indicators.get_sma(bad_quotes, 15)
        assert 502 == len(results)

    def test_no_quotes(self, quotes):
        r = indicators.get_sma([], 5)
        assert 0 == len(r)
        
        r = indicators.get_sma(quotes[:1], 5)
        assert 1 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_sma(quotes, 20).remove_warmup_periods()

        assert 502 - 19 == len(results)
        assert 251.8600 == round(float(results[len(results)-1].sma), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_sma(quotes, 0)
