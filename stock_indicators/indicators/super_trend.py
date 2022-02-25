from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_super_trend(quotes: Iterable[Quote], lookback_periods: int = 10, multiplier: float = 3):
    """Get SuperTrend calculated.

    SuperTrend attempts to determine the primary trend of Close prices by using
    Average True Range (ATR) band thresholds. It can indicate a buy/sell signal or a
    trailing stop when the trend changes.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 10
            Number of periods for ATR.

        `multiplier` : float, defaults 3
            Multiplier sets the ATR band width.

    Returns:
        `SuperTrendResults[SuperTrendResult]`
            SuperTrendResults is list of SuperTrendResult with providing useful helper methods.

    See more:
         - [SuperTrend Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/SuperTrend/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    super_trend_results = CsIndicator.GetSuperTrend[Quote](CsList(Quote, quotes), lookback_periods, multiplier)
    return SuperTrendResults(super_trend_results, SuperTrendResult)


class SuperTrendResult(ResultBase):
    """
    A wrapper class for a single unit of Super Trend results.
    """

    @property
    def super_trend(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.SuperTrend)

    @super_trend.setter
    def super_trend(self, value):
        self._csdata.SuperTrend = CsDecimal(value)

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


_T = TypeVar("_T", bound=SuperTrendResult)
class SuperTrendResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Super Trend results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
