from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_awesome(quotes: Iterable[Quote], fast_periods: int = 5, slow_periods: int = 34):
    """Get Awesome Oscillator calculated.

    Awesome Oscillator (aka Super AO) is a measure of the gap
    between a fast and slow period modified moving average.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `fast_periods` : int, defaults 5
            Number of periods in the Fast moving average.

        `slow_periods` : int, defaults 34
            Number of periods in the Slow moving average.

    Returns:
        `AwesomeResults[AwesomeResult]`
            AwesomeResults is list of AwesomeResult with providing useful helper methods.

    See more:
         - [Awesome Oscillator Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Awesome/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    awesome_results = CsIndicator.GetAwesome[Quote](CsList(Quote, quotes), fast_periods, slow_periods)
    return AwesomeResults(awesome_results, AwesomeResult)


class AwesomeResult(ResultBase):
    """
    A wrapper class for a single unit of Awesome Oscillator results.
    """

    @property
    def oscillator(self) -> Optional[float]:
        return self._csdata.Oscillator

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = value

    @property
    def normalized(self) -> Optional[float]:
        return self._csdata.Normalized

    @normalized.setter
    def normalized(self, value):
        self._csdata.Normalized = value


_T = TypeVar("_T", bound=AwesomeResult)
class AwesomeResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Awesome Oscillator (aka Super AO) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
