from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.decimal import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_epma(quotes: Iterable[Quote], lookback_periods: int):
    """Get EPMA calculated.

    Endpoint Moving Average (EPMA), also known as Least Squares
    Moving Average (LSMA), plots the projected last point of a linear
    regression lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `EPMAResults[EPMAResult]`
            EPMAResults is list of EPMAResult with providing useful helper methods.

    See more:
         - [EPMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Epma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetEpma[Quote](CsList(Quote, quotes), lookback_periods)
    return EPMAResults(results, EPMAResult)


class EPMAResult(ResultBase):
    """
    A wrapper class for a single unit of Endpoint Moving Average (EPMA) results.
    """

    @property
    def epma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Epma)

    @epma.setter
    def epma(self, value):
        self._csdata.Epma = CsDecimal(value)


_T = TypeVar("_T", bound=EPMAResult)
class EPMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Endpoint Moving Average (EPMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
