from tests.TestBase import TestBase
from SkenderStockIndicators import indicators

class TestSMA(TestBase):

    def test_standard(self):
        results = indicators.get_sma(self.quotes, 20)

        # proper quantities
        # should always be the same number of results as there is quotes
        self.assertEqual(502, len(results))
        self.assertEqual(483, len(list(filter(lambda x: x.sma is not None, results))))

        # sample values
        self.assertIsNone(results[18].sma)
        self.assertEqual(214.5250, round(float(results[19].sma), 4))
        self.assertEqual(215.0310, round(float(results[24].sma), 4))
        self.assertEqual(234.9350, round(float(results[149].sma), 4))
        self.assertEqual(255.5500, round(float(results[249].sma), 4))
        self.assertEqual(251.8600, round(float(results[501].sma), 4))

    def test_bad_data(self):
        results = indicators.get_sma_extended(self.bad_quotes, 15)

        self.assertEqual(502, len(results))

    def test_removed(self):
        results = indicators.get_sma(self.quotes, 20).remove_warmup_periods()

        self.assertEqual(483, len(results))
        self.assertEqual(251.8600, round(float(results[len(results)-1].sma), 4))

    def test_exceptions(self):
        from System import ArgumentOutOfRangeException
        self.assertRaises(ArgumentOutOfRangeException, indicators.get_sma, self.quotes, 0)

        from Skender.Stock.Indicators import BadQuotesException
        self.assertRaises(BadQuotesException, indicators.get_sma, self.data_reader.get(9), 10)
