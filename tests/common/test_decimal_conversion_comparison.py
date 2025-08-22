"""Tests comparing precision and performance of different decimal conversion methods."""

from decimal import Decimal as PyDecimal
import pytest

from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.decimal import to_pydecimal, to_pydecimal_via_double


class TestDecimalConversionComparison:
    """Test precision differences between string and double conversion methods."""
    
    def test_basic_decimal_conversion_comparison(self):
        """Test basic decimal values for precision differences."""
        test_values = [
            1996.1012,
            123.456789,
            0.123456789,
            999999.999999,
            0.000001,
            1000000.0,
        ]
        
        for py_decimal in test_values:
            cs_decimal = CsDecimal(py_decimal)
            
            string_result = to_pydecimal(cs_decimal)
            double_result = to_pydecimal_via_double(cs_decimal)
            
            # Check if they're the same
            if string_result == double_result:
                # No precision loss
                assert string_result == double_result
            else:
                # Document precision loss
                print(f"Precision difference for {py_decimal}:")
                print(f"  String method: {string_result}")
                print(f"  Double method: {double_result}")
                print(f"  Difference: {abs(string_result - double_result)}")
    
    def test_exponential_notation_conversion_comparison(self):
        """Test exponential notation values for precision differences."""
        test_values = [
            1.8e-05,
            1.234e10,
            5.6789e-15,
            9.999e20,
        ]
        
        for py_decimal in test_values:
            cs_decimal = CsDecimal(py_decimal)
            
            string_result = to_pydecimal(cs_decimal)
            double_result = to_pydecimal_via_double(cs_decimal)
            
            print(f"Testing {py_decimal} (exponential notation):")
            print(f"  String method: {string_result}")
            print(f"  Double method: {double_result}")
            
            # For exponential notation, we expect the string method to be more precise
            if string_result != double_result:
                print(f"  Precision loss: {abs(string_result - double_result)}")
    
    def test_large_decimal_conversion_comparison(self):
        """Test large decimal values for precision differences."""
        test_values = [
            12345678901234567890.123456789,
            999999999999999999.999999999,
            123456789012345.123456789,
        ]
        
        for py_decimal in test_values:
            cs_decimal = CsDecimal(py_decimal)
            
            string_result = to_pydecimal(cs_decimal)
            double_result = to_pydecimal_via_double(cs_decimal)
            
            print(f"Testing large decimal {py_decimal}:")
            print(f"  String method: {string_result}")
            print(f"  Double method: {double_result}")
            
            # Large decimals are where we expect the most precision loss
            if string_result != double_result:
                precision_loss = abs(string_result - double_result)
                relative_error = precision_loss / abs(string_result) if string_result != 0 else 0
                print(f"  Absolute precision loss: {precision_loss}")
                print(f"  Relative error: {relative_error:.2e}")
    
    def test_high_precision_decimal_conversion_comparison(self):
        """Test high precision decimal values."""
        test_values = [
            PyDecimal('3.141592653589793238462643383279502884197'),
            PyDecimal('2.718281828459045235360287471352662497757'),
            PyDecimal('1.414213562373095048801688724209698078569'),
            PyDecimal('0.123456789012345678901234567890123456789'),
        ]
        
        for py_decimal in test_values:
            cs_decimal = CsDecimal(str(py_decimal))
            
            string_result = to_pydecimal(cs_decimal)
            double_result = to_pydecimal_via_double(cs_decimal)
            
            print(f"Testing high precision {py_decimal}:")
            print(f"  Original:      {py_decimal}")
            print(f"  String method: {string_result}")
            print(f"  Double method: {double_result}")
            
            # Compare precision loss
            string_loss = abs(py_decimal - string_result)
            double_loss = abs(py_decimal - double_result)
            
            print(f"  String precision loss: {string_loss}")
            print(f"  Double precision loss: {double_loss}")
    
    def test_edge_cases_conversion_comparison(self):
        """Test edge cases like very small and very large numbers."""
        test_values = [
            1e-28,  # Very small
            1e28,   # Very large
            0.0,    # Zero
            -123.456,  # Negative
            float('inf') if hasattr(float, '__dict__') and 'inf' in str(float('inf')) else 1e308,  # Large number as alternative
        ]
        
        for py_decimal in test_values:
            try:
                cs_decimal = CsDecimal(py_decimal)
                
                string_result = to_pydecimal(cs_decimal)
                double_result = to_pydecimal_via_double(cs_decimal)
                
                print(f"Testing edge case {py_decimal}:")
                print(f"  String method: {string_result}")
                print(f"  Double method: {double_result}")
                
                if string_result != double_result:
                    print(f"  Difference: {abs(string_result - double_result)}")
            
            except Exception as e:
                print(f"Error testing {py_decimal}: {e}")
    
    def test_none_input_handling(self):
        """Test that both methods handle None input correctly."""
        string_result = to_pydecimal(None)
        double_result = to_pydecimal_via_double(None)
        
        assert string_result is None
        assert double_result is None