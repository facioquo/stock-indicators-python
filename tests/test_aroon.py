import pytest
from stock_indicators import indicators

class TestAroon:
    def test_standard(self, quotes):
        results = indicators.get_aroon(quotes, 25)

        assert 502 == len(results)
        assert 477 == len(list(filter(lambda x: x.aroon_up is not None, results)))
        assert 477 == len(list(filter(lambda x: x.aroon_down is not None, results)))
        assert 477 == len(list(filter(lambda x: x.oscillator is not None, results)))
        
        r = results[210]
        assert 100 == float(r.aroon_up)
        assert 000 == float(r.aroon_down)
        assert 100 == float(r.oscillator)

        r = results[293]
        assert 000 == float(r.aroon_up)
        assert +40 == float(r.aroon_down)
        assert -40 == float(r.oscillator)

        r = results[298]
        assert 000 == float(r.aroon_up)
        assert +20 == float(r.aroon_down)
        assert -20 == float(r.oscillator)

        r = results[458]
        assert 0000 == float(r.aroon_up)
        assert +100 == float(r.aroon_down)
        assert -100 == float(r.oscillator)

        r = results[501]
        assert +28 == float(r.aroon_up)
        assert +88 == float(r.aroon_down)
        assert -60 == float(r.oscillator)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_aroon(bad_quotes, 20)

        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_aroon(quotes, 25).remove_warmup_periods()

        assert 502 - 25 == len(results)

        last = results.pop()
        assert +28 == float(last.aroon_up)
        assert +88 == float(last.aroon_down)
        assert -60 == float(last.oscillator)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_aroon(quotes, 0)
