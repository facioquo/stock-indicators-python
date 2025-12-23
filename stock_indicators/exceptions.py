"""
Custom exceptions for Stock Indicators for Python.
"""


class StockIndicatorsError(Exception):
    """Base exception class for all Stock Indicators errors."""


class StockIndicatorsInitializationError(ImportError, StockIndicatorsError):
    """Raised when the .NET library fails to initialize."""


class TypeConversionError(StockIndicatorsError):
    """Raised when conversion between Python and C# types fails."""


class IndicatorCalculationError(StockIndicatorsError):
    """Raised when indicator calculation fails."""


class ValidationError(StockIndicatorsError):
    """Raised when input validation fails."""
