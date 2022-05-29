from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_stc(quotes: Iterable[Quote], cycle_periods: int = 10,
            fast_periods: int = 23, slow_periods: int = 50):
    """Get STC calculated.

    Schaff Trend Cycle (STC) is a stochastic oscillator view
    of two converging/diverging exponential moving averages.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `cycle_periods` : int, defaults 10
            Number of periods for the Trend Cycle.

        `fast_periods` : int, defaults 23
            Number of periods in the Fast EMA.

        `slow_periods` : int, defaults 50
            Number of periods in the Slow EMA.

    Returns:
        `STCResults[STCResult]`
            STCResults is list of STCResult with providing useful helper methods.

    See more:
         - [STC Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Stc/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetStc[Quote](CsList(Quote, quotes), cycle_periods,
                                        fast_periods, slow_periods)
    return STCResults(results, STCResult)


class STCResult(ResultBase):
    """
    A wrapper class for a single unit of Schaff Trend Cycle (STC) results.
    """

    @property
    def stc(self) -> Optional[float]:
        return self._csdata.Stc

    @stc.setter
    def stc(self, value):
        self._csdata.Stc = value


_T = TypeVar("_T", bound=STCResult)
class STCResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Schaff Trend Cycle (STC) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
