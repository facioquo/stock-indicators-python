from tests.TestBase import TestBase
from SkenderStockIndicators import indicators

class TestAdx(TestBase):
    def test_standard(self):
        results = indicators.get_adx(self.quotes, 14)

        # proper quantities
        # should always be the same number of results as there is quotes
        self.assertEqual(502, len(results))
        self.assertEqual(475, len(list(filter(lambda x: x.adx is not None, results))))

        # sample values
        r = results[19]
        self.assertEqual(21.0361, round(float(r.pdi), 4))
        self.assertEqual(25.0124, round(float(r.mdi), 4))
        self.assertIsNone(r.adx)

        r = results[29]
        self.assertEqual(37.9719, round(float(r.pdi), 4))
        self.assertEqual(14.1658, round(float(r.mdi), 4))
        self.assertEqual(19.7949, round(float(r.adx), 4))

        r = results[248]
        self.assertEqual(32.3167, round(float(r.pdi), 4))
        self.assertEqual(18.2471, round(float(r.mdi), 4))
        self.assertEqual(30.5903, round(float(r.adx), 4))

        r = results[501]
        self.assertEqual(17.7565, round(float(r.pdi), 4))
        self.assertEqual(31.1510, round(float(r.mdi), 4))
        self.assertEqual(34.2987, round(float(r.adx), 4))

    def test_bad_data(self):
        results = indicators.get_adx(self.bad_quotes, 20)

        self.assertEqual(502, len(results))

    def test_removed(self):
        results = indicators.get_adx(self.quotes).remove_warmup_periods()

        self.assertEqual(502 - (2 * 14 + 100), len(results))

        r = results[len(results)-1]
        self.assertEqual(17.7565, round(float(r.pdi), 4))
        self.assertEqual(31.1510, round(float(r.mdi), 4))
        self.assertEqual(34.2987, round(float(r.adx), 4))

    def test_exceptions(self):
        from System import ArgumentOutOfRangeException
        self.assertRaises(ArgumentOutOfRangeException, indicators.get_adx, self.quotes, 1)

        from Skender.Stock.Indicators import BadQuotesException
        self.assertRaises(BadQuotesException, indicators.get_adx, self.data_reader.get(159), 30)
