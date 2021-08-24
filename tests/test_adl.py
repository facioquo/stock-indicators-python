from SkenderStockIndicators._cstypes.decimal import to_pydecimal
from .TestBase import TestBase
from SkenderStockIndicators import indicators

class TestADL(TestBase):

    def test_standard(self):
        results = indicators.get_adl(self.quotes)

        # assertions
        # should always be the same number of results as there is quotes
        self.assertEqual(502, len(results))
        self.assertEqual(502, len(list(filter(lambda x: x.adl_sma is None, results))))

        r1 = results[249]
        self.assertEqual(0.7778,        round(float(r1.money_flow_multiplier), 4))
        self.assertEqual(36433792.89,   round(float(r1.money_flow_volume),     2))
        self.assertEqual(3266400865.74, round(float(r1.adl),                   2))
        self.assertEqual(None,          r1.adl_sma)

        r2 = results[501]
        self.assertEqual(0.8052,        round(float(r2.money_flow_multiplier), 4))
        self.assertEqual(118396116.25,  round(float(r2.money_flow_volume),     2))
        self.assertEqual(3439986548.42, round(float(r2.adl),                   2))
        self.assertEqual(None,          r2.adl_sma)

    def test_convert_to_quotes(self):
        new_quotes = indicators.get_adl(self.quotes).to_quotes()

        self.assertEqual(502, len(new_quotes))

        q1 = new_quotes[249]
        self.assertEqual(3266400865.74, round(float(to_pydecimal(q1.Close)), 2))

        q2 = new_quotes[501]
        self.assertEqual(3439986548.42, round(float(to_pydecimal(q2.Close)), 2))


    def test_bad_data(self):
        results = indicators.get_adl(self.history_bad)

        self.assertEqual(502, len(results))
    
    def test_with_sma(self):
        results = indicators.get_adl(self.quotes, 20)

        # assertions
        # should always be the same number of results as there is quotes
        self.assertEqual(502, len(results))
        self.assertEqual(483, len(list(filter(lambda x: x.adl_sma is not None, results))))

        r = results[501]
        self.assertEqual(0.8052,        round(float(r.money_flow_multiplier), 4))
        self.assertEqual(118396116.25,  round(float(r.money_flow_volume),     2))
        self.assertEqual(3439986548.42, round(float(r.adl),                   2))
        self.assertEqual(3595352721.16, round(float(r.adl_sma),               2))


    def test_exceptions(self):
        from System import ArgumentOutOfRangeException
        self.assertRaises(ArgumentOutOfRangeException, indicators.get_adl, self.quotes, 0)

        from Skender.Stock.Indicators import BadQuotesException
        self.assertRaises(BadQuotesException, indicators.get_adl, self.data_reader.get(1))
