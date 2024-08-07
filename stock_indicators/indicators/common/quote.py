from decimal import Decimal
from typing import Iterable

from stock_indicators._cslib import CsQuote
from stock_indicators._cslib import CsQuoteUtility
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.datetime import to_pydatetime
from stock_indicators._cstypes.decimal import to_pydecimal
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common._contrib.type_resolver import generate_cs_inherited_class


def _get_date(quote):
    return to_pydatetime(quote.Date)

def _set_date(quote, value):
    quote.Date = CsDateTime(value)

def _get_open(quote):
    return to_pydecimal(quote.Open)

def _set_open(quote, value):
    quote.Open = CsDecimal(value)

def _get_high(quote):
    return to_pydecimal(quote.High)

def _set_high(quote, value):
    quote.High = CsDecimal(value)

def _get_low(quote):
    return to_pydecimal(quote.Low)

def _set_low(quote, value):
    quote.Low = CsDecimal(value)

def _get_close(quote):
    return to_pydecimal(quote.Close)

def _set_close(quote, value):
    quote.Close = CsDecimal(value)

def _get_volume(quote):
    return to_pydecimal(quote.Volume)

def _set_volume(quote, value):
    quote.Volume = CsDecimal(value)

class _Quote:
    date = property(_get_date, _set_date)
    open = property(_get_open, _set_open)
    high = property(_get_high, _set_high)
    low = property(_get_low, _set_low)
    close = property(_get_close, _set_close)
    volume = property(_get_volume, _set_volume)

    def __init__(self, date, open = None, high = None, low = None, close = None, volume = None):
        self.date = date
        self.open: Decimal = open if open else 0
        self.high: Decimal = high if high else 0
        self.low: Decimal = low if low else 0
        self.close: Decimal = close if close else 0
        self.volume: Decimal = volume if volume else 0

    @classmethod
    def from_csquote(cls, cs_quote: CsQuote):
        """Constructs `Quote` instance from C# `Quote` instance."""
        return cls(
            date=to_pydatetime(cs_quote.Date),
            open=to_pydecimal(cs_quote.Open),
            high=to_pydecimal(cs_quote.High),
            low=to_pydecimal(cs_quote.Low),
            close=to_pydecimal(cs_quote.Close),
            volume=to_pydecimal(cs_quote.Volume)
        )

    @classmethod
    def use(cls, quotes: Iterable["Quote"], candle_part: CandlePart):
        """
        Optionally select which candle part to use in the calculation.
        It returns C# Object.
        """
        return CsQuoteUtility.Use[Quote](CsList(Quote, quotes), candle_part.cs_value)


class Quote(generate_cs_inherited_class(_Quote, CsQuote)):
    """A single dated quote containing OHLCV elements."""
    pass
