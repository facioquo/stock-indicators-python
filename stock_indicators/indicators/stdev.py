from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_stdev(quotes: Iterable[Quote], lookback_periods: int,
              sma_periods: Optional[int] = None):
    """Get Rolling Standard Deviation calculated.

    Rolling Standard Deviation of Close price over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

        `sma_periods` : int, optional
            Number of periods in the Standard Deviation SMA signal line.

    Returns:
        `StdevResults[StdevResult]`
            StdevResults is list of StdevResult with providing useful helper methods.

    See more:
         - [Stdev Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/StdDev/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetStdDev[Quote](CsList(Quote, quotes), lookback_periods, sma_periods)
    return StdevResults(results, StdevResult)


class StdevResult(ResultBase):
    """
    A wrapper class for a single unit of Rolling Standard Deviation results.
    """

    @property
    def stdev(self) -> Optional[float]:
        return self._csdata.StdDev

    @stdev.setter
    def stdev(self, value):
        self._csdata.StdDev = value

    @property
    def mean(self) -> Optional[float]:
        return self._csdata.Mean

    @mean.setter
    def mean(self, value):
        self._csdata.Mean = value

    @property
    def z_score(self) -> Optional[float]:
        return self._csdata.ZScore

    @z_score.setter
    def z_score(self, value):
        self._csdata.ZScore = value

    @property
    def stdev_sma(self) -> Optional[float]:
        return self._csdata.StdDevSma

    @stdev_sma.setter
    def stdev_sma(self, value):
        self._csdata.StdDevSma = value


_T = TypeVar("_T", bound=StdevResult)
class StdevResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Rolling Standard Deviation results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
