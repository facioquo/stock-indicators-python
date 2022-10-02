import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.enums import BetaType

class TestBeta:
    def test_all(self, quotes, other_quotes):
        results = indicators.get_beta(other_quotes, quotes, 20, BetaType.ALL)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.beta is not None, results)))
        assert 482 == len(list(filter(lambda x: x.beta_up is not None, results)))
        assert 482 == len(list(filter(lambda x: x.beta_down is not None, results)))
        
        r = results[19]
        assert r.beta is None
        assert r.beta_up is None
        assert r.beta_down is None
        assert r.ratio is None
        assert r.convexity is None
        
        r = results[20]
        assert    1.5139 == round(float(r.beta), 4)
        assert    1.8007 == round(float(r.beta_up), 4)
        assert    0.3292 == round(float(r.beta_down), 4)
        assert    5.4693 == round(float(r.ratio), 4)
        assert    2.1652 == round(float(r.convexity), 4)
        assert -0.010678 == round(float(r.returns_eval), 6)
        assert  0.000419 == round(float(r.returns_mrkt), 6)
        
        r = results[249]
        assert  1.9200 == round(float(r.beta), 4)
        assert -1.2289 == round(float(r.beta_up), 4)
        assert -0.3956 == round(float(r.beta_down), 4)
        assert  3.1066 == round(float(r.ratio), 4)
        assert  0.6944 == round(float(r.convexity), 4)
        
        r= results[501]
        assert 1.5123 == round(float(r.beta), 4)
        assert 2.0721 == round(float(r.beta_up), 4)
        assert 1.5908 == round(float(r.beta_down), 4)
        assert 1.3026 == round(float(r.ratio), 4)
        assert 0.2316 == round(float(r.convexity), 4)
        
    def test_standard(self, quotes, other_quotes):
        results = indicators.get_beta(other_quotes, quotes, 20, BetaType.STANDARD)

        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.beta is not None, results)))

        r = results[501]
        assert 1.5123 == round(float(r.beta), 4)

    def test_up(self, quotes, other_quotes):
        results = indicators.get_beta(other_quotes, quotes, 20, BetaType.UP)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.beta_up is not None, results)))

        r = results[501]
        assert 2.0721 == round(float(r.beta_up), 4)
        
    def test_down(self, quotes, other_quotes):
        results = indicators.get_beta(other_quotes, quotes, 20, BetaType.DOWN)
        
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.beta_down is not None, results)))

        r = results[501]
        assert 1.5908 == round(float(r.beta_down), 4)

    def test_bad_data(self, bad_quotes):
        r = indicators.get_beta(bad_quotes, bad_quotes, 15, BetaType.STANDARD)
        assert 502 == len(r)
        
        r = indicators.get_beta(bad_quotes, bad_quotes, 15, BetaType.UP)
        assert 502 == len(r)
        
        r = indicators.get_beta(bad_quotes, bad_quotes, 15, BetaType.DOWN)
        assert 502 == len(r)

    def test_big_data(self, big_quotes):
        r = indicators.get_beta(big_quotes, big_quotes, 150 , BetaType.ALL)
        assert 1246 == len(r)

    # TODO: #82
    # def test_beta_msft(self, spx_quotes, msft_quotes):
    #     results = indicators.get_beta(
    #         Quote.aggregate(spx_quotes, PeriodSize.MONTH),
    #         Quote.aggregate(msft_quotes, PeriodSize.MONTH),
    #         60, BetaType.STANDARD
    #     )

    def test_removed(self, quotes, other_quotes):
        results = indicators.get_beta(other_quotes, quotes, 20).remove_warmup_periods()

        assert 502 - 20 == len(results)

        last = results.pop()
        assert 1.5123 == round(float(last.beta), 4)

    def test_same_same(self, quotes):
        results = indicators.get_beta(quotes, quotes, 20)

        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.beta is not None, results)))

        r = results[501]
        assert 1 == round(float(r.beta), 4)
        
    def test_no_quotes(self, quotes):
        r = indicators.get_beta([], [], 5)
        assert 0 == len(r)
        
        r = indicators.get_beta(quotes[:1], quotes[:1], 5)
        assert 1 == len(r)

    def test_exceptions(self, quotes, other_quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_beta(quotes, other_quotes, 0)

        from Skender.Stock.Indicators import InvalidQuotesException
        with pytest.raises(InvalidQuotesException):
            indicators.get_beta(quotes, other_quotes[:300], 30)
