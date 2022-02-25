from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_hma(quotes: Iterable[Quote], lookback_periods: int):
    """Get HMA calculated.

    Hull Moving Average (HMA) is a modified weighted average
    of Close price over N lookback periods that reduces lag.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `HMAResults[HMAResult]`
            HMAResults is list of HMAResult with providing useful helper methods.

    See more:
         - [HMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Hma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetHma[Quote](CsList(Quote, quotes), lookback_periods)
    return HMAResults(results, HMAResult)


class HMAResult(ResultBase):
    """
    A wrapper class for a single unit of Hull Moving Average (HMA) results.
    """

    @property
    def hma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Hma)

    @hma.setter
    def hma(self, value):
        self._csdata.Hma = CsDecimal(value)


_T = TypeVar("_T", bound=HMAResult)
class HMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Hull Moving Average (HMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
