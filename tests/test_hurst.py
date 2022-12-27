import pytest
from stock_indicators import indicators

class TestHurst:
    def test_standard_long(self, longest_quotes):
        results = indicators.get_hurst(longest_quotes, len(longest_quotes) - 1)

        assert 15821 == len(results)
        assert 1 == len(list(filter(lambda x: x.hurst_exponent is not None, results)))

        r = results[15820]
        assert 0.483563 == round(float(r.hurst_exponent), 6)

    # def test_to_quotes(self, longest_quotes):
    #     new_quotes = indicators.get_hurst(longest_quotes, len(longest_quotes) - 1).to_quotes()

    #     assert 1  == len(new_quotes)

    #     q = new_quotes.pop()
    #     assert 0.483563 == round(float(q.open), 6)
    #     assert 0.483563 == round(float(q.high), 6)
    #     assert 0.483563 == round(float(q.low), 6)
    #     assert 0.483563 == round(float(q.close), 6)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_hurst(bad_quotes, 150)
        assert 502 == len(r)

    def test_no_quotes(self, quotes):
        r = indicators.get_hurst([])
        assert 0 == len(r)

        r = indicators.get_hurst(quotes[:1])
        assert 1 == len(r)

    def test_removed(self, longest_quotes):
        results = indicators.get_hurst(longest_quotes, len(longest_quotes) - 1)
        results = results.remove_warmup_periods()

        assert 1 == len(results)

        last  = results.pop()
        assert 0.483563 == round(float(last.hurst_exponent), 6)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_hurst(quotes, 19)
