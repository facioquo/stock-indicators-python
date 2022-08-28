import pytest
from stock_indicators import indicators

class TestRSI:
    def test_standard(self, quotes):
        results = indicators.get_rsi(quotes, 14)

        assert 502 == len(results)
        assert 488 == len(list(filter(lambda x: x.rsi is not None, results)))

        r = results[13]
        assert r.rsi is None

        r = results[14]
        assert 62.0541 == round(float(r.rsi), 4)
                
        r = results[249]
        assert 70.9368 == round(float(r.rsi), 4)

        r = results[501]
        assert 42.0773 == round(float(r.rsi), 4)

    def test_small_lookback(self, quotes):
        results = indicators.get_rsi(quotes, 1)

        assert 502 == len(results)
        assert 501 == len(list(filter(lambda x: x.rsi is not None, results)))

        r = results[28]
        assert 100 == round(float(r.rsi), 4)

        r = results[52]
        assert   0 == round(float(r.rsi), 4)

    # def test_convert_to_quotes(self, quotes):
    #     results = indicators.get_rsi(quotes, 14).to_quotes()
        
    #     assert 488 == len(results)

    #     first = results[0]
    #     assert 62.0541 == round(float(to_pydecimal(first.Close)), 4)

    #     last = results.pop()
    #     assert 42.0773 == round(float(to_pydecimal(last.Close)), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_rsi(bad_quotes, 20)

        assert 502 == len(r)

    def test_removed(self, quotes):
        results = indicators.get_rsi(quotes, 14).remove_warmup_periods()

        assert 502 - (10 * 14) == len(results)

        last = results.pop()
        assert 42.0773 == round(float(last.rsi), 4)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_rsi(quotes, 0)
