from stock_indicators import indicators

class TestCandleResults:
    def test_standard(self, quotes):
        results = indicators.get_doji(quotes, 0.1)
        
        r = results[0]
        assert 212.80 == round(float(r.candle.close), 2)
        assert   1.83 == round(float(r.candle.size), 2)
        assert   0.19 == round(float(r.candle.body), 2)
        assert   0.10 == round(float(r.candle.body_pct), 2)
        assert   1.09 == round(float(r.candle.lower_wick), 2)
        assert   0.60 == round(float(r.candle.lower_wick_pct), 2)
        assert   0.55 == round(float(r.candle.upper_wick), 2)
        assert   0.30 == round(float(r.candle.upper_wick_pct), 2)
        assert r.candle.is_bearish == False
        assert r.candle.is_bullish == True
        
        r = results[351]
        assert 263.16 == round(float(r.candle.close), 2)
        assert   1.24 == round(float(r.candle.size), 2)
        assert   0.00 == round(float(r.candle.body), 2)
        assert   0.00 == round(float(r.candle.body_pct), 2)
        assert   0.55 == round(float(r.candle.lower_wick), 2)
        assert   0.44 == round(float(r.candle.lower_wick_pct), 2)
        assert   0.69 == round(float(r.candle.upper_wick), 2)
        assert   0.56 == round(float(r.candle.upper_wick_pct), 2)
        assert r.candle.is_bearish == False
        assert r.candle.is_bullish == False
        
        r = results[501] 
        assert 245.28 == round(float(r.candle.close), 2)
        assert   2.67 == round(float(r.candle.size), 2)
        assert   0.36 == round(float(r.candle.body), 2)
        assert   0.13 == round(float(r.candle.body_pct), 2)
        assert   2.05 == round(float(r.candle.lower_wick), 2)
        assert   0.77 == round(float(r.candle.lower_wick_pct), 2)
        assert   0.26 == round(float(r.candle.upper_wick), 2)
        assert   0.10 == round(float(r.candle.upper_wick_pct), 2)
        assert r.candle.is_bearish == False
        assert r.candle.is_bullish == True
