from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_stoch(quotes: Iterable[Quote], lookback_periods: int = 14, signal_periods: int = 3, smooth_periods: int = 3):
    """Get Stochastic Oscillator calculated, with KDJ indexes.

    Stochastic Oscillatoris a momentum indicator that looks back N periods to produce a scale of 0 to 100.
    %J is also included for the KDJ Index extension.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 14
            Number of periods for the Oscillator.

        `signal_periods` : int, defaults 3
            Smoothing period for the %D signal line.

        `smooth_periods` : int, defaults 3
            Smoothing period for the %K Oscillator.
            Use 3 for Slow or 1 for Fast.

    Returns:
        `StochResults[StochResult]`
            StochResults is list of StochResult with providing useful helper methods.

    See more:
         - [Stochastic Oscillator Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Stoch/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    stoch_results = CsIndicator.GetStoch[Quote](CsList(Quote, quotes), lookback_periods, signal_periods, smooth_periods)
    return StochResults(stoch_results, StochResult)


class StochResult(ResultBase):
    """
    A wrapper class for a single unit of Stochastic Oscillator(with KDJ Index) results.
    """

    @property
    def oscillator(self) -> Optional[float]:
        return self._csdata.Oscillator

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = value

    @property
    def signal(self) -> Optional[float]:
        return self._csdata.Signal

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = value

    @property
    def percent_j(self) -> Optional[float]:
        return self._csdata.PercentJ

    @percent_j.setter
    def percent_j(self, value):
        self._csdata.PercentJ = value

    k = oscillator
    d = signal
    j = percent_j


_T = TypeVar("_T", bound=StochResult)
class StochResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Stochastic Oscillator(with KDJ Index) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
