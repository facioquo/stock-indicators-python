from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import ToQuotesMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_dpo(quotes: Iterable[Quote], lookback_periods: int):
    """Get DPO calculated.

    Detrended Price Oscillator (DPO) depicts the difference
    between price and an offset simple moving average.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `DPOResults[DPOResult]`
            DPOResults is list of DPOResult with providing useful helper methods.

    See more:
         - [DPO Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Dpo/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetDpo[Quote](CsList(Quote, quotes), lookback_periods)
    return DPOResults(results, DPOResult)


class DPOResult(ResultBase):
    """
    A wrapper class for a single unit of Detrended Price Oscillator (DPO) results.
    """

    @property
    def sma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Sma)

    @sma.setter
    def sma(self, value):
        self._csdata.Sma = CsDecimal(value)

    @property
    def dpo(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Dpo)

    @dpo.setter
    def dpo(self, value):
        self._csdata.Dpo = CsDecimal(value)


_T = TypeVar("_T", bound=DPOResult)
class DPOResults(ToQuotesMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Detrended Price Oscillator (DPO) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
