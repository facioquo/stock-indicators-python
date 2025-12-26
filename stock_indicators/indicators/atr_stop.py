from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.enums import EndType
from stock_indicators.indicators.common.helpers import CondenseMixin, RemoveWarmupMixin
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def get_atr_stop(
    quotes: Iterable[Quote],
    lookback_periods: int = 21,
    multiplier: float = 3,
    end_type: EndType = EndType.CLOSE,
):
    """Get ATR Trailing Stop calculated.

    ATR Trailing Stop attempts to determine the primary trend of prices by using
    Average True Range (ATR) band thresholds. It can indicate a buy/sell signal or a
    trailing stop when the trend changes.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 21
            Number of periods for ATR.

        `multiplier` : float, defaults 3
            Multiplier sets the ATR band width.

        `end_type` : EndType, defaults EndType.CLOSE
            Sets basis for stop offsets (Close or High/Low).

    Returns:
        `AtrStopResults[AtrStopResult]`
            AtrStopResults is list of AtrStopResult with providing useful helper methods.

    See more:
         - [ATR Trailing Stop Reference](https://python.stockindicators.dev/indicators/AtrStop/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetAtrStop[Quote](
        CsList(Quote, quotes), lookback_periods, multiplier, end_type.cs_value
    )
    return AtrStopResults(results, AtrStopResult)


class AtrStopResult(ResultBase):
    """
    A wrapper class for a single unit of ATR Trailing Stop results.
    """

    @property
    def atr_stop(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.AtrStop)

    @atr_stop.setter
    def atr_stop(self, value):
        self._csdata.AtrStop = CsDecimal(value)

    @property
    def buy_stop(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.BuyStop)

    @buy_stop.setter
    def buy_stop(self, value):
        self._csdata.BuyStop = CsDecimal(value)

    @property
    def sell_stop(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.SellStop)

    @sell_stop.setter
    def sell_stop(self, value):
        self._csdata.SellStop = CsDecimal(value)


_T = TypeVar("_T", bound=AtrStopResult)


class AtrStopResults(CondenseMixin, RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of ATR Trailing Stop results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
