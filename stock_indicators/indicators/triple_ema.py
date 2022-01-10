from decimal import Decimal
from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_triple_ema(quotes: Iterable[Quote], lookback_periods: int):
    """Get TEMA calculated.
    
    Triple Exponential Moving Average (TEMA) of the Close price.
    Note: TEMA is often confused with the alternative TRIX oscillator.
    
    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.
        
        `lookback_periods` : int
            Number of periods in the lookback window.
    
    Returns:
        `TEMAResults[TEMAResult]`
            TEMAResults is list of TEMAResult with providing useful helper methods.
    
    See more:
         - [TEMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/TripleEma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetTripleEma[Quote](CsList(Quote, quotes), lookback_periods)
    return TEMAResults(results, TEMAResult)

class TEMAResult(ResultBase):
    """
    A wrapper class for a single unit of Triple Exponential Moving Average (TEMA) results.
    """

    @property
    def tema(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Tema)

    @tema.setter
    def tema(self, value):
        self._csdata.Tema = CsDecimal(value)

T = TypeVar("T", bound=TEMAResult)
class TEMAResults(IndicatorResults[T]):
    """
    A wrapper class for the list of Triple Exponential Moving Average (TEMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        