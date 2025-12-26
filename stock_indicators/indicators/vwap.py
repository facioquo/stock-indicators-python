from datetime import datetime
from typing import Iterable, Optional, TypeVar, Union, overload

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import CondenseMixin, RemoveWarmupMixin
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


@overload
def get_vwap(
    quotes: Iterable[Quote], start: Optional[datetime] = None
) -> "VWAPResults[VWAPResult]": ...


@overload
def get_vwap(
    quotes: Iterable[Quote],
    year: int,
    *,
    month: int = 1,
    day: int = 1,
    hour: int = 0,
    minute: int = 0,
) -> "VWAPResults[VWAPResult]": ...


def get_vwap(
    quotes: Iterable[Quote],
    start: Union[datetime, int, None] = None,
    *legacy_date_parts,
    month: int = 1,
    day: int = 1,
    hour: int = 0,
    minute: int = 0,
) -> "VWAPResults[VWAPResult]":  # pylint: disable=too-many-branches,too-many-statements,keyword-arg-before-vararg
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
        # Validate legacy_date_parts is a sequence with at most 4 items
        if not isinstance(legacy_date_parts, (tuple, list)):
            raise TypeError("legacy_date_parts must be a sequence")
        if len(legacy_date_parts) > 4:
            raise ValueError(
                "Too many positional date arguments (max 4: month, day, hour, minute)"
            )

        # Interpret: start is actually the year; legacy_date_parts supply remaining
        if not isinstance(start, int):
            raise TypeError(
                "Year must be provided as an int when using legacy positional date form"
            )
        year = start

        # Fill provided parts into month, day, hour, minute if given positionally
        parts = list(legacy_date_parts)
        if len(parts) > 0:
            if not isinstance(parts[0], int):
                raise TypeError("Month must be an int")
            month = parts[0]
        if len(parts) > 1:
            if not isinstance(parts[1], int):
                raise TypeError("Day must be an int")
            day = parts[1]
        if len(parts) > 2:
            if not isinstance(parts[2], int):
                raise TypeError("Hour must be an int")
            hour = parts[2]
        if len(parts) > 3:
            if not isinstance(parts[3], int):
                raise TypeError("Minute must be an int")
            minute = parts[3]

        # Validate ranges
        if not 1 <= month <= 12:
            raise ValueError(f"Month must be 1-12, got {month}")
        if not 1 <= day <= 31:
            raise ValueError(f"Day must be 1-31, got {day}")
        if not 0 <= hour <= 23:
            raise ValueError(f"Hour must be 0-23, got {hour}")
        if not 0 <= minute <= 59:
            raise ValueError(f"Minute must be 0-59, got {minute}")

        start_dt = datetime(year, month, day, hour, minute)
    else:
        # When not using legacy parts, validate that start is either int (year) or datetime
        if start is not None:
            if isinstance(start, int):
                # Using keyword arguments for date parts
                year = start
                # Validate ranges for keyword arguments
                if not 1 <= month <= 12:
                    raise ValueError(f"Month must be 1-12, got {month}")
                if not 1 <= day <= 31:
                    raise ValueError(f"Day must be 1-31, got {day}")
                if not 0 <= hour <= 23:
                    raise ValueError(f"Hour must be 0-23, got {hour}")
                if not 0 <= minute <= 59:
                    raise ValueError(f"Minute must be 0-59, got {minute}")
                start_dt = datetime(year, month, day, hour, minute)
            elif isinstance(start, datetime):
                start_dt = start
            else:
                raise TypeError(
                    f"start must be int (year), datetime, or None, got {type(start).__name__}"
                )
        else:
            start_dt = None

    results = CsIndicator.GetVwap[Quote](
        CsList(Quote, quotes), CsDateTime(start_dt) if start_dt else None
    )
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
