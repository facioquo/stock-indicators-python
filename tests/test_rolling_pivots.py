import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import PivotPointType

class TestPivotPoints:
    def test_standard(self, quotes):
        results = indicators.get_rolling_pivots(quotes, 11, 9, PivotPointType.STANDARD)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.pp is not None, results)))
        
        r = results[19]
        assert r.pp is None
        assert r.s1 is None
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        assert r.r1 is None
        assert r.r2 is None
        assert r.r3 is None
        assert r.r4 is None
        
        r = results[20]
        assert 213.6367 == round(float(r.pp), 4)
        assert 212.1033 == round(float(r.s1), 4)
        assert 209.9867 == round(float(r.s2), 4)
        assert 208.4533 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 215.7533 == round(float(r.r1), 4)
        assert 217.2867 == round(float(r.r2), 4)
        assert 219.4033 == round(float(r.r3), 4)
        assert r.r4 is None
        
        r = results[149]
        assert 233.6333 == round(float(r.pp), 4)
        assert 231.3567 == round(float(r.s1), 4)
        assert 227.3733 == round(float(r.s2), 4)
        assert 225.0967 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 237.6167 == round(float(r.r1), 4)
        assert 239.8933 == round(float(r.r2), 4)
        assert 243.8767 == round(float(r.r3), 4)
        assert r.r4 is None
        
        r = results[249]
        assert 253.9533 == round(float(r.pp), 4)
        assert 251.5267 == round(float(r.s1), 4)
        assert 247.4433 == round(float(r.s2), 4)
        assert 245.0167 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 258.0367 == round(float(r.r1), 4)
        assert 260.4633 == round(float(r.r2), 4)
        assert 264.5467 == round(float(r.r3), 4)
        assert r.r4 is None
        
        r = results[501]
        assert 260.0267 == round(float(r.pp), 4)
        assert 246.4633 == round(float(r.s1), 4)
        assert 238.7767 == round(float(r.s2), 4)
        assert 225.2133 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 267.7133 == round(float(r.r1), 4)
        assert 281.2767 == round(float(r.r2), 4)
        assert 288.9633 == round(float(r.r3), 4)
        assert r.r4 is None
        
    def test_camarilla(self, quotes):
        results = indicators.get_rolling_pivots(quotes[:38], 10, 0, PivotPointType.CAMARILLA)
        
        assert 38 == len(results)
        assert 28 == len(list(filter(lambda x: x.pp is not None, results)))
        
        r = results[9]
        assert r.pp is None
        assert r.s1 is None
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        assert r.r1 is None
        assert r.r2 is None
        assert r.r3 is None
        assert r.r4 is None
        
        r = results[10]
        assert 267.0800 == round(float(r.pp), 4)
        assert 265.8095 == round(float(r.s1), 5)
        assert 264.5390 == round(float(r.s2), 4)
        assert 263.2685 == round(float(r.s3), 4)
        assert 259.4570 == round(float(r.s4), 4)
        assert 268.3505 == round(float(r.r1), 4)
        assert 269.6210 == round(float(r.r2), 4)
        assert 270.8915 == round(float(r.r3), 5)
        assert 274.7030 == round(float(r.r4), 4)
        
        r = results[22]
        assert 263.2900 == round(float(r.pp), 4)
        assert 261.6840 == round(float(r.s1), 4)
        assert 260.0780 == round(float(r.s2), 4)
        assert 258.4720 == round(float(r.s3), 4)
        assert 253.6540 == round(float(r.s4), 4)
        assert 264.8960 == round(float(r.r1), 4)
        assert 266.5020 == round(float(r.r2), 4)
        assert 268.1080 == round(float(r.r3), 4)
        assert 272.9260 == round(float(r.r4), 4)
        
        r = results[23]
        assert 257.1700 == round(float(r.pp), 4)
        assert 255.5640 == round(float(r.s1), 4)
        assert 253.9580 == round(float(r.s2), 4)
        assert 252.3520 == round(float(r.s3), 4)
        assert 247.5340 == round(float(r.s4), 4)
        assert 258.7760 == round(float(r.r1), 4)
        assert 260.3820 == round(float(r.r2), 4)
        assert 261.9880 == round(float(r.r3), 4)
        assert 266.8060 == round(float(r.r4), 4)
        
        r = results[37]
        assert 243.1500 == round(float(r.pp), 4)
        assert 240.5650 == round(float(r.s1), 5)
        assert 237.9800 == round(float(r.s2), 4)
        assert 235.3950 == float(round(r.s3, 4))
        assert 227.6400 == round(float(r.s4), 4)
        assert 245.7350 == round(float(r.r1), 4)
        assert 248.3200 == round(float(r.r2), 4)
        assert 250.9050 == round(float(r.r3), 5)
        assert 258.6600 == round(float(r.r4), 4)
        
    def test_demark(self, quotes):
        results = indicators.get_rolling_pivots(quotes, 10, 10, PivotPointType.DEMARK)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.pp is not None, results)))
        
        r = results[19]
        assert r.pp is None
        assert r.s1 is None
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        assert r.r1 is None
        assert r.r2 is None
        assert r.r3 is None
        assert r.r4 is None
        
        r = results[20]
        assert 212.9900 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 214.4600 == float(round(r.r1, 4))
        assert 210.8100 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
        r = results[149]
        assert 232.6525 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 235.6550 == float(round(r.r1, 4))
        assert 229.3950 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
        r = results[250]
        assert 252.9325 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 255.9950 == float(round(r.r1, 4))
        assert 249.4850 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
        r = results[251]
        assert 252.6700 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 255.4700 == float(round(r.r1, 4))
        assert 248.9600 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
        r = results[501]
        assert 264.6125 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 276.8850 == float(round(r.r1, 4))
        assert 255.6350 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
    def test_fibonacci(self, intraday_quotes):
        results = indicators.get_rolling_pivots(intraday_quotes[:300], 44, 15, PivotPointType.FIBONACCI)
        
        assert 300 == len(results)
        assert 241 == len(list(filter(lambda x: x.pp is not None, results)))
        
        r = results[58]
        assert r.pp is None
        assert r.s1 is None
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        assert r.r1 is None
        assert r.r2 is None
        assert r.r3 is None
        assert r.r4 is None
        
        r = results[59]
        assert 368.4283 == float(round(r.pp, 4))
        assert 367.8553 == float(round(r.s1, 4))
        assert 367.5013 == float(round(r.s2, 4))
        assert 366.9283 == float(round(r.s3, 4))
        assert 369.0013 == float(round(r.r1, 4))
        assert 369.3553 == float(round(r.r2, 4))
        assert 369.9283 == float(round(r.r3, 4))
        
        r = results[118]
        assert 369.1573 == float(round(r.pp, 4))
        assert 368.7333 == float(round(r.s1, 4))
        assert 368.4713 == float(round(r.s2, 4))
        assert 368.0473 == float(round(r.s3, 4))
        assert 369.5813 == float(round(r.r1, 4))
        assert 369.8433 == float(round(r.r2, 4))
        assert 370.2673 == float(round(r.r3, 4))
        
        r = results[119]
        assert 369.1533 == float(round(r.pp, 4))
        assert 368.7293 == float(round(r.s1, 4))
        assert 368.4674 == float(round(r.s2, 4))
        assert 368.0433 == float(round(r.s3, 4))
        assert 369.5774 == float(round(r.r1, 4))
        assert 369.8393 == float(round(r.r2, 4))
        assert 370.2633 == float(round(r.r3, 4))
        
        r = results[149]
        assert 369.0183 == float(round(r.pp, 4))
        assert 368.6593 == float(round(r.s1, 4))
        assert 368.4374 == float(round(r.s2, 4))
        assert 368.0783 == float(round(r.s3, 4))
        assert 369.3774 == float(round(r.r1, 4))
        assert 369.5993 == float(round(r.r2, 4))
        assert 369.9583 == float(round(r.r3, 4))
        
        r = results[299]
        assert 367.7567 == float(round(r.pp, 4))
        assert 367.3174 == float(round(r.s1, 4))
        assert 367.0460 == float(round(r.s2, 4))
        assert 366.6067 == float(round(r.s3, 4))
        assert 368.1960 == float(round(r.r1, 4))
        assert 368.4674 == float(round(r.r2, 4))
        assert 368.9067 == float(round(r.r3, 4))
        
    def test_woodie(self, intraday_quotes):
        results = indicators.get_rolling_pivots(intraday_quotes, 375, 16, PivotPointType.WOODIE)
        
        assert 1564 == len(results)
        assert 1173 == len(list(filter(lambda x: x.pp is not None, results)))
        
        r = results[390]
        assert r.pp is None
        assert r.s1 is None
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        assert r.r1 is None
        assert r.r2 is None
        assert r.r3 is None
        assert r.r4 is None
        
        r = results[391]
        assert 368.7850 == float(round(r.pp, 4))
        assert 367.9901 == float(round(r.s1, 4))
        assert 365.1252 == float(round(r.s2, 4))
        assert 364.3303 == float(round(r.s3, 4))
        assert 371.6499 == float(round(r.r1, 4))
        assert 372.4448 == float(round(r.r2, 4))
        assert 375.3097 == float(round(r.r3, 4))
        
        r = results[1172]
        assert 371.7500 == float(round(r.pp, 4))
        assert 371.0400 == float(round(r.s1, 4))
        assert 369.3500 == float(round(r.s2, 4))
        assert 368.6400 == float(round(r.s3, 4))
        assert 373.4400 == float(round(r.r1, 4))
        assert 374.1500 == float(round(r.r2, 4))
        assert 375.8400 == float(round(r.r3, 4))
        
        r = results[1173]
        assert 371.3625 == float(round(r.pp, 4))
        assert 370.2650 == float(round(r.s1, 4))
        assert 369.9525 == float(round(r.s2, 4))
        assert 368.8550 == float(round(r.s3, 4))
        assert 371.6750 == float(round(r.r1, 4))
        assert 372.7725 == float(round(r.r2, 4))
        assert 373.0850 == float(round(r.r3, 4))
        
        r = results[1563]
        assert 369.3800 == float(round(r.pp, 4))
        assert 366.5200 == float(round(r.s1, 4))
        assert 364.1600 == float(round(r.s2, 4))
        assert 361.3000 == float(round(r.s3, 4))
        assert 371.7400 == float(round(r.r1, 4))
        assert 374.6000 == float(round(r.r2, 4))
        assert 376.9600 == float(round(r.r3, 4))
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_rolling_pivots(bad_quotes, 5, 5)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_rolling_pivots([], 5, 2)
        assert 0 == len(r)
        
        r = indicators.get_rolling_pivots(quotes[:1], 5, 2)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        window_periods = 11
        offset_periods = 9
        results = indicators.get_rolling_pivots(quotes, window_periods, offset_periods, PivotPointType.STANDARD)
        results = results.remove_warmup_periods()
        
        assert 502 - (window_periods + offset_periods) == len(results)   
        
        last = results.pop()
        assert 260.0267 == round(float(last.pp), 4)
        assert 246.4633 == round(float(last.s1), 4)
        assert 238.7767 == round(float(last.s2), 4)
        assert 225.2133 == round(float(last.s3), 4)
        assert last.s4 is None
        assert 267.7133 == round(float(last.r1), 4)
        assert 281.2767 == round(float(last.r2), 4)
        assert 288.9633 == round(float(last.r3), 4)
        assert last.r4 is None
           
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_rolling_pivots(quotes, 0, 10)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_rolling_pivots(quotes, 10, -1)
