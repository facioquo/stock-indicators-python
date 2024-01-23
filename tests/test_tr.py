from stock_indicators import indicators

class TestTr:
    def test_standard(self, quotes):
        results = indicators.get_tr(quotes)
        
        assert 502 == len(results)
        assert 501 == len(list(filter(lambda x: x.tr is not None, results)))

        r = results[0]
        assert r.tr is None

        r = results[1]
        assert 1.42 == round(float(r.tr), 2)

        r = results[12]
        assert 1.32 == round(float(r.tr), 2)

        r = results[13]
        assert 1.45 == round(float(r.tr), 2)

        r = results[24]
        assert 0.88 == round(float(r.tr), 2)

        r = results[249]
        assert 0.58 == round(float(r.tr), 2)
        
        r = results[501]
        assert 2.67 == round(float(r.tr), 2)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_tr(bad_quotes)
        assert 502 == len(r)
    
    def test_no_quotes(self, quotes):
        r = indicators.get_tr([])
        assert 0 == len(r)
        
        r = indicators.get_tr(quotes[:1])
        assert 1 == len(r)
