from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_atr(quotes: Iterable[Quote], lookback_periods: int = 14):
    """Get ATR calculated.

    Average True Range (ATR) is a measure of volatility that captures gaps and limits between periods.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 14
            Number of periods in the lookback window.

    Returns:
        `ATRResults[ATRResult]`
            ATRResults is list of ATRResult with providing useful helper methods.

    See more:
         - [ATR Reference](https://python.stockindicators.dev/indicators/Atr/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    atr_results = CsIndicator.GetAtr[Quote](CsList(Quote, quotes), lookback_periods)
    return ATRResults(atr_results, ATRResult)


class ATRResult(ResultBase):
    """
    A wrapper class for a single unit of ATR results.
    """

    @property
    def tr(self) -> Optional[float]:
        return self._csdata.Tr

    @tr.setter
    def tr(self, value):
        self._csdata.Tr = value

    @property
    def atr(self) -> Optional[float]:
        return self._csdata.Atr

    @atr.setter
    def atr(self, value):
        self._csdata.Atr = value

    @property
    def atrp(self) -> Optional[float]:
        return self._csdata.Atrp

    @atrp.setter
    def atrp(self, value):
        self._csdata.Atrp = value


_T = TypeVar("_T", bound=ATRResult)
class ATRResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of ATR(Average True Range) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
