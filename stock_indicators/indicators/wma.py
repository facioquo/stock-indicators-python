from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_wma(quotes: Iterable[Quote], lookback_periods: int,
            candle_part: CandlePart = CandlePart.CLOSE):
    """Get WMA calculated.

    Weighted Moving Average (WMA) is the linear weighted average
    of Close price over N lookback periods.
    This also called Linear Weighted Moving Average (LWMA).

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
           Number of periods in the lookback window.

        `candle_part` : CandlePart, defaults CandlePart.CLOSE
            Selected OHLCV part.

    Returns:
        `WMAResults[WMAResult]`
            WMAResults is list of WMAResult with providing useful helper methods.

    See more:
         - [WMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Wma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetWma[Quote](CsList(Quote, quotes), lookback_periods,
                                        candle_part)
    return WMAResults(results, WMAResult)


class WMAResult(ResultBase):
    """
    A wrapper class for a single unit of Weighted Moving Average (WMA) results.
    """

    @property
    def wma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Wma)

    @wma.setter
    def wma(self, value):
        self._csdata.Wma = CsDecimal(value)


_T = TypeVar("_T", bound=WMAResult)
class WMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Weighted Moving Average (WMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
