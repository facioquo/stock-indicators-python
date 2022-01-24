import pytest
from stock_indicators import indicators

class TestMACD:
    def test_standard(self, quotes):
        results = indicators.get_macd(quotes, 12, 26, 9)

        assert 502 == len(results)
        assert 477 == len(list(filter(lambda x: x.macd is not None, results)))
        assert 469 == len(list(filter(lambda x: x.signal is not None, results)))
        assert 469 == len(list(filter(lambda x: x.histogram is not None, results)))        
        
        r = results[49]
        assert   1.7203 == round(float(r.macd), 4)
        assert   1.9675 == round(float(r.signal), 4)
        assert -00.2472 == round(float(r.histogram), 4)
        assert 224.1840 == round(float(r.fast_ema), 4)
        assert 222.4637 == round(float(r.slow_ema), 4)

        r = results[249]
        assert   2.2353 == round(float(r.macd), 4)
        assert   2.3141 == round(float(r.signal), 4)
        assert -00.0789 == round(float(r.histogram), 4)
        assert 256.6780 == round(float(r.fast_ema), 4)
        assert 254.4428 == round(float(r.slow_ema), 4)

        r = results[501]
        assert  -6.2198 == round(float(r.macd), 4)
        assert  -5.8569 == round(float(r.signal), 4)
        assert  -0.3629 == round(float(r.histogram), 4)
        assert 245.4957 == round(float(r.fast_ema), 4)
        assert 251.7155 == round(float(r.slow_ema), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_macd(bad_quotes, 10, 20, 5)
        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_macd(quotes, 12, 26, 9).remove_warmup_periods()

        assert 502 - (26 + 9 + 250) == len(results)

        last = results.pop()
        assert -6.2198 == round(float(last.macd), 4)
        assert -5.8569 == round(float(last.signal), 4)
        assert -0.3629 == round(float(last.histogram), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_macd(quotes, 0, 26, 9)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_macd(quotes, 12, 12, 9)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_macd(quotes, 12, 26, -1)
