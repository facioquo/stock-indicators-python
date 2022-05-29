from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_pvo(quotes: Iterable[Quote], fast_periods: int = 12,
               slow_periods: int = 26, signal_periods: int = 9):
    """Get PVO calculated.

    Percentage Volume Oscillator (PVO) is a simple oscillator view
    of two converging/diverging exponential moving averages of Volume.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `fast_periods` : int, defaults 12
            Number of periods in the Fast moving average.

        `slow_periods` : int, defaults 26
            Number of periods in the Slow moving average.

        `signal_periods` : int, defaults 9
            Number of periods for the PVO SMA signal line.

    Returns:
        `PVOResults[PVOResult]`
            PVOResults is list of PVOResult with providing useful helper methods.

    See more:
         - [PVO Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Pvo/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetPvo[Quote](CsList(Quote, quotes), fast_periods,
                                           slow_periods, signal_periods)
    return PVOResults(results, PVOResult)


class PVOResult(ResultBase):
    """
    A wrapper class for a single unit of Percentage Volume Oscillator (PVO) results.
    """

    @property
    def pvo(self) -> Optional[float]:
        return self._csdata.Pvo

    @pvo.setter
    def pvo(self, value):
        self._csdata.Pvo = value

    @property
    def signal(self) -> Optional[float]:
        return self._csdata.Signal

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = value

    @property
    def histogram(self) -> Optional[float]:
        return self._csdata.Histogram

    @histogram.setter
    def histogram(self, value):
        self._csdata.Histogram = value


_T = TypeVar("_T", bound=PVOResult)
class PVOResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Percentage Volume Oscillator (PVO) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
