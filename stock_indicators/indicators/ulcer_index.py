from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_ulcer_index(quotes: Iterable[Quote], lookback_periods: int = 14):
    """Get Ulcer Index calculated.

    Ulcer Index (UI) is a measure of downside Close price volatility
    over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 14
           Number of periods in the lookback window.

    Returns:
        `UlcerIndexResults[UlcerIndexResult]`
            UlcerIndexResults is list of UlcerIndexResult with providing useful helper methods.

    See more:
         - [Ulcer Index Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/UlcerIndex/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetUlcerIndex[Quote](CsList(Quote, quotes), lookback_periods)
    return UlcerIndexResults(results, UlcerIndexResult)


class UlcerIndexResult(ResultBase):
    """
    A wrapper class for a single unit of Ulcer Index (UI) results.
    """

    @property
    def ui(self) -> Optional[float]:
        return self._csdata.UI

    @ui.setter
    def ui(self, value):
        self._csdata.UI = value


_T = TypeVar("_T", bound=UlcerIndexResult)
class UlcerIndexResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Ulcer Index (UI) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
