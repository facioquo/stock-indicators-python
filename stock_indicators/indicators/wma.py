from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
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
         - [WMA Reference](https://python.stockindicators.dev/indicators/Wma/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    quotes = Quote.use(quotes, candle_part) # Error occurs if not assigned to local var.
    results = CsIndicator.GetWma(quotes, lookback_periods)
    return WMAResults(results, WMAResult)


class WMAResult(ResultBase):
    """
    A wrapper class for a single unit of Weighted Moving Average (WMA) results.
    """

    @property
    def wma(self) -> Optional[float]:
        return self._csdata.Wma

    @wma.setter
    def wma(self, value):
        self._csdata.Wma = value


_T = TypeVar("_T", bound=WMAResult)
class WMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Weighted Moving Average (WMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
