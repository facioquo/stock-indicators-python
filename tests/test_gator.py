from stock_indicators import indicators

class TestGator:
    def test_standard(self, quotes):
        results = indicators.get_gator(quotes)

        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.upper is not None, results)))
        assert 490 == len(list(filter(lambda x: x.lower is not None, results)))
        assert 481 == len(list(filter(lambda x: x.is_upper_expanding is not None, results)))
        assert 489 == len(list(filter(lambda x: x.is_lower_expanding is not None, results)))

        r = results[11]
        assert r.upper is None
        assert r.lower is None
        assert r.is_upper_expanding is None
        assert r.is_lower_expanding is None

        r = results[12]
        assert r.upper is None
        assert -0.1402 == round(float(r.lower), 4)
        assert r.is_upper_expanding is None
        assert r.is_lower_expanding is None
        
        r = results[13]
        assert r.upper is None
        assert -0.0406 == round(float(r.lower), 4)
        assert r.is_upper_expanding is None
        assert r.is_lower_expanding == False
        
        r = results[19]
        assert r.upper is None
        assert -1.0018 == round(float(r.lower), 4)
        assert r.is_upper_expanding is None
        assert r.is_lower_expanding == True
        
        r = results[20]
        assert  0.4004 == round(float(r.upper), 4)
        assert -1.0130 == round(float(r.lower), 4)
        assert r.is_upper_expanding is None
        assert r.is_lower_expanding == True
        
        r = results[21]
        assert  0.7298 == round(float(r.upper), 4)
        assert -0.6072 == round(float(r.lower), 4)
        assert r.is_upper_expanding == True
        assert r.is_lower_expanding == False

        r = results[99]
        assert  0.5159 == round(float(r.upper), 4)
        assert -0.2320 == round(float(r.lower), 4)
        assert r.is_upper_expanding == False
        assert r.is_lower_expanding == True
        
        r = results[249]
        assert  3.1317 == round(float(r.upper), 4)
        assert -1.8058 == round(float(r.lower), 4)
        assert r.is_upper_expanding == True
        assert r.is_lower_expanding == False
        
        r = results[501]
        assert  7.4538 == round(float(r.upper), 4)
        assert -9.2399 == round(float(r.lower), 4)
        assert r.is_upper_expanding == True
        assert r.is_lower_expanding == True
        
    def test_gator_with_alligator(self, quotes):
        alligator_results = indicators.get_alligator(quotes)
        alligator_results.done()
        
        results = indicators.get_gator(alligator_results)
        assert 502 == len(results)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_gator(bad_quotes)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_gator([])
        assert 0 == len(r)
        
        r = indicators.get_gator(quotes[:1])
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_gator(quotes).remove_warmup_periods()
        
        assert 502 - 150 == len(results)
        
        last = results.pop()
        assert  7.4538 == round(float(last.upper), 4)
        assert -9.2399 == round(float(last.lower), 4)
        assert last.is_upper_expanding == True
        assert last.is_lower_expanding == True
