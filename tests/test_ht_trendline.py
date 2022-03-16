from stock_indicators import indicators

class TestHTTrendline:
    def test_standard(self, quotes):
        results = indicators.get_ht_trendline(quotes)
        
        assert 502 == len(results)
        assert 502 == len(list(filter(lambda x: x.trendline is not None, results)))
        assert 496 == len(list(filter(lambda x: x.smooth_price is not None, results)))
        
        r = results[5]
        assert 214.205 == round(float(r.trendline), 3)
        assert r.smooth_price is None
        
        r = results[6]
        assert  213.84 == round(float(r.trendline), 2)
        assert 214.071 == round(float(r.smooth_price), 3)
        
        r = results[11]
        assert 213.9502 == round(float(r.trendline), 4)
        assert 213.8460 == round(float(r.smooth_price), 4)
        
        r = results[25]
        assert 215.3948 == round(float(r.trendline), 4)
        assert 216.3365 == round(float(r.smooth_price), 4)
        
        r = results[149]
        assert 233.9410 == round(float(r.trendline), 4)
        assert 235.8570 == round(float(r.smooth_price), 4)
        
        r = results[249]
        assert 253.8788 == round(float(r.trendline), 4)
        assert 257.5825 == round(float(r.smooth_price), 4)
        
        r = results[501]
        assert 252.2172 == round(float(r.trendline), 4)
        assert 242.3435 == round(float(r.smooth_price), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_ht_trendline(bad_quotes)
        assert 502 == len(r)
    
    def test_removed(self, quotes):
        results = indicators.get_ht_trendline(quotes).remove_warmup_periods()
        
        assert 502 - 100 == len(results)
        
        last = results.pop()
        assert 252.2172 == round(float(last.trendline), 4)
        assert 242.3435 == round(float(last.smooth_price), 4)
        
    def test_penny_data(self, penny_quotes):
        results = indicators.get_ht_trendline(penny_quotes)
        assert 533 == len(results)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_ht_trendline([])
        assert 0 == len(r)
        
        r = indicators.get_ht_trendline(quotes[:1])
        assert 1 == len(r)
