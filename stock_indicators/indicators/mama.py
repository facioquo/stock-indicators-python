from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_mama(quotes: Iterable[Quote], fast_limit: float = 0.5,
             slow_limit: float = 0.05):
    """Get MAMA calculated.

    MESA Adaptive Moving Average (MAMA) is a 5-period
    adaptive moving average of high/low price.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `fast_limit` : float, defaults 0.5
            Fast limit threshold.

        `slow_limit` : float, defaults 0.05
            Slow limit threshold.

    Returns:
        `MAMAResults[MAMAResult]`
            MAMAResults is list of MAMAResult with providing useful helper methods.

    See more:
         - [MAMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Mama/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetMama[Quote](CsList(Quote, quotes), fast_limit,
                                         slow_limit)
    return MAMAResults(results, MAMAResult)


class MAMAResult(ResultBase):
    """
    A wrapper class for a single unit of MESA Adaptive Moving Average (MAMA) results.
    """

    @property
    def mama(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Mama)

    @mama.setter
    def mama(self, value):
        self._csdata.Mama = CsDecimal(value)

    @property
    def fama(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Fama)

    @fama.setter
    def fama(self, value):
        self._csdata.Fama = CsDecimal(value)


_T = TypeVar("_T", bound=MAMAResult)
class MAMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of MESA Adaptive Moving Average (MAMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
