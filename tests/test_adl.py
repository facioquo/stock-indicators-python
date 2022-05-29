import pytest
from stock_indicators import indicators

class TestADL:
    def test_standard(self, quotes):
        results = indicators.get_adl(quotes)

        # assertions
        # should always be the same number of results as there is quotes
        assert 502 == len(results)
        assert 502 == len(list(filter(lambda x: x.adl_sma is None, results)))

        r1 = results[249]
        assert 0.7778        == round(float(r1.money_flow_multiplier), 4)
        assert 36433792.89   == round(float(r1.money_flow_volume),     2)
        assert 3266400865.74 == round(float(r1.adl),                   2)
        assert r1.adl_sma is None

        r2 = results[501]
        assert 0.8052        == round(float(r2.money_flow_multiplier), 4)
        assert 118396116.25  == round(float(r2.money_flow_volume),     2)
        assert 3439986548.42 == round(float(r2.adl),                   2)
        assert r2.adl_sma is None

    # def test_convert_to_quotes(self, quotes):
    #     new_quotes = indicators.get_adl(quotes).to_quotes()

    #     assert 502 == len(new_quotes)

    #     q1 = new_quotes[249]
    #     assert 3266400865.74 == round(float(to_pydecimal(q1.Close)), 2)

    #     q2 = new_quotes[501]
    #     assert 3439986548.42 == round(float(to_pydecimal(q2.Close)), 2)

    def test_bad_data(self, bad_quotes):
        results = indicators.get_adl(bad_quotes)

        assert 502 == len(results)
    
    def test_with_sma(self, quotes):
        results = indicators.get_adl(quotes, 20)

        # assertions
        # should always be the same number of results as there is quotes
        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.adl_sma is not None, results)))

        r = results[501]
        assert 0.8052        == round(float(r.money_flow_multiplier), 4)
        assert 118396116.25  == round(float(r.money_flow_volume),     2)
        assert 3439986548.42 == round(float(r.adl),                   2)
        assert 3595352721.16 == round(float(r.adl_sma),               2)


    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_adl(quotes, 0)
