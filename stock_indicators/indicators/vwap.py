from datetime import datetime
from typing import Iterable, Optional, TypeVar, overload, Union

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators.indicators.common.helpers import CondenseMixin, RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


@overload
def get_vwap(quotes: Iterable[Quote], start: Optional[datetime] = None) -> "VWAPResults[VWAPResult]": ...
@overload
def get_vwap(quotes: Iterable[Quote], year: int, *,
             month: int = 1, day: int = 1,
             hour: int = 0, minute: int = 0) -> "VWAPResults[VWAPResult]": ...
def get_vwap(quotes: Iterable[Quote], start: Union[datetime, int, None] = None, *legacy_date_parts,
             month: int = 1, day: int = 1, hour: int = 0, minute: int = 0) -> "VWAPResults[VWAPResult]":  # pylint: disable=too-many-positional-arguments
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
    # Backward compatibility: support positional year,month,day,hour as in tests
    if legacy_date_parts:
        # Interpret: start is actually the year; legacy_date_parts supply remaining
        year = start if isinstance(start, int) else None
        parts = list(legacy_date_parts)
        # Fill provided parts into month, day, hour, minute if given positionally
        if len(parts) > 0: month = parts[0]
        if len(parts) > 1: day = parts[1]
        if len(parts) > 2: hour = parts[2]
        if len(parts) > 3: minute = parts[3]
        if year is None:
            raise TypeError("Year must be provided as first positional argument when using legacy positional date form")
        start_dt = datetime(year, month, day, hour, minute)
    else:
        if isinstance(start, int):
            start_dt = datetime(start, month, day, hour, minute)
        else:
            start_dt = start

    results = CsIndicator.GetVwap[Quote](CsList(Quote, quotes), CsDateTime(start_dt) if start_dt else None)
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
