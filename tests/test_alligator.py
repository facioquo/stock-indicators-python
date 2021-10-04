from tests.testbase import TestBase
from SkenderStockIndicators import indicators

class TestAlligator(TestBase):
    def test_standard(self):
        results = indicators.get_alligator(self.quotes)

        # proper quantities
        # should always be the same number of results as there is quotes
        self.assertEqual(502, len(results))
        self.assertEqual(482, len(list(filter(lambda x: x.jaw is not None, results))))
        self.assertEqual(490, len(list(filter(lambda x: x.teeth is not None, results))))
        self.assertEqual(495, len(list(filter(lambda x: x.lips is not None, results))))

        # starting calculations at proper index
        self.assertIsNone(results[19].jaw)
        self.assertIsNotNone(results[20].jaw)

        self.assertIsNone(results[11].teeth)
        self.assertIsNotNone(results[12].teeth)

        self.assertIsNone(results[6].lips)
        self.assertIsNotNone(results[7].lips)

        # sample values
        self.assertEqual(213.81269, round(float(results[20].jaw), 5))
        self.assertEqual(213.79287, round(float(results[21].jaw), 5))
        self.assertEqual(225.60571, round(float(results[99].jaw), 5))
        self.assertEqual(260.98953, round(float(results[501].jaw), 5))
        
        self.assertEqual(213.69938, round(float(results[12].teeth), 5))
        self.assertEqual(213.80008, round(float(results[13].teeth), 5))
        self.assertEqual(226.12157, round(float(results[99].teeth), 5))
        self.assertEqual(253.53576, round(float(results[501].teeth), 5))
        
        self.assertEqual(213.63500, round(float(results[7].lips), 5))
        self.assertEqual(213.74900, round(float(results[8].lips), 5))
        self.assertEqual(226.35353, round(float(results[99].lips), 5))
        self.assertEqual(244.29591, round(float(results[501].lips), 5))
        
    def test_bad_data(self):
        results = indicators.get_alligator(self.bad_quotes)

        self.assertEqual(502, len(results))

    def test_removed(self):
        results = indicators.get_alligator(self.quotes).remove_warmup_periods()

        self.assertEqual(237, len(results))

        r = results[len(results)-1]
        self.assertEqual(260.98953, round(float(r.jaw), 5))
        self.assertEqual(253.53576, round(float(r.teeth), 5))
        self.assertEqual(244.29591, round(float(r.lips), 5))
        
    def test_exceptions(self):
        from Skender.Stock.Indicators import BadQuotesException
        self.assertRaises(BadQuotesException, indicators.get_alligator, self.data_reader.get(114))
