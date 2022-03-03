import pytest
from stock_indicators import indicators

class TestVortex:
    def test_standard(self, quotes):
        results = indicators.get_vortex(quotes, 14)
        
        assert 502 == len(results)
        assert 488 == len(list(filter(lambda x: x.pvi is not None, results)))
        
        r = results[13]
        assert r.pvi is None
        assert r.nvi is None
        
        r = results[14]
        assert 1.0460 == round(float(r.pvi), 4)
        assert 0.8119 == round(float(r.nvi), 4)
        
        r = results[29]
        assert 1.1300 == round(float(r.pvi), 4)
        assert 0.7393 == round(float(r.nvi), 4)
        
        r = results[249]
        assert 1.1558 == round(float(r.pvi), 4)
        assert 0.6634 == round(float(r.nvi), 4)
        
        r = results[501]
        assert 0.8712 == round(float(r.pvi), 4)
        assert 1.1163 == round(float(r.nvi), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_vortex(bad_quotes, 20)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_vortex([], 5)
        assert 0 == len(r)
        
        r = indicators.get_vortex(quotes[:1], 5)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_vortex(quotes, 14)
        results = results.remove_warmup_periods()
        
        assert 502 - 14 == len(results)
        
        last = results.pop()
        assert 0.8712 == round(float(last.pvi), 4)
        assert 1.1163 == round(float(last.nvi), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_vortex(quotes, 1)
