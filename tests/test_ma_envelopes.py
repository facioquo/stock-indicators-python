import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import MAType

class TestMAEnvelopes:
    def test_alma(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 10, 2.5, MAType.ALMA)

        assert 502 == len(results)
        assert 493 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[24]
        assert 216.0619 == round(float(r.center_line), 4)
        assert 221.4635 == round(float(r.upper_envelope), 4)
        assert 210.6604 == round(float(r.lower_envelope), 4)

        r = results[249]
        assert 257.5787 == round(float(r.center_line), 4)
        assert 264.0182 == round(float(r.upper_envelope), 4)
        assert 251.1393 == round(float(r.lower_envelope), 4)

        r = results[501]
        assert 242.1871 == round(float(r.center_line), 4)
        assert 248.2418 == round(float(r.upper_envelope), 4)
        assert 236.1324 == round(float(r.lower_envelope), 4)

    def test_dema(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.DEMA)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[38]
        assert 223.4594 == round(float(r.center_line), 4)
        assert 229.0459 == round(float(r.upper_envelope), 4)
        assert 217.8730 == round(float(r.lower_envelope), 4)

        r = results[249]
        assert 258.4452 == round(float(r.center_line), 4)
        assert 264.9064 == round(float(r.upper_envelope), 4)
        assert 251.9841 == round(float(r.lower_envelope), 4)

        r = results[501]
        assert 241.1677 == round(float(r.center_line), 4)
        assert 247.1969 == round(float(r.upper_envelope), 4)
        assert 235.1385 == round(float(r.lower_envelope), 4)

    def test_epma(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.EPMA)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[24]
        assert 216.2859 == round(float(r.center_line), 4)
        assert 221.6930 == round(float(r.upper_envelope), 4)
        assert 210.8787 == round(float(r.lower_envelope), 4)

        r = results[249]
        assert 258.5179 == round(float(r.center_line), 4)
        assert 264.9808 == round(float(r.upper_envelope), 4)
        assert 252.0549 == round(float(r.lower_envelope), 4)

        r = results[501]
        assert 235.8131 == round(float(r.center_line), 4)
        assert 241.7085 == round(float(r.upper_envelope), 4)
        assert 229.9178 == round(float(r.lower_envelope), 4)

    def test_ema(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.EMA)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[24]
        assert 215.0920 == round(float(r.center_line), 4)
        assert 220.4693 == round(float(r.upper_envelope), 4)
        assert 209.7147 == round(float(r.lower_envelope), 4)

        r = results[249]
        assert 255.3873 == round(float(r.center_line), 4)
        assert 261.7719 == round(float(r.upper_envelope), 4)
        assert 249.0026 == round(float(r.lower_envelope), 4)

        r = results[501]
        assert 249.3519 == round(float(r.center_line), 4)
        assert 255.5857 == round(float(r.upper_envelope), 4)
        assert 243.1181 == round(float(r.lower_envelope), 4)

    def test_hma(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.HMA)

        assert 502 == len(results)
        assert 480 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[149]
        assert 236.0835 == round(float(r.center_line), 4)
        assert 241.9856 == round(float(r.upper_envelope), 4)
        assert 230.1814 == round(float(r.lower_envelope), 4)

        r = results[501]
        assert 235.6972 == round(float(r.center_line), 4)
        assert 241.5897 == round(float(r.upper_envelope), 4)
        assert 229.8048 == round(float(r.lower_envelope), 4)

    def test_sma(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.SMA)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[24]
        assert 215.0310 == round(float(r.center_line), 4)
        assert 220.4068 == round(float(r.upper_envelope), 4)
        assert 209.6552 == round(float(r.lower_envelope), 4)

        r = results[249]
        assert 255.5500 == round(float(r.center_line), 4)
        assert 261.9388 == round(float(r.upper_envelope), 4)
        assert 249.16125 == round(float(r.lower_envelope), 5)

        r = results[501]
        assert 251.8600 == round(float(r.center_line), 4)
        assert 258.1565 == round(float(r.upper_envelope), 4)
        assert 245.5635 == round(float(r.lower_envelope), 4)

    def test_smma(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.SMMA)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[24]
        assert 214.8433 == round(float(r.center_line), 4)
        assert 220.2144 == round(float(r.upper_envelope), 4)
        assert 209.4722 == round(float(r.lower_envelope), 4)

        r = results[249]
        assert 252.5574 == round(float(r.center_line), 4)
        assert 258.8714 == round(float(r.upper_envelope), 4)
        assert 246.2435 == round(float(r.lower_envelope), 4)

        r = results[501]
        assert 255.6746 == round(float(r.center_line), 4)
        assert 262.0665 == round(float(r.upper_envelope), 4)
        assert 249.2828 == round(float(r.lower_envelope), 4)

    def test_tema(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.TEMA)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[57]
        assert 222.6349 == round(float(r.center_line), 4)
        assert 228.2008 == round(float(r.upper_envelope), 4)
        assert 217.0690 == round(float(r.lower_envelope), 4)

        r = results[249]
        assert 258.6208 == round(float(r.center_line), 4)
        assert 265.0863 == round(float(r.upper_envelope), 4)
        assert 252.1553 == round(float(r.lower_envelope), 4)

        r = results[501]
        assert 238.7690 == round(float(r.center_line), 4)
        assert 244.7382 == round(float(r.upper_envelope), 4)
        assert 232.7998 == round(float(r.lower_envelope), 4)

    def test_wma(self, quotes):
        results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.WMA)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.center_line is not None, results)))

        r = results[149]
        assert 235.5253 == round(float(r.center_line), 4)
        assert 241.4135 == round(float(r.upper_envelope), 4)
        assert 229.6372 == round(float(r.lower_envelope), 4)

        r = results[501]
        assert 246.5110 == round(float(r.center_line), 4)
        assert 252.6738 == round(float(r.upper_envelope), 4)
        assert 240.3483 == round(float(r.lower_envelope), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_ma_envelopes(bad_quotes, 5, 2.5, MAType.ALMA)
        assert 502 == len(r)

        r = indicators.get_ma_envelopes(bad_quotes, 5, 2.5, MAType.DEMA)
        assert 502 == len(r)

        r = indicators.get_ma_envelopes(bad_quotes, 5, 2.5, MAType.EPMA)
        assert 502 == len(r)

        r = indicators.get_ma_envelopes(bad_quotes, 5, 2.5, MAType.EMA)
        assert 502 == len(r)

        r = indicators.get_ma_envelopes(bad_quotes, 5, 2.5, MAType.HMA)
        assert 502 == len(r)

        r = indicators.get_ma_envelopes(bad_quotes, 5, 2.5, MAType.SMA)
        assert 502 == len(r)

        r = indicators.get_ma_envelopes(bad_quotes, 5, 2.5, MAType.TEMA)
        assert 502 == len(r)

        r = indicators.get_ma_envelopes(bad_quotes, 5, 2.5, MAType.WMA)
        assert 502 == len(r)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ma_envelopes(quotes, 14, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_ma_envelopes(quotes, 14, 5, MAType.KAMA)
