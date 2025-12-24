import pytest

from stock_indicators import indicators


class TestHurst:
    def test_standard_long(self, quotes_longest):
        results = indicators.get_hurst(quotes_longest, len(quotes_longest) - 1)

        assert 15821 == len(results)
        assert 1 == len(list(filter(lambda x: x.hurst_exponent is not None, results)))

        r = results[15820]
        assert 0.483563 == round(float(r.hurst_exponent), 6)

    # def test_to_quotes(self, quotes_longest):
    #     new_quotes = indicators.get_hurst(
    #         quotes_longest, len(quotes_longest) - 1
    #     ).to_quotes()

    #     assert 1  == len(new_quotes)

    #     q = new_quotes.pop()
    #     assert 0.483563 == round(float(q.open), 6)
    #     assert 0.483563 == round(float(q.high), 6)
    #     assert 0.483563 == round(float(q.low), 6)
    #     assert 0.483563 == round(float(q.close), 6)

    def test_bad_data(self, quotes_bad):
        r = indicators.get_hurst(quotes_bad, 150)
        assert 502 == len(r)

    def test_quotes_no(self, quotes):
        r = indicators.get_hurst([])
        assert 0 == len(r)

        r = indicators.get_hurst(quotes[:1])
        assert 1 == len(r)

    def test_removed(self, quotes_longest):
        results = indicators.get_hurst(quotes_longest, len(quotes_longest) - 1)
        results = results.remove_warmup_periods()

        assert 1 == len(results)

        last = results.pop()
        assert 0.483563 == round(float(last.hurst_exponent), 6)

    def test_condense(self, quotes_longest):
        results = indicators.get_hurst(
            quotes_longest, len(quotes_longest) - 1
        ).condense()

        assert 1 == len(results)

        last = results.pop()
        assert 0.483563 == round(float(last.hurst_exponent), 6)

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_hurst(quotes, 19)
