from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Iterable, Optional, Union

from stock_indicators._cslib import CsQuote, CsQuoteUtility
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import to_pydatetime, to_pydecimal
from stock_indicators.indicators.common._contrib.type_resolver import (
    generate_cs_inherited_class,
)
from stock_indicators.indicators.common.enums import CandlePart


def _get_date(quote) -> datetime:
    """Get the date property with proper null handling."""
    return to_pydatetime(quote.Date)


def _set_date(quote, value: datetime) -> None:
    """Set the date property with validation and timezone normalization."""
    if not isinstance(value, datetime):
        raise TypeError("Date must be a datetime.datetime instance")

    # Normalize timezone-aware datetime to UTC (from main branch)
    if value.tzinfo is not None and value.utcoffset() is not None:
        value = value.astimezone(timezone.utc)
    quote.Date = CsDateTime(value)


def _get_open(quote) -> Optional[Decimal]:
    """Get the open property with proper null handling."""
    return to_pydecimal(quote.Open)


def _set_open(quote, value: Optional[Union[int, float, Decimal, str]]) -> None:
    """Set the open property with validation."""
    if value is not None:
        quote.Open = CsDecimal(value)
    # Note: C# nullable decimals can't be explicitly set to None from Python.NET
    # The C# property handles null values internally when not set


def _get_high(quote) -> Optional[Decimal]:
    """Get the high property with proper null handling."""
    return to_pydecimal(quote.High)


def _set_high(quote, value: Optional[Union[int, float, Decimal, str]]) -> None:
    """Set the high property with validation."""
    if value is not None:
        quote.High = CsDecimal(value)


def _get_low(quote) -> Optional[Decimal]:
    """Get the low property with proper null handling."""
    return to_pydecimal(quote.Low)


def _set_low(quote, value: Optional[Union[int, float, Decimal, str]]) -> None:
    """Set the low property with validation."""
    if value is not None:
        quote.Low = CsDecimal(value)


def _get_close(quote) -> Optional[Decimal]:
    """Get the close property with proper null handling."""
    return to_pydecimal(quote.Close)


def _set_close(quote, value: Optional[Union[int, float, Decimal, str]]) -> None:
    """Set the close property with validation."""
    if value is not None:
        quote.Close = CsDecimal(value)


def _get_volume(quote) -> Optional[Decimal]:
    """Get the volume property with proper null handling."""
    return to_pydecimal(quote.Volume)


def _set_volume(quote, value: Optional[Union[int, float, Decimal, str]]) -> None:
    """Set the volume property with validation."""
    if value is not None:
        quote.Volume = CsDecimal(value)


class _Quote:
    """Internal Quote implementation with property definitions."""

    date = property(_get_date, _set_date)
    open = property(_get_open, _set_open)
    high = property(_get_high, _set_high)
    low = property(_get_low, _set_low)
    close = property(_get_close, _set_close)
    volume = property(_get_volume, _set_volume)

    def __init__(
        self,
        date: datetime,  # pylint: disable=too-many-positional-arguments
        open: Optional[Union[int, float, Decimal, str]] = None,  # pylint: disable=redefined-builtin
        high: Optional[Union[int, float, Decimal, str]] = None,
        low: Optional[Union[int, float, Decimal, str]] = None,
        close: Optional[Union[int, float, Decimal, str]] = None,
        volume: Optional[Union[int, float, Decimal, str]] = None,
    ):
        """
        Initialize a Quote with OHLCV data.

        Args:
            date: The date for this quote (required)
            open: Opening price (optional)
            high: High price (optional)
            low: Low price (optional)
            close: Closing price (optional)
            volume: Volume (optional)
        """
        if not isinstance(date, datetime):
            raise TypeError("date must be a datetime.datetime instance")

        self.date = date
        # Only set values that are not None to avoid C# nullable issues
        if open is not None:
            self.open = open
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if close is not None:
            self.close = close
        if volume is not None:
            self.volume = volume

    @classmethod
    def from_csquote(cls, cs_quote: CsQuote) -> "Quote":
        """Constructs `Quote` instance from C# `Quote` instance."""
        if not isinstance(cs_quote, CsQuote):
            raise TypeError("cs_quote must be a C# Quote instance")

        return cls(
            date=to_pydatetime(cs_quote.Date),
            open=to_pydecimal(cs_quote.Open),
            high=to_pydecimal(cs_quote.High),
            low=to_pydecimal(cs_quote.Low),
            close=to_pydecimal(cs_quote.Close),
            volume=to_pydecimal(cs_quote.Volume),
        )

    @classmethod
    def use(cls, quotes: Iterable["Quote"], candle_part: CandlePart) -> Any:
        """
        Optionally select which candle part to use in the calculation.
        It returns C# Object.

        Args:
            quotes: Collection of Quote objects
            candle_part: Which part of the candle to use

        Returns:
            C# collection prepared for indicator calculation
        """
        if not hasattr(quotes, "__iter__"):
            raise TypeError("quotes must be iterable")
        if not isinstance(candle_part, CandlePart):
            raise TypeError("candle_part must be a CandlePart enum value")

        try:
            return CsQuoteUtility.Use[Quote](
                CsList(Quote, quotes), candle_part.cs_value
            )
        except Exception as e:
            raise ValueError(f"Failed to prepare quotes for calculation: {e}") from e


class Quote(generate_cs_inherited_class(_Quote, CsQuote)):
    """
    A single dated quote containing OHLCV elements.
    OHLCV values can be given as any object that can be represented as a number string.

    This class extends the C# Quote type to provide Python-friendly access to quote data.
    """
