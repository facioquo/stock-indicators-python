from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_dema(quotes: Iterable[Quote], lookback_periods: int):
    """Get DEMA calculated.

    Double Exponential Moving Average (DEMA) of the Close price.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `DEMAResults[DEMAResult]`
            DEMAResults is list of DEMAResult with providing useful helper methods.

    See more:
         - [DEMA Reference](https://python.stockindicators.dev/indicators/DoubleEma/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetDema[Quote](CsList(Quote, quotes), lookback_periods)
    return DEMAResults(results, DEMAResult)


class DEMAResult(ResultBase):
    """
    A wrapper class for a single unit of Double Exponential Moving Average (DEMA) results.
    """

    @property
    def dema(self) -> Optional[float]:
        return self._csdata.Dema

    @dema.setter
    def dema(self, value):
        self._csdata.Dema = value


_T = TypeVar("_T", bound=DEMAResult)
class DEMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Double Exponential Moving Average (DEMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
