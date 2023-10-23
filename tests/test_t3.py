import pytest
from stock_indicators import indicators

class TestT3:
    def test_standard(self, quotes):
        results = indicators.get_t3(quotes, 5, 0.7)
        
        assert 502 == len(results)
        assert 502 == len(list(filter(lambda x: x.t3 is not None, results)))
        
        r = results[5]
        assert 213.9654 == round(float(r.t3), 4)
        
        r = results[24]
        assert 215.9481 == round(float(r.t3), 4)
        
        r = results[44]
        assert 224.9412 == round(float(r.t3), 4)
        
        r = results[149]
        assert 235.8851 == round(float(r.t3), 4)
        
        r = results[249]
        assert 257.8735 == round(float(r.t3), 4)
        
        r = results[501]
        assert 238.9308 == round(float(r.t3), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_t3(bad_quotes)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_t3([])
        assert 0 == len(r)
        
        r = indicators.get_t3(quotes[:1])
        assert 1 == len(r)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_t3(quotes, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_t3(quotes, 25, 0)
