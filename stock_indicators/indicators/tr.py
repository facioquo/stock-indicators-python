from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import CondenseMixin
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def get_tr(quotes: Iterable[Quote]):
    """Get TR calculated.

    True Range (TR) is a measure of volatility that captures gaps and limits between periods.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

    Returns:
        `TrResults[TrResult]`
            TrResults is list of TrResult with providing useful helper methods.

    See more:
         - [True Range Reference](https://python.stockindicators.dev/indicators/Atr/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetTr[Quote](CsList(Quote, quotes))
    return TrResults(results, TrResult)


class TrResult(ResultBase):
    """
    A wrapper class for a single unit of True Range (TR) results.
    """

    @property
    def tr(self) -> Optional[float]:
        return self._csdata.Tr

    @tr.setter
    def tr(self, value):
        self._csdata.Tr = value


_T = TypeVar("_T", bound=TrResult)


class TrResults(CondenseMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of True Range (TR) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
