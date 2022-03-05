from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_volatility_stop(quotes: Iterable[Quote], lookback_periods: int = 7,
                        multiplier: float = 3):
    """Get Volatility Stop calculated.

    Volatility Stop is an ATR based indicator used to
    determine trend direction, stops, and reversals.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 7
           Number of periods in the lookback window.

        `multiplier` : float, defaults 3
           ATR offset amount.

    Returns:
        `VolatilityStopResults[VolatilityStopResult]`
            VolatilityStopResults is list of VolatilityStopResult with providing useful helper methods.

    See more:
         - [Volatility Stop Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/VolatilityStop/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetVolatilityStop[Quote](CsList(Quote, quotes), lookback_periods,
                                                   multiplier)
    return VolatilityStopResults(results, VolatilityStopResult)


class VolatilityStopResult(ResultBase):
    """
    A wrapper class for a single unit of Volatility Stop results.
    """

    @property
    def sar(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Sar)

    @sar.setter
    def sar(self, value):
        self._csdata.Sar = CsDecimal(value)

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
    def is_stop(self) -> Optional[bool]:
        return self._csdata.IsStop

    @is_stop.setter
    def is_stop(self, value):
        self._csdata.IsStop = value


_T = TypeVar("_T", bound=VolatilityStopResult)
class VolatilityStopResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Volatility Stop results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
