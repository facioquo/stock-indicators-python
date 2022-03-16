import pytest
from stock_indicators import indicators

class TestROC:
    def test_standard(self, quotes):
        results = indicators.get_roc(quotes, 20)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.roc is not None, results)))
        assert 000 == len(list(filter(lambda x: x.roc_sma is not None, results)))
        
        r = results[249]
        assert 2.4827 == round(float(r.roc), 4)
        assert r.roc_sma is None
        
        r = results[501]
        assert -8.2482 == round(float(r.roc), 4)
        assert r.roc_sma is None
        
    def test_with_sma(self, quotes):
        results = indicators.get_roc(quotes, 20, 5)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.roc is not None, results)))
        assert 478 == len(list(filter(lambda x: x.roc_sma is not None, results)))
        
        r = results[29]
        assert 3.2936 == round(float(r.roc), 4)
        assert 2.1558 == round(float(r.roc_sma), 4)
        
        r = results[501]
        assert -8.2482 == round(float(r.roc), 4)
        assert -8.4828 == round(float(r.roc_sma), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_roc(bad_quotes, 35, 2)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_roc(quotes, 20).remove_warmup_periods()
        
        assert 502 - 20 == len(results)
        
        last = results.pop()
        assert -8.2482 == round(float(last.roc), 4)
        assert last.roc_sma is None

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_roc(quotes, 0)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_roc(quotes, 14, 0)
