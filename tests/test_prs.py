import pytest
from stock_indicators import indicators

class TestPRS:
    def test_standard(self, quotes, other_quotes):
        results = indicators.get_prs(other_quotes, quotes, 30, 10)
        
        assert 502 == len(results)
        assert 502 == len(list(filter(lambda x: x.prs is not None, results)))
        assert 493 == len(list(filter(lambda x: x.prs_sma is not None, results)))
        
        r = results[8]
        assert 1.108340 == round(float(r.prs), 6)
        assert r.prs_sma is None
        assert r.prs_percent is None
        
        r = results[249]
        assert  1.222373 == round(float(r.prs), 6)
        assert  1.275808 == round(float(r.prs_sma), 6)
        assert -0.023089 == round(float(r.prs_percent), 6) 
        
        r = results[501]
        assert 1.356817 == round(float(r.prs), 6)
        assert 1.343445 == round(float(r.prs_sma), 6)
        assert 0.037082 == round(float(r.prs_percent), 6) 
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_prs(bad_quotes, bad_quotes, 15, 4)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_prs([], [])
        assert 0 == len(r)
        
        r = indicators.get_prs(quotes[:1], quotes[:1])
        assert 1 == len(r)
        
    def test_exceptions(self, quotes, other_quotes, mismatch_quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_prs(quotes, other_quotes, 0)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_prs(quotes, other_quotes, 14, 0)

        from Skender.Stock.Indicators import InvalidQuotesException
        with pytest.raises(InvalidQuotesException):
            indicators.get_prs(quotes, other_quotes[:13], 14)
            
        with pytest.raises(InvalidQuotesException):
            indicators.get_prs(quotes, other_quotes[:300], 14)
            
        with pytest.raises(InvalidQuotesException):
            indicators.get_prs(mismatch_quotes, other_quotes, 14)