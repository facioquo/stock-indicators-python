from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class BOPResult(ResultBase):
    """
    A wrapper class for a single unit of
    Balance of Power (aka Balance of Market Power) results.
    """

    @property
    def bop(self) -> Optional[float]:
        return self._csdata.Bop

    @bop.setter
    def bop(self, value):
        self._csdata.Bop = value


_T = TypeVar("_T", bound=BOPResult)
class BOPResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Balance of Power (aka Balance of Market Power) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """


class BOP(Indicator):
    is_chainee = False
    is_chainor = True

    indicator_method = CsIndicator.GetBop[Quote]
    chaining_method = None

    list_wrap_class = BOPResults
    unit_wrap_class = BOPResult


@calculate_indicator(indicator=BOP())
def get_bop(quotes: Iterable[Quote], smooth_periods: int = 14) -> BOPResults[BOPResult]:
    """Get BOP calculated.

    Balance of Power (aka Balance of Market Power) is a momentum oscillator
    that depicts the strength of buying and selling pressure.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `smooth_periods` : int, defaults 14
            Number of periods for smoothing.

    Returns:
        `BOPResults[BOPResult]`
            BOPResults is list of BOPResult with providing useful helper methods.

    See more:
         - [BOP Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Bop/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, smooth_periods)
