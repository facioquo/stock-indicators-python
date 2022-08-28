from stock_indicators import indicators

class TestHeikinAshi:
    def test_standard(self, quotes):
        results = indicators.get_heikin_ashi(quotes)
        
        assert 502 == len(results)
        
        r = results[501]
        assert  241.3018 == round(float(r.open), 4)
        assert  245.5400 == round(float(r.high), 4)
        assert  241.3018 == round(float(r.low), 4)
        assert  244.6525 == round(float(r.close), 4)
        assert 147031456 == r.volume
        
    # def test_to_quotes(self, quotes):
    #     new_quotes = indicators.get_heikin_ashi(quotes).to_quotes()
        
    #     assert 502 == len(new_quotes)
    #     q = new_quotes[501]
    #     assert  241.3018 == round(float(q.open), 4)
    #     assert  245.5400 == round(float(q.high), 4)
    #     assert  241.3018 == round(float(q.low), 4)
    #     assert  244.6525 == round(float(q.close), 4)
    #     assert 147031456 == q.volume
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_heikin_ashi(bad_quotes)
        assert 502 == len(r)
