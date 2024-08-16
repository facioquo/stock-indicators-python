from datetime import datetime
from typing import Iterable, Optional, TypeVar, overload

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators.indicators.common.helpers import CondenseMixin, RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


@overload
def get_vwap(quotes: Iterable[Quote], start: Optional[datetime] = None) -> "VWAPResults[VWAPResult]": ...
@overload
def get_vwap(quotes: Iterable[Quote], year: int,
             month: int = 1, day: int = 1,
             hour: int = 0, minute: int = 0) -> "VWAPResults[VWAPResult]": ...
def get_vwap(quotes, start = None, month = 1, day = 1, hour = 0, minute = 0):
    """Get VWAP calculated.

    Volume Weighted Average Price (VWAP) is a Volume weighted average
    of Close price, typically used on intraday data.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `start` : datetime, optional
            Optional anchor date. If not provided, the first date in quotes is used.

        `year`, `month`, `day`, `hour`, `minute` : int, optional
            Optional anchor date. If not provided, the first date in quotes is used.

    Returns:
        `VWAPResults[VWAPResult]`
            VWAPResults is list of VWAPResult with providing useful helper methods.

    See more:
         - [VWAP Fractal Reference](https://python.stockindicators.dev/indicators/Vwap/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    if isinstance(start, int):
        start = datetime(start, month, day, hour, minute)

    results = CsIndicator.GetVwap[Quote](CsList(Quote, quotes), CsDateTime(start) if start else None)
    return VWAPResults(results, VWAPResult)


class VWAPResult(ResultBase):
    """
    A wrapper class for a single unit of Volume Weighted Average Price (VWAP) results.
    """

    @property
    def vwap(self) -> Optional[float]:
        return self._csdata.Vwap

    @vwap.setter
    def vwap(self, value):
        self._csdata.Vwap = value


_T = TypeVar("_T", bound=VWAPResult)
class VWAPResults(CondenseMixin, RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Volume Weighted Average Price (VWAP) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
