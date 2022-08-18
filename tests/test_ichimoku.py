import pytest
from stock_indicators import indicators

class TestIchimoku:
    def test_standard(self, quotes):
        results = indicators.get_ichimoku(quotes, 9, 26, 52)
        
        assert 502 == len(results)
        assert 494 == len(list(filter(lambda x: x.tenkan_sen is not None, results)))
        assert 477 == len(list(filter(lambda x: x.kijun_sen is not None, results)))
        assert 451 == len(list(filter(lambda x: x.senkou_span_a is not None, results)))
        assert 425 == len(list(filter(lambda x: x.senkou_span_b is not None, results)))
        assert 476 == len(list(filter(lambda x: x.chikou_span is not None, results)))
        
        r = results[51]
        assert 224.4650 == round(float(r.tenkan_sen), 4)
        assert 221.9400 == round(float(r.kijun_sen), 4)
        assert 214.8325 == round(float(r.senkou_span_a), 4)
        assert r.senkou_span_b is None
        assert 226.3500 == round(float(r.chikou_span), 4)
        
        r = results[249]
        assert 257.1500 == round(float(r.tenkan_sen), 4)
        assert 253.0850 == round(float(r.kijun_sen), 4)
        assert 246.3125 == round(float(r.senkou_span_a), 4)
        assert 241.6850 == round(float(r.senkou_span_b), 4)
        assert 259.2100 == round(float(r.chikou_span), 4)
        
        r = results[475]
        assert 265.5750 == round(float(r.tenkan_sen), 4)
        assert 263.9650 == round(float(r.kijun_sen), 4)
        assert 274.9475 == round(float(r.senkou_span_a), 4)
        assert 274.9500 == round(float(r.senkou_span_b), 4)
        assert 245.2800 == round(float(r.chikou_span), 4)
        
        r = results[501]
        assert 241.2600 == round(float(r.tenkan_sen), 4)
        assert 251.5050 == round(float(r.kijun_sen), 4)
        assert 264.7700 == round(float(r.senkou_span_a), 4)
        assert 269.8200 == round(float(r.senkou_span_b), 4)
        assert r.chikou_span is None

    def test_extended(self, quotes):
        r = indicators.get_ichimoku(quotes, 3, 13, 40, 0, 0)
        assert 502 == len(r)
        
    def test_bad_data(self, quotes):
        r = indicators.get_ichimoku(quotes)
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_ichimoku([])
        assert 0 == len(r)
        
        r = indicators.get_ichimoku(quotes[:1])
        assert 1 == len(r)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ichimoku(quotes, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ichimoku(quotes, 9, 0, 52)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ichimoku(quotes, 9, 26, 26)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ichimoku(quotes, 9, 26, 52, -1)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ichimoku(quotes, 9, 26, 52, -1, 12)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ichimoku(quotes, 9, 26, 52, 12, -1)
