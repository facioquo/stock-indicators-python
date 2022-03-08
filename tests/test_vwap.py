from datetime import datetime
import pytest
from stock_indicators import indicators

class TestVWAP:
    
    def test_standard(self, intraday_quotes):
        intraday_quotes.sort(key=lambda x: x.date)
        results = indicators.get_vwap(intraday_quotes[:391])
        
        assert 391 == len(results)
        assert 391 == len(list(filter(lambda x: x.vwap is not None, results)))
        
        r = results[0]
        assert 367.4800 == round(float(r.vwap), 4)
        
        r = results[1]
        assert 367.4223 == round(float(r.vwap), 4)
        
        r = results[369]
        assert 367.9494 == round(float(r.vwap), 4)
        
        r = results[390]
        assert 368.1804 == round(float(r.vwap), 4)
        
    def test_with_start_date(self, intraday_quotes):
        intraday_quotes.sort(key=lambda x: x.date)
        year = 2020
        month = 12
        day = 15
        hour = 10
        date = datetime(year, month, day, hour)
        
        results_date = indicators.get_vwap(intraday_quotes[:391], date)
        results_int = indicators.get_vwap(intraday_quotes[:391], year, month, day, hour)
        
        assert 391 == len(results_date) == len(results_int)
        assert 361 == len(list(filter(lambda x: x.vwap is not None, results_date)))
        assert 361 == len(list(filter(lambda x: x.vwap is not None, results_int)))
        
        rd = results_date[29]
        ri = results_int[29]
        assert rd.vwap is None
        assert ri.vwap is None
        
        rd = results_date[30]
        ri = results_int[30]
        assert 366.8100 == round(float(rd.vwap), 4)
        assert 366.8100 == round(float(ri.vwap), 4)
        
        rd = results_date[369]
        ri = results_int[369]
        assert 368.0511 == round(float(rd.vwap), 4)
        assert 368.0511 == round(float(ri.vwap), 4)
        
        rd = results_date[390]
        ri = results_int[390]
        assert 368.2908 == round(float(rd.vwap), 4)
        assert 368.2908 == round(float(ri.vwap), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_vwap(bad_quotes)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_vwap([])
        assert 0 == len(r)
        
        r = indicators.get_vwap(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, intraday_quotes):
        intraday_quotes.sort(key=lambda x: x.date)
        
        results = indicators.get_vwap(intraday_quotes[:391]).remove_warmup_periods()
        
        last = results.pop()
        assert 368.1804 == round(float(last.vwap), 4)
        
        
        year = 2020
        month = 12
        day = 15
        hour = 10
        date = datetime(year, month, day, hour)
        
        results_date = indicators.get_vwap(intraday_quotes[:391], date)
        results_date = results_date.remove_warmup_periods()
        
        results_int = indicators.get_vwap(intraday_quotes[:391], year, month, day, hour)
        results_int = results_int.remove_warmup_periods()
        
        assert 361 == len(results_int) == len(results_date)
        
        last_d = results_date.pop()
        last_i = results_int.pop()
        
        assert 368.2908 == round(float(last_d.vwap), 4)
        assert 368.2908 == round(float(last_i.vwap), 4)
        
    def test_exceptions(self, quotes):
        start_date = datetime(2000, 12, 15)
        
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_vwap(quotes, start_date)
