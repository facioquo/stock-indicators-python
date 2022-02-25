from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_atr(quotes: Iterable[Quote], lookback_periods: int = 14):
    """Get ATR calculated.

    Average True Range (ATR) is a measure of volatility that captures gaps and limits between periods.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 14
            Number of periods in the lookback window.

    Returns:
        `ATRResults[ATRResult]`
            ATRResults is list of ATRResult with providing useful helper methods.

    See more:
         - [ATR Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Atr/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    atr_results = CsIndicator.GetAtr[Quote](CsList(Quote, quotes), lookback_periods)
    return ATRResults(atr_results, ATRResult)


class ATRResult(ResultBase):
    """
    A wrapper class for a single unit of ATR results.
    """

    @property
    def tr(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Tr)

    @tr.setter
    def tr(self, value):
        self._csdata.Tr = CsDecimal(value)

    @property
    def atr(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Atr)

    @atr.setter
    def atr(self, value):
        self._csdata.Atr = CsDecimal(value)

    @property
    def atrp(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Atrp)

    @atrp.setter
    def atrp(self, value):
        self._csdata.Atrp = CsDecimal(value)


_T = TypeVar("_T", bound=ATRResult)
class ATRResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of ATR(Average True Range) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
