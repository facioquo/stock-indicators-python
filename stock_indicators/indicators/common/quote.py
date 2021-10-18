from stock_indicators._cslib import CsQuote
from stock_indicators._cstypes import DateTime, Decimal

class Quote(CsQuote):
    def __init__(self, date, open = None, high = None, low = None, close = None, volume = None):
        self.Date = DateTime(date)
        self.Open = Decimal(open) if open else super().Open
        self.High = Decimal(high) if high else super().High
        self.Low = Decimal(low) if low else super().Low
        self.Close = Decimal(close) if close else super().Close
        self.Volume = Decimal(volume) if volume else super().Volume

    # @staticmethod
    # def fromCsQuote(csQuote: CsQuote):
    #     return Quote(
    #         date=csQuote.Date,
    #         open=csQuote.Open,
    #         high=csQuote.High,
    #         low=csQuote.Low,
    #         close=csQuote.Close,
    #         volume=csQuote.Volume
    #     )
