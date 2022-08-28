from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_chop(quotes: Iterable[Quote], lookback_periods: int = 14):
    """Get Choppiness Index calculated.

    Choppiness Index (CHOP) measures the trendiness or choppiness
    over N lookback periods on a scale of 0 to 100.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 14
            Number of periods in the lookback window.

    Returns:
        `ChopResults[ChopResult]`
            ChopResults is list of ChopResult with providing useful helper methods.

    See more:
         - [Choppiness Index Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Chop/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetChop[Quote](CsList(Quote, quotes), lookback_periods)
    return ChopResults(results, ChopResult)


class ChopResult(ResultBase):
    """
    A wrapper class for a single unit of Choppiness Index (CHOP) results.
    """

    @property
    def chop(self) -> Optional[float]:
        return self._csdata.Chop

    @chop.setter
    def chop(self, value):
        self._csdata.Chop = value


_T = TypeVar("_T", bound=ChopResult)
class ChopResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Choppiness Index (CHOP) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
