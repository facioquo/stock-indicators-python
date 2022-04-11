from decimal import Decimal
from typing import Iterable, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.enums import EndType
from stock_indicators.indicators.common.helpers import ToQuotesMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_renko(quotes: Iterable[Quote], brick_size: float,
               end_type: EndType = EndType.CLOSE):
    """Get Renko Chart calculated.

    Renko Chart is a modified Japanese candlestick pattern
    that uses time-lapsed bricks.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `brick_size` : float
            Fixed brick size ($).

        `end_type` : EndType, defaults EndType.CLOSE
            End type.  See documentation.

    Returns:
        `RenkoResults[RenkoResult]`
            RenkoResults is list of RenkoResult with providing useful helper methods.

    See more:
         - [Renko Chart Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Renko/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetRenko[Quote](CsList(Quote, quotes), CsDecimal(brick_size),
                                           end_type)
    return RenkoResults(results, RenkoResult)


def get_renko_atr(quotes: Iterable[Quote], atr_periods: int,
               end_type: EndType = EndType.CLOSE):
    """Get ATR Renko Chart calculated.

    The ATR Renko Chart is a modified Japanese candlestick pattern
    based on Average True Range brick size.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `atr_periods` : int
            Lookback periods for the ATR evaluation.

        `end_type` : EndType, defaults EndType.CLOSE
            End type.  See documentation.

    Returns:
        `RenkoResults[RenkoResult]`
            RenkoResults is list of RenkoResult with providing useful helper methods.

    See more:
         - [ATR Renko Chart Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Renko/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetRenkoAtr[Quote](CsList(Quote, quotes), atr_periods,
                                           end_type)
    return RenkoResults(results, RenkoResult)


class RenkoResult(ResultBase):
    """
    A wrapper class for a single unit of Renko Chart results.
    """

    @property
    def open(self) -> Decimal:
        return to_pydecimal(self._csdata.Open)

    @open.setter
    def open(self, value):
        self._csdata.Open = CsDecimal(value)

    @property
    def high(self) -> Decimal:
        return to_pydecimal(self._csdata.High)

    @high.setter
    def high(self, value):
        self._csdata.High = CsDecimal(value)

    @property
    def low(self) -> Decimal:
        return to_pydecimal(self._csdata.Low)

    @low.setter
    def low(self, value):
        self._csdata.Low = CsDecimal(value)

    @property
    def close(self) -> Decimal:
        return to_pydecimal(self._csdata.Close)

    @close.setter
    def close(self, value):
        self._csdata.Close = CsDecimal(value)

    @property
    def volume(self) -> Decimal:
        return to_pydecimal(self._csdata.Volume)

    @volume.setter
    def volume(self, value):
        self._csdata.Volume = CsDecimal(value)

    @property
    def is_up(self) -> bool:
        return self._csdata.IsUp

    @is_up.setter
    def is_up(self, value):
        self._csdata.IsUp = value


_T = TypeVar("_T", bound=RenkoResult)
class RenkoResults(ToQuotesMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Renko Chart results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
