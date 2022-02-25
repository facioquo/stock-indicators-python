from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_adx(quotes: Iterable[Quote], lookback_periods: int = 14):
    """Get ADX calculated.

    Average Directional Movement Index (ADX) is a measure of price directional movement.
    It includes upward and downward indicators, and is often used to measure strength of trend.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 14
            Number of periods in the lookback window.

    Returns:
        `ADXResults[ADXResult]`
            ADXResults is list of ADXResult with providing useful helper methods.

    See more:
         - [ADX Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Adx/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    adx_results = CsIndicator.GetAdx[Quote](CsList(Quote, quotes), lookback_periods)
    return ADXResults(adx_results, ADXResult)


class ADXResult(ResultBase):
    """
    A wrapper class for a single unit of ADX results.
    """

    @property
    def pdi(self) -> Optional[float]:
        return self._csdata.Pdi

    @pdi.setter
    def pdi(self, value):
        self._csdata.Pdi = value

    @property
    def mdi(self) -> Optional[float]:
        return self._csdata.Mdi

    @mdi.setter
    def mdi(self, value):
        self._csdata.Mdi = value

    @property
    def adx(self) -> Optional[float]:
        return self._csdata.Adx

    @adx.setter
    def adx(self, value):
        self._csdata.Adx = value


_T = TypeVar("_T", bound=ADXResult)
class ADXResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of ADX(Average Directional Movement Index) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
