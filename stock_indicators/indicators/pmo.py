from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_pmo(quotes: Iterable[Quote], time_periods: int = 35,
            smooth_periods: int = 20, signal_periods: int = 10):
    """Get PMO calculated.

    Price Momentum Oscillator (PMO) is double-smoothed ROC
    based momentum indicator.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `time_periods` : int, defaults 35
            Number of periods for ROC EMA smoothing.

        `smooth_periods` : int, defaults 20
            Number of periods for PMO EMA smoothing.

        `signal_periods` : int, defaults 10
            Number of periods for Signal line EMA.

    Returns:
        `PMOResults[PMOResult]`
            PMOResults is list of PMOResult with providing useful helper methods.

    See more:
         - [PMO Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Pmo/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetPmo[Quote](CsList(Quote, quotes), time_periods,
                                        smooth_periods, signal_periods)
    return PMOResults(results, PMOResult)


class PMOResult(ResultBase):
    """
    A wrapper class for a single unit of Price Momentum Oscillator (PMO) results.
    """

    @property
    def pmo(self) -> Optional[float]:
        return self._csdata.Pmo

    @pmo.setter
    def pmo(self, value):
        self._csdata.Pmo = value

    @property
    def signal(self) -> Optional[float]:
        return self._csdata.Signal

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = value


_T = TypeVar("_T", bound=PMOResult)
class PMOResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Price Momentum Oscillator (PMO) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
