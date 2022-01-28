import pytest
from stock_indicators import indicators

class TestFisherTransform:
    def test_standard(self, quotes):
        results = indicators.get_fisher_transform(quotes, 10)
        
        assert 502 == len(results)
        assert 501 == len(list(filter(lambda x: x.fisher != 0, results)))
        
        r = results[0]
        assert 0 == r.fisher
        assert r.trigger is None
        
        r = results[1]
        assert 0.3428 == round(float(r.fisher), 4)
        assert      0 == r.trigger
        
        r = results[2]
        assert 0.6873 == round(float(r.fisher), 4)
        assert 0.3428 == round(float(r.trigger), 4)
        
        r = results[9]
        assert 1.3324 == round(float(r.fisher), 4)
        assert 1.4704 == round(float(r.trigger), 4)
        
        r = results[10]
        assert 0.9790 == round(float(r.fisher), 4)
        assert 1.3324 == round(float(r.trigger), 4)
        
        r = results[35]
        assert 6.1509 == round(float(r.fisher), 4)
        assert 4.7014 == round(float(r.trigger), 4)
        
        r = results[36]
        assert 5.4455 == round(float(r.fisher), 4)
        assert 6.1509 == round(float(r.trigger), 4)
        
        r = results[149]
        assert 1.0349 == round(float(r.fisher), 4)
        assert 0.7351 == round(float(r.trigger), 4)
        
        r = results[249]
        assert 1.3496 == round(float(r.fisher), 4)
        assert 1.4408 == round(float(r.trigger), 4)
        
        r = results[501]
        assert -1.2876 == round(float(r.fisher), 4)
        assert -2.0071 == round(float(r.trigger), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_fisher_transform(bad_quotes, 9)
        assert 502 == len(r)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_fisher_transform([])
        assert 0 == len(r)
        
        r = indicators.get_fisher_transform(quotes[:1])
        assert 1 == len(r)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_fisher_transform(quotes, 0)
