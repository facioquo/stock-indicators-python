from typing import Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class GatorResult(ResultBase):
    """
    A wrapper class for a single unit of Gator Oscillator results.
    """

    @property
    def upper(self) -> Optional[float]:
        return self._csdata.Upper

    @upper.setter
    def upper(self, value):
        self._csdata.Upper = value

    @property
    def lower(self) -> Optional[float]:
        return self._csdata.Lower

    @lower.setter
    def lower(self, value):
        self._csdata.Lower = value

    @property
    def is_upper_expanding(self) -> Optional[bool]:
        return self._csdata.UpperIsExpanding

    @is_upper_expanding.setter
    def is_upper_expanding(self, value):
        self._csdata.UpperIsExpanding = value

    @property
    def is_lower_expanding(self) -> Optional[bool]:
        return self._csdata.LowerIsExpanding

    @is_lower_expanding.setter
    def is_lower_expanding(self, value):
        self._csdata.LowerIsExpanding = value


_T = TypeVar("_T", bound=GatorResult)
class GatorResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Gator Oscillator results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

class Gator(Indicator):
    is_chainee = True
    is_chainor = False

    indicator_method = CsIndicator.GetGator[Quote]
    chaining_method = CsIndicator.GetGator

    list_wrap_class = GatorResults
    unit_wrap_class = GatorResult


@calculate_indicator(indicator=Gator())
def get_gator(quotes) -> GatorResults[GatorResult]:
    """Get Gator Oscillator calculated.

    Gator Oscillator is an expanded view of Williams Alligator.

    Parameters:
        `quotes` : Iterable[Quote] or Iterable[AlligatorResult]
            Historical price quotes.

    Returns:
        `GatorResults[GatorResult]`
            GatorResults is list of GatorResult with providing useful helper methods.

    See more:
         - [Gator Oscillator Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Gator/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes,)
