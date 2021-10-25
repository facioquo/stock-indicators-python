from stock_indicators._cslib import CsQuote
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.datetime import to_pydatetime
from stock_indicators._cstypes.decimal import to_pydecimal

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

class Quote(CsQuote):
    """
    A base wrapper class for a single unit of historical quotes.
    """

    date = property(_get_date, _set_date)
    open = property(_get_open, _set_open)
    high = property(_get_high, _set_high)
    low = property(_get_low, _set_low)
    close = property(_get_close, _set_close)
    volume = property(_get_volume, _set_volume)

    def __init__(self, date, open = None, high = None, low = None, close = None, volume = None):
        self.date = date
        self.open = open if open else super().Open
        self.high = high if high else super().High
        self.low = low if low else super().Low
        self.close = close if close else super().Close
        self.volume = volume if volume else super().Volume

    @staticmethod
    def from_csquote(csQuote: CsQuote):
        """
        Constructs `Quote` instance from C# `Quote` instance. 
        """

        return Quote(
            date=to_pydatetime(csQuote.Date),
            open=csQuote.Open,
            high=csQuote.High,
            low=csQuote.Low,
            close=csQuote.Close,
            volume=csQuote.Volume
        )
