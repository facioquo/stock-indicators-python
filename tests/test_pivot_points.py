import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import PeriodSize, PivotPointType

class TestPivotPoints:
    def test_standard(self, quotes):
        results = indicators.get_pivot_points(quotes, PeriodSize.MONTH, PivotPointType.STANDARD)
        
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
        assert 214.5000 == round(float(r.pp), 4)
        assert 211.9800 == round(float(r.s1), 4)
        assert 209.0000 == round(float(r.s2), 4)
        assert 206.4800 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 217.4800 == round(float(r.r1), 4)
        assert 220.0000 == round(float(r.r2), 4)
        assert 222.9800 == round(float(r.r3), 4)
        assert r.r4 is None
        
        r = results[149]
        assert 233.6400 == round(float(r.pp), 4)
        assert 230.8100 == round(float(r.s1), 4)
        assert 226.3300 == round(float(r.s2), 4)
        assert 223.5000 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 238.1200 == round(float(r.r1), 4)
        assert 240.9500 == round(float(r.r2), 4)
        assert 245.4300 == round(float(r.r3), 4)
        assert r.r4 is None
        
        r = results[250]
        assert 251.2767 == round(float(r.pp), 4)
        assert 247.6133 == round(float(r.s1), 4)
        assert 241.2867 == round(float(r.s2), 4)
        assert 237.6233 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 257.6033 == round(float(r.r1), 4)
        assert 261.2667 == round(float(r.r2), 4)
        assert 267.5933 == round(float(r.r3), 4)
        assert r.r4 is None
        
        r = results[251]
        assert 255.1967 == round(float(r.pp), 4)
        assert 251.6933 == round(float(r.s1), 4)
        assert 246.3667 == round(float(r.s2), 4)
        assert 242.8633 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 260.5233 == round(float(r.r1), 4)
        assert 264.0267 == round(float(r.r2), 4)
        assert 269.3533 == round(float(r.r3), 4)
        assert r.r4 is None
        
        r = results[501]
        assert 266.6767 == round(float(r.pp), 4)
        assert 258.9633 == round(float(r.s1), 4)
        assert 248.9667 == round(float(r.s2), 4)
        assert 241.2533 == round(float(r.s3), 4)
        assert r.s4 is None
        assert 276.6733 == round(float(r.r1), 4)
        assert 284.3867 == round(float(r.r2), 4)
        assert 294.3833 == round(float(r.r3), 4)
        assert r.r4 is None
        
    def test_camarilla(self, quotes):
        results = indicators.get_pivot_points(quotes[:38], PeriodSize.WEEK, PivotPointType.CAMARILLA)
        
        assert 38 == len(results)
        assert 33 == len(list(filter(lambda x: x.pp is not None, results)))
        
        r = results[4]
        assert r.pp is None
        assert r.s1 is None
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        assert r.r1 is None
        assert r.r2 is None
        assert r.r3 is None
        assert r.r4 is None
        
        r = results[5]
        assert  271.0200 == round(float(r.pp), 4)
        assert 270.13725 == round(float(r.s1), 5)
        assert  269.2545 == round(float(r.s2), 4)
        assert  268.3718 == round(float(r.s3), 4)
        assert  265.7235 == round(float(r.s4), 4)
        assert  271.9028 == round(float(r.r1), 4)
        assert  272.7855 == round(float(r.r2), 4)
        assert 273.66825 == round(float(r.r3), 5)
        assert  276.3165 == round(float(r.r4), 4)
        
        r = results[22]
        assert  268.9600 == round(float(r.pp), 4)
        assert  267.9819 == round(float(r.s1), 4)
        assert  267.0038 == round(float(r.s2), 4)
        assert  266.0258 == round(float(r.s3), 4)
        assert  263.0915 == round(float(r.s4), 4)
        assert  269.9381 == round(float(r.r1), 4)
        assert  270.9162 == round(float(r.r2), 4)
        assert 271.89425 == round(float(r.r3), 5)
        assert  274.8285 == round(float(r.r4), 4)
        
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
        assert  243.1500 == round(float(r.pp), 4)
        assert 241.56325 == round(float(r.s1), 5)
        assert  239.9765 == round(float(r.s2), 4)
        assert  238.3898 == float(round(r.s3, 4))
        assert  233.6295 == round(float(r.s4), 4)
        assert  244.7368 == round(float(r.r1), 4)
        assert  246.3235 == round(float(r.r2), 4)
        assert 247.91025 == round(float(r.r3), 5)
        assert  252.6705 == round(float(r.r4), 4)
        
    def test_demark(self, quotes):
        results = indicators.get_pivot_points(quotes, PeriodSize.MONTH, PivotPointType.DEMARK)
        
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
        assert 215.1300 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 218.7400 == float(round(r.r1, 4))
        assert 213.2400 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
        r = results[149]
        assert 234.3475 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 239.5350 == float(round(r.r1, 4))
        assert 232.2250 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
        r = results[250]
        assert 252.1925 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 259.4350 == float(round(r.r1, 4))
        assert 249.4450 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
        r = results[251]
        assert 256.0725 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 262.2750 == float(round(r.r1, 4))
        assert 253.4450 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
        r = results[501]
        assert 268.6050 == float(round(r.pp, 4))
        assert r.r4 is None
        assert r.r3 is None
        assert r.r2 is None
        assert 280.5300 == float(round(r.r1, 4))
        assert 262.8200 == float(round(r.s1, 4))
        assert r.s2 is None
        assert r.s3 is None
        assert r.s4 is None
        
    def test_fibonacci(self, intraday_quotes):
        results = indicators.get_pivot_points(intraday_quotes[:300], PeriodSize.ONE_HOUR, PivotPointType.FIBONACCI)
        
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
        assert 368.4967 == float(round(r.pp, 4))
        assert 367.9237 == float(round(r.s1, 4))
        assert 367.5697 == float(round(r.s2, 4))
        assert 366.9967 == float(round(r.s3, 4))
        assert 369.0697 == float(round(r.r1, 4))
        assert 369.4237 == float(round(r.r2, 4))
        assert 369.9967 == float(round(r.r3, 4))
        
        r = results[118]
        assert 368.4967 == float(round(r.pp, 4))
        assert 367.9237 == float(round(r.s1, 4))
        assert 367.5697 == float(round(r.s2, 4))
        assert 366.9967 == float(round(r.s3, 4))
        assert 369.0697 == float(round(r.r1, 4))
        assert 369.4237 == float(round(r.r2, 4))
        assert 369.9967 == float(round(r.r3, 4))
        
        r = results[119]
        assert 369.0000 == float(round(r.pp, 4))
        assert 368.5760 == float(round(r.s1, 4))
        assert 368.3140 == float(round(r.s2, 4))
        assert 367.8900 == float(round(r.s3, 4))
        assert 369.4240 == float(round(r.r1, 4))
        assert 369.6860 == float(round(r.r2, 4))
        assert 370.1100 == float(round(r.r3, 4))
        
        r = results[149]
        assert 369.0000 == float(round(r.pp, 4))
        assert 368.5760 == float(round(r.s1, 4))
        assert 368.3140 == float(round(r.s2, 4))
        assert 367.8900 == float(round(r.s3, 4))
        assert 369.4240 == float(round(r.r1, 4))
        assert 369.6860 == float(round(r.r2, 4))
        assert 370.1100 == float(round(r.r3, 4))
        
        r = results[299]
        assert 368.8200 == float(round(r.pp, 4))
        assert 367.5632 == float(round(r.s1, 4))
        assert 366.7868 == float(round(r.s2, 4))
        assert 365.5300 == float(round(r.s3, 4))
        assert 370.0768 == float(round(r.r1, 4))
        assert 370.8532 == float(round(r.r2, 4))
        assert 372.1100 == float(round(r.r3, 4))
        
    def test_woodie(self, intraday_quotes):
        results = indicators.get_pivot_points(intraday_quotes, PeriodSize.DAY, PivotPointType.WOODIE)
        
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
        assert 368.7875 == float(round(r.pp, 4))
        assert 367.9850 == float(round(r.s1, 4))
        assert 365.1175 == float(round(r.s2, 4))
        assert 364.3150 == float(round(r.s3, 4))
        assert 371.6550 == float(round(r.r1, 4))
        assert 372.4575 == float(round(r.r2, 4))
        assert 375.3250 == float(round(r.r3, 4))
        
        r = results[1172]
        assert 370.9769 == float(round(r.pp, 4))
        assert 370.7938 == float(round(r.s1, 4))
        assert 368.6845 == float(round(r.s2, 4))
        assert 368.5014 == float(round(r.s3, 4))
        assert 373.0862 == float(round(r.r1, 4))
        assert 373.2693 == float(round(r.r2, 4))
        assert 375.3786 == float(round(r.r3, 4))
        
        r = results[1173]
        assert 371.3625 == float(round(r.pp, 4))
        assert 370.2650 == float(round(r.s1, 4))
        assert 369.9525 == float(round(r.s2, 4))
        assert 368.8550 == float(round(r.s3, 4))
        assert 371.6750 == float(round(r.r1, 4))
        assert 372.7725 == float(round(r.r2, 4))
        assert 373.0850 == float(round(r.r3, 4))
        
        r = results[1563]
        assert 371.3625 == float(round(r.pp, 4))
        assert 370.2650 == float(round(r.s1, 4))
        assert 369.9525 == float(round(r.s2, 4))
        assert 368.8550 == float(round(r.s3, 4))
        assert 371.6750 == float(round(r.r1, 4))
        assert 372.7725 == float(round(r.r2, 4))
        assert 373.0850 == float(round(r.r3, 4))
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_pivot_points(bad_quotes, PeriodSize.WEEK)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_pivot_points([], PeriodSize.WEEK)
        assert 0 == len(r)
        
        r = indicators.get_pivot_points(quotes[:1], PeriodSize.WEEK)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_pivot_points(quotes, PeriodSize.MONTH, PivotPointType.STANDARD)
        results = results.remove_warmup_periods()
        
        assert 482 == len(results)   
        
        last = results.pop()
        assert 266.6767 == round(float(last.pp), 4)
        assert 258.9633 == round(float(last.s1), 4)
        assert 248.9667 == round(float(last.s2), 4)
        assert 241.2533 == round(float(last.s3), 4)
        assert last.s4 is None
        assert 276.6733 == round(float(last.r1), 4)
        assert 284.3867 == round(float(last.r2), 4)
        assert 294.3833 == round(float(last.r3), 4)
        assert last.r4 is None
           
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_pivot_points(quotes, PeriodSize.THREE_MINUTES)
