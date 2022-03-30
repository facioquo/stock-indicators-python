import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import EndType, PivotTrend

class TestPivots:
    def test_standard(self, quotes):
        results = indicators.get_pivots(quotes, 4, 4, 20, EndType.HIGH_LOW)
        
        assert 502 == len(results)
        assert  35 == len(list(filter(lambda x: x.high_point is not None, results)))
        assert 333 == len(list(filter(lambda x: x.high_trend is not None, results)))
        assert 338 == len(list(filter(lambda x: x.high_line is not None, results)))
        assert  34 == len(list(filter(lambda x: x.low_point is not None, results)))
        assert 328 == len(list(filter(lambda x: x.low_trend is not None, results)))
        assert 333 == len(list(filter(lambda x: x.low_line is not None, results)))

        r = results[3]
        assert r.high_point is None
        assert r.high_trend is None
        assert r.high_line is None
        assert r.low_point is None
        assert r.low_trend is None
        assert r.low_line is None
        
        r = results[7]
        assert r.high_point is None
        assert r.high_trend is None
        assert r.high_line is None
        assert 212.53 == float(round(r.low_point, 2))
        assert r.low_trend is None
        assert 212.53 == float(round(r.low_line, 2))
        
        r = results[120]
        assert 233.02 == float(round(r.high_point, 2))
        assert r.high_trend == PivotTrend.LH
        assert 233.02 == float(round(r.high_point, 2))
        assert r.low_point is None
        assert r.low_trend == PivotTrend.LL
        assert 228.9671 == float(round(r.low_line, 4))
        
        r = results[180]
        assert 239.74 == float(round(r.high_point, 2))
        assert r.high_trend == PivotTrend.HH
        assert 239.74 == float(round(r.high_line, 2))
        assert r.low_point is None
        assert r.low_trend == PivotTrend.HL
        assert 236.7050 == float(round(r.low_line, 4))
        
        r = results[250]
        assert r.high_point is None
        assert r.high_trend is None
        assert r.high_line is None
        assert 256.81 == float(round(r.low_point, 2))
        assert r.low_trend is None
        assert r.low_line is None
        
        r = results[472]
        assert r.high_point is None
        assert r.high_trend == PivotTrend.LH
        assert 274.14 == float(round(r.high_line, 2))
        assert r.low_point is None
        assert r.low_trend == PivotTrend.HL
        assert 255.8078 == float(round(r.low_line, 4))
        
        r = results[497]
        assert r.high_point is None
        assert r.high_trend is None
        assert r.high_line is None
        assert r.low_point is None
        assert r.low_trend is None
        assert r.low_line is None
        
        r = results[498]
        assert r.high_point is None
        assert r.high_trend is None
        assert r.high_line is None
        assert r.low_point is None
        assert r.low_trend is None
        assert r.low_line is None
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_pivots(bad_quotes)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_pivots([])
        assert 0 == len(r)
        
        r = indicators.get_pivots(quotes[:1])
        assert 1 == len(r)
    
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pivots(quotes, 1)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pivots(quotes, 2, 1)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pivots(quotes, 20, 10, 20, EndType.CLOSE)
