from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class ForceIndexResult(ResultBase):
    """
    A wrapper class for a single unit of Force Index results.
    """

    @property
    def force_index(self) -> Optional[float]:
        return self._csdata.ForceIndex

    @force_index.setter
    def force_index(self, value):
        self._csdata.ForceIndex = value


_T = TypeVar("_T", bound=ForceIndexResult)
class ForceIndexResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Force Index results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """


class ForceIndex(Indicator):
    is_chainee = False
    is_chainor = True

    indicator_method = CsIndicator.GetForceIndex[Quote]
    chaining_method = None

    list_wrap_class = ForceIndexResults
    unit_wrap_class = ForceIndexResult


@calculate_indicator(indicator=ForceIndex())
def get_force_index(quotes: Iterable[Quote], lookback_periods: int) -> ForceIndexResults[ForceIndexResult]:
    """Get Force Index calculated.

    The Force Index depicts volume-based buying and selling pressure.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods for the EMA of Force Index.

    Returns:
        `ForceIndexResults[ForceIndexResult]`
            ForceIndexResults is list of ForceIndexResult with providing useful helper methods.

    See more:
         - [Force Index Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/ForceIndex/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, lookback_periods)
