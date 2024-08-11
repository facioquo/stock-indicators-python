from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import CondenseMixin, RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_kama(quotes: Iterable[Quote], er_periods: int = 10,
             fast_periods: int = 2, slow_periods: int = 30):
    """Get KAMA calculated.

    Kaufman’s Adaptive Moving Average (KAMA) is an volatility
    adaptive moving average of Close price over configurable lookback periods.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `er_periods` : int, defaults 10
            Number of Efficiency Ratio (volatility) periods.

        `fast_periods` : int, defaults 2
            Number of periods in the Fast EMA.

        `slow_periods` : int, defaults 30
            Number of periods in the Slow EMA.

    Returns:
        `KAMAResults[KAMAResult]`
            KAMAResults is list of KAMAResult with providing useful helper methods.

    See more:
         - [KAMA Reference](https://python.stockindicators.dev/indicators/Kama/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetKama[Quote](CsList(Quote, quotes), er_periods,
                                         fast_periods, slow_periods)
    return KAMAResults(results, KAMAResult)


class KAMAResult(ResultBase):
    """
    A wrapper class for a single unit of Kaufman’s Adaptive Moving Average (KAMA) results.
    """

    @property
    def efficiency_ratio(self) -> Optional[float]:
        return self._csdata.ER

    @efficiency_ratio.setter
    def efficiency_ratio(self, value):
        self._csdata.ER = value

    @property
    def kama(self) -> Optional[float]:
        return self._csdata.Kama

    @kama.setter
    def kama(self, value):
        self._csdata.Kama = value


_T = TypeVar("_T", bound=KAMAResult)
class KAMAResults(CondenseMixin, RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Kaufman’s Adaptive Moving Average (KAMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
