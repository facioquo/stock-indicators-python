from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_tema(quotes: Iterable[Quote], lookback_periods: int):
    """Get TEMA calculated.

    Triple Exponential Moving Average (TEMA) of the Close price.
    Note: TEMA is often confused with the alternative TRIX oscillator.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `TEMAResults[TEMAResult]`
            TEMAResults is list of TEMAResult with providing useful helper methods.

    See more:
         - [TEMA Reference](https://python.stockindicators.dev/indicators/TripleEma/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetTema[Quote](CsList(Quote, quotes), lookback_periods)
    return TEMAResults(results, TEMAResult)


class TEMAResult(ResultBase):
    """
    A wrapper class for a single unit of Triple Exponential Moving Average (TEMA) results.
    """

    @property
    def tema(self) -> Optional[float]:
        return self._csdata.Tema

    @tema.setter
    def tema(self, value):
        self._csdata.Tema = value


_T = TypeVar("_T", bound=TEMAResult)
class TEMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Triple Exponential Moving Average (TEMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
