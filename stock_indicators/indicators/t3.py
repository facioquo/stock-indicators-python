from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_t3(quotes: Iterable[Quote], lookback_periods: int = 5,
           volume_factor: float = 0.7):
    """Get T3 calculated.

    Tillson T3 is a smooth moving average that reduces
    both lag and overshooting.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 5
            Number of periods for the EMA smoothing.

        `volume_factor` : float, defaults 0.7
            Size of the Volume Factor.

    Returns:
        `T3Results[T3Result]`
            T3Results is list of T3Result with providing useful helper methods.

    See more:
         - [T3 Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/T3/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetT3[Quote](CsList(Quote, quotes), lookback_periods,
                                       volume_factor)
    return T3Results(results, T3Result)


class T3Result(ResultBase):
    """
    A wrapper class for a single unit of Tillson T3 results.
    """

    @property
    def t3(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.T3)

    @t3.setter
    def t3(self, value):
        self._csdata.T3 = CsDecimal(value)


_T = TypeVar("_T", bound=T3Result)
class T3Results(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Tillson T3 results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
