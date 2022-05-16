import pytest
from stock_indicators import indicators

class TestTRIX:
    def test_standard(self, quotes):
        results = indicators.get_trix(quotes, 20, 5)

        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.ema3 is not None, results)))
        assert 482 == len(list(filter(lambda x: x.trix is not None, results)))
        assert 478 == len(list(filter(lambda x: x.signal is not None, results)))

        r = results[67]
        assert 221.7837 == round(float(r.ema3), 4)
        assert 0.050030 == round(float(r.trix), 6)
        assert 0.057064 == round(float(r.signal), 6)

        r = results[249]
        assert 249.4469 == round(float(r.ema3), 4)
        assert 0.121781 == round(float(r.trix), 6)
        assert 0.119769 == round(float(r.signal), 6)

        r = results[501]
        assert  263.3216 == round(float(r.ema3), 4)
        assert -0.230742 == round(float(r.trix), 6)
        assert -0.204536 == round(float(r.signal), 6)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_trix(bad_quotes, 15, 2)
        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_trix(quotes, 20, 5).remove_warmup_periods()

        assert 502 - ((3 * 20) + 100) == len(results)

        last = results.pop()
        assert  263.3216 == round(float(last.ema3), 4)
        assert -0.230742 == round(float(last.trix), 6)
        assert -0.204536 == round(float(last.signal), 6)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_trix(quotes, 0)
