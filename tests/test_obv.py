import pytest
from stock_indicators import indicators

class TestOBV:
    def test_standard(self, quotes):
        results = indicators.get_obv(quotes)
        
        assert 502 == len(results)
        assert 502 == len(list(filter(lambda x: x.obv_sma is None, results)))
        
        r = results[249]
        assert 1780918888 == r.obv
        assert r.obv_sma is None
        
        r = results[501]
        assert 539843504 == r.obv
        assert r.obv_sma is None
        
    def test_with_sma(self, quotes):
        results = indicators.get_obv(quotes, 20)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.obv_sma, results)))
        
        r = results[501]
        assert     539843504 == r.obv
        assert 1016208844.40 == r.obv_sma
        
    # def test_convert_to_quotes(self, quotes):
    #     new_quotes = indicators.get_obv(quotes).to_quotes()
        
    #     assert 502 == len(new_quotes)
        
    #     q = new_quotes[249]
    #     assert 1780918888 == q.close
        
    #     q = new_quotes[501]
    #     assert 539843504 == q.close
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_obv(bad_quotes)
        assert 502 == len(r)
        
    def test_big_data(self, big_quotes):
        r = indicators.get_obv(big_quotes)
        assert 1246 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_obv([])
        assert 0 == len(r)
        
        r = indicators.get_obv(quotes[:1])
        assert 1 == len(r)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_obv(quotes, 0)
