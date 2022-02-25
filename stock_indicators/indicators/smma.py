from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_smma(quotes: Iterable[Quote], lookback_periods: int):
    """Get SMMA calculated.

    Smoothed Moving Average (SMMA) is the average of Close price
    over a lookback window using a smoothing method.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `SMMAResults[SMMAResult]`
            SMMAResults is list of SMMAResult with providing useful helper methods.

    See more:
         - [SMMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Smma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetSmma[Quote](CsList(Quote, quotes), lookback_periods)
    return SMMAResults(results, SMMAResult)


class SMMAResult(ResultBase):
    """
    A wrapper class for a single unit of Smoothed Moving Average (SMMA) results.
    """

    @property
    def smma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Smma)

    @smma.setter
    def smma(self, value):
        self._csdata.Smma = CsDecimal(value)


_T = TypeVar("_T", bound=SMMAResult)
class SMMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Smoothed Moving Average (SMMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
