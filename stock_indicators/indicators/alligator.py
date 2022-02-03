from decimal import Decimal
from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_alligator(quotes: Iterable[Quote]):
    """Get Williams Alligator calculated.

    Williams Alligator is an indicator that transposes multiple moving averages,
    showing chart patterns that creator Bill Williams compared to an alligator's
    feeding habits when describing market movement.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

    Returns:
        `AlligatorResults[AlligatorResult]`
            AlligatorResults is list of AlligatorResult with providing useful helper methods.

    See more:
         - [Williams Alligator Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Alligator/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    alligator_results = CsIndicator.GetAlligator[Quote](CsList(Quote, quotes))
    return AlligatorResults(alligator_results, AlligatorResult)


class AlligatorResult(ResultBase):
    """
    A wrapper class for a single unit of Williams Alligator results.
    """

    @property
    def jaw(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Jaw)

    @jaw.setter
    def jaw(self, value):
        self._csdata.Jaw = CsDecimal(value)

    @property
    def teeth(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Teeth)

    @teeth.setter
    def teeth(self, value):
        self._csdata.Teeth = CsDecimal(value)

    @property
    def lips(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Lips)

    @lips.setter
    def lips(self, value):
        self._csdata.Lips = CsDecimal(value)


_T = TypeVar("_T", bound=AlligatorResult)
class AlligatorResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Williams Alligator results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
