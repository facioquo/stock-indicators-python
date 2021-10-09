import pytest
from SkenderStockIndicators import indicators

class TestAlligator:
    def test_standard(self, quotes):
        results = indicators.get_alligator(quotes)

        # proper quantities
        # should always be the same number of results as there is quotes
        assert 502 == len(results)
        assert 482 == len(list(filter(lambda x: x.jaw is not None, results)))
        assert 490 == len(list(filter(lambda x: x.teeth is not None, results)))
        assert 495 == len(list(filter(lambda x: x.lips is not None, results)))
        
        # starting calculations at proper index
        assert results[19].jaw is None
        assert results[20].jaw is not None

        assert results[11].teeth is None
        assert results[12].teeth is not None

        assert results[6].lips is None
        assert results[7].lips is not None

        # sample values
        assert 213.81269 == round(float(results[20].jaw), 5)
        assert 213.79287 == round(float(results[21].jaw), 5)
        assert 225.60571 == round(float(results[99].jaw), 5)
        assert 260.98953 == round(float(results[501].jaw), 5)

        assert 213.69938 == round(float(results[12].teeth), 5)
        assert 213.80008 == round(float(results[13].teeth), 5)
        assert 226.12157 == round(float(results[99].teeth), 5)
        assert 253.53576 == round(float(results[501].teeth), 5)

        assert 213.63500 == round(float(results[7].lips), 5)
        assert 213.74900 == round(float(results[8].lips), 5)
        assert 226.35353 == round(float(results[99].lips), 5)
        assert 244.29591 == round(float(results[501].lips), 5)
        
    def test_bad_data(self, bad_quotes):
        results = indicators.get_alligator(bad_quotes)

        assert 502 == len(results)

    def test_removed(self, quotes):
        results = indicators.get_alligator(quotes).remove_warmup_periods()

        assert 237 == len(results)

        r = results[len(results)-1]
        assert 260.98953 == round(float(r.jaw), 5)
        assert 253.53576 == round(float(r.teeth), 5)
        assert 244.29591 == round(float(r.lips), 5)
        
    def test_exceptions(self, quotes):
        from Skender.Stock.Indicators import BadQuotesException
        with pytest.raises(BadQuotesException):
            indicators.get_alligator(quotes[:114])
