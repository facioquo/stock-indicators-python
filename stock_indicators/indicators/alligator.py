from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator, CsIReusableResult
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.chain import chainable
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def _wrap_results(results):
    return AlligatorResults(results, AlligatorResult)

def _calculate(indicator_params, is_chaining):
    if is_chaining:
        return CsIndicator.GetAlligator(*indicator_params)
    else:
        return CsIndicator.GetAlligator[Quote](*indicator_params)

@chainable(is_chainable=True, calc_func=_calculate, wrap_func=_wrap_results)
def get_alligator(quotes: Iterable[Quote],
                  jaw_periods: int = 13, jaw_offset: int = 8,
                  teeth_periods: int = 8, teeth_offset: int = 5,
                  lips_periods: int = 5, lips_offset: int = 3) -> "AlligatorResults[AlligatorResult]":
    """Get Williams Alligator calculated.

    Williams Alligator is an indicator that transposes multiple moving averages,
    showing chart patterns that creator Bill Williams compared to an alligator's
    feeding habits when describing market movement.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `jaw_periods` : int, defaults 13
            Lookback periods for the Jaw line

        `jaw_offset` : int, defaults 8
            Offset periods for the Jaw line.

        `teeth_periods` : int, defaults 8
            Lookback periods for the Teeth line.

        `teeth_offset` : int, defaults 5
            Offset periods for the Teeth line.

        `lips_periods` : int, defaults 5
            Lookback periods for the Lips line.

        `lips_offset` : int, defaults 3
            Offset periods for the Lips line.

    Returns:
        `AlligatorResults[AlligatorResult]`
            AlligatorResults is list of AlligatorResult with providing useful helper methods.

    See more:
         - [Williams Alligator Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Alligator/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, jaw_periods, jaw_offset, teeth_periods, teeth_offset, lips_periods, lips_offset)


class AlligatorResult(ResultBase):
    """
    A wrapper class for a single unit of Williams Alligator results.
    """

    @property
    def jaw(self) -> Optional[float]:
        return self._csdata.Jaw

    @jaw.setter
    def jaw(self, value):
        self._csdata.Jaw = value

    @property
    def teeth(self) -> Optional[float]:
        return self._csdata.Teeth

    @teeth.setter
    def teeth(self, value):
        self._csdata.Teeth = value

    @property
    def lips(self) -> Optional[float]:
        return self._csdata.Lips

    @lips.setter
    def lips(self, value):
        self._csdata.Lips = value


_T = TypeVar("_T", bound=AlligatorResult)
class AlligatorResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Williams Alligator results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
