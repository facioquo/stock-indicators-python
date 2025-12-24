from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import CondenseMixin, RemoveWarmupMixin
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def get_cmo(quotes: Iterable[Quote], lookback_periods: int):
    """Get CMO calculated.

    The Chande Momentum Oscillator (CMO) is a momentum indicator
    depicting the weighted percentof higher prices in financial markets.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `CMOResults[CMOResult]`
            CMOResults is list of CMOResult with providing useful helper methods.

    See more:
         - [CMO Reference](https://python.stockindicators.dev/indicators/Cmo/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetCmo[Quote](CsList(Quote, quotes), lookback_periods)
    return CMOResults(results, CMOResult)


class CMOResult(ResultBase):
    """
    A wrapper class for a single unit of Chande Momentum Oscillator (CMO) results.
    """

    @property
    def cmo(self) -> Optional[float]:
        return self._csdata.Cmo

    @cmo.setter
    def cmo(self, value):
        self._csdata.Cmo = value


_T = TypeVar("_T", bound=CMOResult)


class CMOResults(CondenseMixin, RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Chande Momentum Oscillator (CMO) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
