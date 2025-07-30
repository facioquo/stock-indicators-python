"""
Custom exceptions for Stock Indicators for Python.
"""


class StockIndicatorsError(Exception):
    """Base exception class for all Stock Indicators errors."""
    pass


class StockIndicatorsInitializationError(StockIndicatorsError):
    """Raised when the .NET library fails to initialize."""
    pass


class TypeConversionError(StockIndicatorsError):
    """Raised when conversion between Python and C# types fails."""
    pass


class IndicatorCalculationError(StockIndicatorsError):
    """Raised when indicator calculation fails."""
    pass


class ValidationError(StockIndicatorsError):
    """Raised when input validation fails."""
    pass