from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_ultimate(quotes: Iterable[Quote], short_periods: int = 7,
                 middle_periods: int = 14, long_periods: int = 28):
    """Get Ultimate Oscillator calculated.

    Ultimate Oscillator uses several lookback periods to weigh buying power
    against True Range price to produce on oversold / overbought oscillator.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `short_periods` : int, defaults 7
           Number of periods in the smallest window.

        `middle_periods` : int, defaults 14
           Number of periods in the middle-sized window.

        `long_periods` : int, defaults 28
           Number of periods in the largest window.

    Returns:
        `UltimateResults[UltimateResult]`
            UltimateResults is list of UltimateResult with providing useful helper methods.

    See more:
         - [Ultimate Oscillator Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Ultimate/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetUltimate[Quote](CsList(Quote, quotes), short_periods,
                                             middle_periods, long_periods)
    return UltimateResults(results, UltimateResult)


class UltimateResult(ResultBase):
    """
    A wrapper class for a single unit of Ultimate Oscillator results.
    """

    @property
    def ultimate(self) -> Optional[float]:
        return self._csdata.Ultimate

    @ultimate.setter
    def ultimate(self, value):
        self._csdata.Ultimate = value


_T = TypeVar("_T", bound=UltimateResult)
class UltimateResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Ultimate Oscillator results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
