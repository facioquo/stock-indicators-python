from tests.TestBase import TestBase
from SkenderStockIndicators import indicators

class TestSMAExtended(TestBase):
    def test_extended(self):
        results = indicators.get_sma_extended(self.quotes, 20)

        # Assertions.
        # Proper quantities.
        # Should always be the same number of results as there is quotes.
        self.assertEqual(502, len(results))
        self.assertEqual(483, len(list(filter(lambda x: x.sma is not None, results))))

        # Sample value.
        r = results[501]
        self.assertEqual(251.8600, round(float(r.sma), 4))
        self.assertEqual(9.4500  , round(float(r.Mad), 4))
        self.assertEqual(119.2510, round(float(r.Mse), 4))
        self.assertEqual(0.037637, round(float(r.Mape), 6))

    def test_bad_data(self):
        results = indicators.get_sma_extended(self.bad_quotes, 15)

        # Assertions 
        self.assertEqual(502, len(results))

    def test_removed(self):
        results = indicators.get_sma_extended(self.quotes, 20).remove_warmup_periods()

        # Assertions
        self.assertEqual(502 - 19, len(results))
        self.assertEqual(251.8600, round(float(results[len(results)-1].sma), 4))

    def test_exceptions(self):
        from System import ArgumentOutOfRangeException
        self.assertRaises(ArgumentOutOfRangeException, indicators.get_sma_extended, self.quotes, 0)

        from Skender.Stock.Indicators import BadQuotesException
        self.assertRaises(BadQuotesException, indicators.get_sma_extended, self.data_reader.get(9), 10)
