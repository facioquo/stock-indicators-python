import pytest
from stock_indicators import indicators

class TestDPO:
    def test_standard(self, quotes):
        results = indicators.get_dpo(quotes, 14)
        
        assert 502 == len(results)
        assert 489 == len(list(filter(lambda x: x.dpo is not None, results)))
        
        r = results[51]
        assert   1.3264 == round(float(r.dpo), 4)
        assert 223.5836 == round(float(r.sma), 4)
        
        r = results[249]
        assert  -1.9307 == round(float(r.dpo), 4)
        assert 259.9207 == round(float(r.sma), 4)
        
        r = results[501]
        assert r.dpo is None
        assert r.sma is None
        
    # def test_to_quotes(self, quotes):
    #     new_quotes = indicators.get_dpo(quotes, 14).to_quotes()
        
    #     assert 489 == len(new_quotes)
        
    #     q = new_quotes.pop()
    #     assert 2.18214 == round(float(q.close), 5)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_dpo(bad_quotes, 5)
        
        assert 502 == len(r)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_dpo(quotes, 0)
