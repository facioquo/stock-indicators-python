from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class DEMAResult(ResultBase):
    """
    A wrapper class for a single unit of Double Exponential Moving Average (DEMA) results.
    """

    @property
    def dema(self) -> Optional[float]:
        return self._csdata.Dema

    @dema.setter
    def dema(self, value):
        self._csdata.Dema = value


_T = TypeVar("_T", bound=DEMAResult)
class DEMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Double Exponential Moving Average (DEMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

class DEMA(Indicator):
    is_chainee = True
    is_chainor = True

    indicator_method = CsIndicator.GetDema[Quote]
    chaining_method = CsIndicator.GetDema

    list_wrap_class = DEMAResults
    unit_wrap_class = DEMAResult


@calculate_indicator(indicator=DEMA())
def get_dema(quotes: Iterable[Quote], lookback_periods: int) -> DEMAResults[DEMAResult]:
    """Get DEMA calculated.

    Double Exponential Moving Average (DEMA) of the Close price.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `DEMAResults[DEMAResult]`
            DEMAResults is list of DEMAResult with providing useful helper methods.

    See more:
         - [DEMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/DoubleEma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, lookback_periods)
