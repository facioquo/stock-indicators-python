"""
Decimal Conversion Performance Research
======================================

This script demonstrates the performance vs precision trade-offs between different 
decimal conversion methods in the stock-indicators-python library.

The library provides two methods for converting C# decimals to Python decimals:

1. String-based conversion (default): High precision, slower performance
2. Double-based conversion (alternative): Lower precision, much faster performance

Results Summary:
- Performance improvement: ~4.4x faster with double-based conversion
- Precision trade-off: Small but measurable precision loss with floating-point arithmetic
"""

from decimal import Decimal as PyDecimal
import time
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.decimal import to_pydecimal, to_pydecimal_via_double


def demonstrate_precision_differences():
    """Demonstrate precision differences between conversion methods."""
    print("=== Precision Comparison ===\n")
    
    test_values = [
        1996.1012,
        123.456789,
        0.123456789,
        999999.999999,
        1.8e-05,
        12345678901234567890.123456789,
    ]
    
    print(f"{'Value':<30} {'String Method':<35} {'Double Method':<35} {'Difference':<15}")
    print("-" * 115)
    
    for value in test_values:
        try:
            cs_decimal = CsDecimal(value)
            string_result = to_pydecimal(cs_decimal)
            double_result = to_pydecimal_via_double(cs_decimal)
            
            difference = abs(string_result - double_result) if string_result != double_result else 0
            
            print(f"{str(value):<30} {str(string_result):<35} {str(double_result):<35} {str(difference):<15}")
        except Exception as e:
            print(f"{str(value):<30} Error: {e}")
    
    print()


def demonstrate_performance_differences():
    """Demonstrate performance differences between conversion methods."""
    print("=== Performance Comparison ===\n")
    
    # Create test data
    test_values = [1996.1012, 123.456789, 0.123456789, 999999.999999] * 10000
    cs_decimals = [CsDecimal(val) for val in test_values]
    
    # Benchmark string conversion
    start_time = time.perf_counter()
    string_results = [to_pydecimal(cs_decimal) for cs_decimal in cs_decimals]
    string_time = time.perf_counter() - start_time
    
    # Benchmark double conversion  
    start_time = time.perf_counter()
    double_results = [to_pydecimal_via_double(cs_decimal) for cs_decimal in cs_decimals]
    double_time = time.perf_counter() - start_time
    
    print(f"String-based conversion: {string_time:.4f} seconds")
    print(f"Double-based conversion: {double_time:.4f} seconds")
    print(f"Performance improvement: {string_time / double_time:.2f}x faster")
    print()


def recommend_usage():
    """Provide recommendations for when to use each method."""
    print("=== Usage Recommendations ===\n")
    
    print("Use String-based conversion (to_pydecimal) when:")
    print("  • Precision is critical (financial calculations, scientific computing)")
    print("  • Working with very large numbers or high-precision decimals")
    print("  • Backward compatibility is required")
    print("  • Small performance overhead is acceptable")
    print()
    
    print("Consider Double-based conversion (to_pydecimal_via_double) when:")
    print("  • Performance is critical and you're processing large datasets")
    print("  • Small precision loss is acceptable for your use case")
    print("  • Working with typical stock price data where floating-point precision is sufficient")
    print("  • You need ~4x performance improvement in decimal conversions")
    print()
    
    print("Precision Loss Characteristics:")
    print("  • Typical loss: 10^-14 to 10^-16 for normal values")
    print("  • More significant loss with very large numbers (>10^15)")
    print("  • Exponential notation values may have precision differences")
    print()


if __name__ == "__main__":
    print("Stock Indicators Python - Decimal Conversion Research")
    print("=" * 56)
    print()
    
    demonstrate_precision_differences()
    demonstrate_performance_differences()
    recommend_usage()
    
    print("Note: This research demonstrates the trade-offs identified in GitHub issue #392")
    print("The default string-based method remains unchanged for backward compatibility.")