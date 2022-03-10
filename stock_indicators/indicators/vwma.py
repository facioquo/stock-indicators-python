from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_vwma(quotes: Iterable[Quote], lookback_periods: int):
    """Get VWMA calculated.

    Volume Weighted Moving Average (VWMA) is the volume adjusted average price
    over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
           Number of periods in the lookback window.

    Returns:
        `VWMAResults[VWMAResult]`
            VWMAResults is list of VWMAResult with providing useful helper methods.

    See more:
         - [VWMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Vwma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetVwma[Quote](CsList(Quote, quotes), lookback_periods)
    return VWMAResults(results, VWMAResult)


class VWMAResult(ResultBase):
    """
    A wrapper class for a single unit of Volume Weighted Moving Average (VWMA) results.
    """

    @property
    def vwma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Vwma)

    @vwma.setter
    def vwma(self, value):
        self._csdata.Vwma = CsDecimal(value)


_T = TypeVar("_T", bound=VWMAResult)
class VWMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Volume Weighted Moving Average (VWMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
