import pytest
from stock_indicators import indicators

class TestStdev:
    def test_standard(self, quotes):
        results = indicators.get_stdev(quotes, 10)
        
        assert 502 == len(results)
        assert 493 == len(list(filter(lambda x: x.stdev is not None, results)))
        assert 493 == len(list(filter(lambda x: x.z_score is not None, results)))
        assert   0 == len(list(filter(lambda x: x.stdev_sma is not None, results)))
        
        r = results[8]
        assert r.stdev is None
        assert r.mean is None
        assert r.z_score is None
        assert r.stdev_sma is None
        
        r = results[9]
        assert    0.5020 == round(float(r.stdev), 4)
        assert  214.0140 == round(float(r.mean), 4)
        assert -0.525917 == round(float(r.z_score), 6)
        assert r.stdev_sma is None
        
        r = results[249]
        assert   0.9827 == round(float(r.stdev), 4)
        assert 257.2200 == round(float(r.mean), 4)
        assert 0.783563 == round(float(r.z_score), 6)
        assert r.stdev_sma is None
        
        r = results[501]
        assert   5.4738 == round(float(r.stdev), 4)
        assert 242.4100 == round(float(r.mean), 4)
        assert 0.524312 == round(float(r.z_score), 6)
        assert r.stdev_sma is None
        
    def test_stdev_with_sma(self, quotes):
        results = indicators.get_stdev(quotes, 10, 5)
        
        assert 502 == len(results)
        assert 493 == len(list(filter(lambda x: x.stdev is not None, results)))
        assert 493 == len(list(filter(lambda x: x.z_score is not None, results)))
        assert 489 == len(list(filter(lambda x: x.stdev_sma is not None, results)))
        
        r = results[19]
        assert    1.1642 == round(float(r.stdev), 4)
        assert -0.065282 == round(float(r.z_score), 6)
        assert    1.1422 == round(float(r.stdev_sma), 4)
        
        r = results[501]
        assert   5.4738 == round(float(r.stdev), 4)
        assert 0.524312 == round(float(r.z_score), 6)
        assert   7.6886 == round(float(r.stdev_sma), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_stdev(bad_quotes, 15, 3)
        assert 502 == len(r)
        
    def test_big_data(self, big_quotes):
        r = indicators.get_stdev(big_quotes, 200, 3)
        assert 1246 == len(r)
        
    def test_no_data(self, quotes):
        r = indicators.get_stdev([], 10)
        assert 0 == len(r)
        
        r = indicators.get_stdev(quotes[:1], 10)
        assert 1 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_stdev(quotes, 10).remove_warmup_periods()
        
        assert 502 - 9 == len(results)
        
        last = results.pop()
        assert   5.4738 == round(float(last.stdev), 4)
        assert 242.4100 == round(float(last.mean), 4)
        assert 0.524312 == round(float(last.z_score), 6)
        assert last.stdev_sma is None
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stdev(quotes, 1)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stdev(quotes, 14,0)
