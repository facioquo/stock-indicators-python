"""Benchmarks comparing performance of different decimal conversion methods."""

import pytest
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.decimal import to_pydecimal, to_pydecimal_via_double


@pytest.mark.performance
class TestDecimalConversionPerformance:
    """Benchmark performance of different decimal conversion methods."""
    
    def test_benchmark_string_conversion(self, benchmark, raw_data):
        """Benchmark the current string-based conversion method."""
        from stock_indicators._cstypes.decimal import to_pydecimal
        
        raw_data = raw_data * 100  # Use subset for faster testing
        
        # Pre-convert to CsDecimal to isolate the conversion performance
        cs_decimals = [CsDecimal(row[2]) for row in raw_data]
        
        def convert_via_string(cs_decimals):
            for cs_decimal in cs_decimals:
                to_pydecimal(cs_decimal)
        
        benchmark(convert_via_string, cs_decimals)
    
    def test_benchmark_double_conversion(self, benchmark, raw_data):
        """Benchmark the new double-based conversion method."""
        from stock_indicators._cstypes.decimal import to_pydecimal_via_double
        
        raw_data = raw_data * 100  # Use subset for faster testing
        
        # Pre-convert to CsDecimal to isolate the conversion performance
        cs_decimals = [CsDecimal(row[2]) for row in raw_data]
        
        def convert_via_double(cs_decimals):
            for cs_decimal in cs_decimals:
                to_pydecimal_via_double(cs_decimal)
        
        benchmark(convert_via_double, cs_decimals)
    
    def test_benchmark_small_dataset_string_conversion(self, benchmark):
        """Benchmark string conversion with a controlled small dataset."""
        test_values = [
            1996.1012, 123.456789, 0.123456789, 999999.999999,
            0.000001, 1000000.0, 1.8e-05, 1.234e10
        ] * 1000  # Repeat to get meaningful measurements
        
        cs_decimals = [CsDecimal(val) for val in test_values]
        
        def convert_via_string(cs_decimals):
            for cs_decimal in cs_decimals:
                to_pydecimal(cs_decimal)
        
        benchmark(convert_via_string, cs_decimals)
    
    def test_benchmark_small_dataset_double_conversion(self, benchmark):
        """Benchmark double conversion with a controlled small dataset."""
        test_values = [
            1996.1012, 123.456789, 0.123456789, 999999.999999,
            0.000001, 1000000.0, 1.8e-05, 1.234e10
        ] * 1000  # Repeat to get meaningful measurements
        
        cs_decimals = [CsDecimal(val) for val in test_values]
        
        def convert_via_double(cs_decimals):
            for cs_decimal in cs_decimals:
                to_pydecimal_via_double(cs_decimal)
        
        benchmark(convert_via_double, cs_decimals)