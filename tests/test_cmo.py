import pytest
from stock_indicators import indicators

class TestCMO:
    def test_standard(self, quotes):
        results = indicators.get_cmo(quotes, 14)
        
        assert 502 == len(results)
        assert 488 == len(list(filter(lambda x: x.cmo is not None, results)))
        
        r = results[13]
        assert r.cmo is None

        r = results[14]
        assert 24.1081 == round(float(r.cmo), 4)

        r = results[249]
        assert 48.9614 == round(float(r.cmo), 4)

        r = results[501]
        assert -26.7502 == round(float(r.cmo), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_cmo(bad_quotes, 15)
        
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_cmo([], 5)
        assert 0 == len(r)

        r = indicators.get_cmo(quotes[:1], 5)
        assert 1 == len(r)
   
    def test_removed(self, quotes):
        results = indicators.get_cmo(quotes, 14).remove_warmup_periods()
        
        assert 488 == len(results)
        
        last = results.pop()
        assert -26.7502 == round(float(last.cmo), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_cmo(quotes, 0)
