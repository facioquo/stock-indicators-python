from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_vortex(quotes: Iterable[Quote], lookback_periods: int):
    """Get VI calculated.

    Vortex Indicator (VI) is a measure of price directional movement.
    It includes positive and negative indicators, and is often used
    to identify trends and reversals.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
           Number of periods in the lookback window.

    Returns:
        `VortexResults[VortexResult]`
            VortexResults is list of VortexResult with providing useful helper methods.

    See more:
         - [Vortex Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Vortex/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetVortex[Quote](CsList(Quote, quotes), lookback_periods)
    return VortexResults(results, VortexResult)


class VortexResult(ResultBase):
    """
    A wrapper class for a single unit of Vortex Indicator (VI) results.
    """

    @property
    def pvi(self) -> Optional[float]:
        return self._csdata.Pvi

    @pvi.setter
    def pvi(self, value):
        self._csdata.Pvi = value

    @property
    def nvi(self) -> Optional[float]:
        return self._csdata.Nvi

    @nvi.setter
    def nvi(self, value):
        self._csdata.Nvi = value


_T = TypeVar("_T", bound=VortexResult)
class VortexResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Vortex Indicator (VI) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
