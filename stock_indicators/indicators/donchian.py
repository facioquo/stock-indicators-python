from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_donchian(quotes: Iterable[Quote], lookback_periods: int = 20):
    """Get Donchian Channels calculated.

    Donchian Channels, also called Price Channels, are derived from highest High and lowest Low values over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 22
            Number of periods in the lookback window.

    Returns:
        `DonchianResults[DonchianResult]`
            DonchianResults is list of DonchianResult with providing useful helper methods.

    See more:
         - [Donchian Channels Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Donchian/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetDonchian[Quote](CsList(Quote, quotes), lookback_periods)
    return DonchianResults(results, DonchianResult)


class DonchianResult(ResultBase):
    """
    A wrapper class for a single unit of Donchian Channels results.
    """

    @property
    def upper_band(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.UpperBand)

    @upper_band.setter
    def upper_band(self, value):
        self._csdata.UpperBand = CsDecimal(value)

    @property
    def lower_band(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.LowerBand)

    @lower_band.setter
    def lower_band(self, value):
        self._csdata.LowerBand = CsDecimal(value)

    @property
    def center_line(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Centerline)

    @center_line.setter
    def center_line(self, value):
        self._csdata.Centerline = CsDecimal(value)

    @property
    def width(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Width)

    @width.setter
    def width(self, value):
        self._csdata.Width = CsDecimal(value)


_T = TypeVar("_T", bound=DonchianResult)
class DonchianResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Donchian Channels results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
