from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_williams_r(quotes: Iterable[Quote], lookback_periods: int = 14):
    """Get Williams %R calculated.

    Williams %R momentum indicator is a stochastic oscillator
    with scale of -100 to 0. It is exactly the same as the Fast variant
    of Stochastic Oscillator, but with a different scaling.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 14
           Number of periods in the lookback window.

    Returns:
        `WilliamsResults[WilliamsResult]`
            WilliamsResults is list of WilliamsResult with providing useful helper methods.

    See more:
         - [Williams %R Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/WilliamsR/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetWilliamsR[Quote](CsList(Quote, quotes), lookback_periods)
    return WilliamsResults(results, WilliamsResult)


class WilliamsResult(ResultBase):
    """
    A wrapper class for a single unit of Williams %R results.
    """

    @property
    def williams_r(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.WilliamsR)

    @williams_r.setter
    def williams_r(self, value):
        self._csdata.WilliamsR = CsDecimal(value)


_T = TypeVar("_T", bound=WilliamsResult)
class WilliamsResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Williams %R results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
