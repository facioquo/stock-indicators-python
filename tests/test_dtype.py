import pytest
from stock_indicators import indicators
from stock_indicators.indicators.common.results import DEFAULT_NAN

import numpy as np

#TODO: Needs to consider precision of each type.
class TestDType:
    def test_np_float_(self, quotes):
        self.start_test_with_bbands(quotes, np.float_)
    
    def test_np_float16(self, quotes):
        self.start_test_with_bbands(quotes, np.float16)
    
    def test_np_float32(self, quotes):
        self.start_test_with_bbands(quotes, np.float32)
        
    def test_np_float64(self, quotes):
        self.start_test_with_bbands(quotes, np.float64)
       
    def test_np_float80(self, quotes):
        self.start_test_with_bbands(quotes, np.float80)
    
    def test_np_float96(self, quotes):
        self.start_test_with_bbands(quotes, np.float96)
    
    def test_np_float128(self, quotes):
        self.start_test_with_bbands(quotes, np.float128)
    
    def test_np_float256(self, quotes):
        self.start_test_with_bbands(quotes, np.float256)

            
    def start_test_with_bbands(self, quotes, dtype):
        results = indicators.get_bollinger_bands(quotes, 20, 2, decimal=dtype, float=dtype)

        assert 502 == len(results)
        assert 483 == len(list(filter(lambda x: x.sma is not DEFAULT_NAN, results)))
        assert 483 == len(list(filter(lambda x: x.upper_band is not DEFAULT_NAN, results)))
        assert 483 == len(list(filter(lambda x: x.lower_band is not DEFAULT_NAN, results)))
        assert 483 == len(list(filter(lambda x: x.percent_b is not DEFAULT_NAN, results)))
        assert 483 == len(list(filter(lambda x: x.z_score is not DEFAULT_NAN, results)))
        assert 483 == len(list(filter(lambda x: x.width is not DEFAULT_NAN, results)))
        
        r = results[249]
        assert 255.5500 == round(float(r.sma), 4)
        assert 259.5642 == round(float(r.upper_band), 4)
        assert 251.5358 == round(float(r.lower_band), 4)
        assert 0.803923 == round(float(r.percent_b), 6)
        assert 1.215692 == round(float(r.z_score), 6)
        assert 0.031416 == round(float(r.width), 6)

        r = results[501]
        assert 251.8600  == round(float(r.sma), 4)
        assert 273.7004  == round(float(r.upper_band), 4)
        assert 230.0196  == round(float(r.lower_band), 4)
        assert 0.349362  == round(float(r.percent_b), 6)
        assert -0.602552 == round(float(r.z_score), 6)
        assert 0.173433  == round(float(r.width), 6)
