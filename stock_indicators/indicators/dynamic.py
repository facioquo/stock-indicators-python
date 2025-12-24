from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import CondenseMixin
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def get_dynamic(quotes: Iterable[Quote], lookback_periods: int, k_factor: float = 0.6):
    """Get McGinley Dynamic calculated.

    McGinley Dynamic is a more responsive variant of exponential moving average.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

        `k_factor` : float, defaults 0.6
            Range adjustment factor.

    Returns:
        `DynamicResults[DynamicResult]`
            DynamicResults is list of DynamicResult with providing useful helper methods.

    See more:
         - [McGinley Dynamic Reference](https://python.stockindicators.dev/indicators/Dynamic/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetDynamic[Quote](
        CsList(Quote, quotes), lookback_periods, k_factor
    )
    return DynamicResults(results, DynamicResult)


class DynamicResult(ResultBase):
    """
    A wrapper class for a single unit of McGinley Dynamic results.
    """

    @property
    def dynamic(self) -> Optional[float]:
        return self._csdata.Dynamic

    @dynamic.setter
    def dynamic(self, value):
        self._csdata.Dynamic = value


_T = TypeVar("_T", bound=DynamicResult)


class DynamicResults(CondenseMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of McGinley Dynamic results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
