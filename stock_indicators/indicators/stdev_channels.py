from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_stdev_channels(quotes: Iterable[Quote],
                       lookback_periods: Optional[int] = 20,
                       standard_deviations: float = 2):
    """Get Standard Deviation Channels calculated.

    Standard Deviation Channels are based on an linearregression centerline
    and standard deviations band widths.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, optional, defaults 20
            Size of the evaluation window.

        `standard_deviations` : float, defaults 2
            Width of bands. Number of Standard Deviations from the regression line.

    Returns:
        `StdevChannelsResults[StdevChannelsResult]`
            StdevChannelsResults is list of StdevChannelsResult with providing useful helper methods.

    See more:
         - [Stdev Channels Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/StdDevChannels/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetStdDevChannels[Quote](CsList(Quote, quotes), lookback_periods, standard_deviations)
    return StdevChannelsResults(results, StdevChannelsResult)


class StdevChannelsResult(ResultBase):
    """
    A wrapper class for a single unit of Standard Deviation Channels results.
    """

    @property
    def center_line(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Centerline)

    @center_line.setter
    def center_line(self, value):
        self._csdata.Centerline = CsDecimal(value)

    @property
    def upper_channel(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.UpperChannel)

    @upper_channel.setter
    def upper_channel(self, value):
        self._csdata.UpperChannel = CsDecimal(value)

    @property
    def lower_channel(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.LowerChannel)

    @lower_channel.setter
    def lower_channel(self, value):
        self._csdata.LowerChannel = CsDecimal(value)

    @property
    def break_point(self) -> bool:
        return self._csdata.BreakPoint

    @break_point.setter
    def break_point(self, value):
        self._csdata.BreakPoint = value


_T = TypeVar("_T", bound=StdevChannelsResult)
class StdevChannelsResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Standard Deviation Channels results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
