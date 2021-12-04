from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_adl(quotes: Iterable[Quote], sma_periods: Optional[int] = None):
    """Get ADL calculated.
    
    Accumulation/Distribution Line (ADL) is a rolling accumulation of Chaikin Money Flow Volume.
    
    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.
        
        `sma_periods` : int, optional
            Number of periods in the moving average of ADL.
    
    Returns:
        `ADLResults[ADLResult]`
            ADLResults is list of ADLResult with providing useful helper methods.
    
    See more:
         - [ADL Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Adl/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    adl_results = CsIndicator.GetAdl[Quote](CsList(Quote, quotes), sma_periods)
    return ADLResults(adl_results, ADLResult)

class ADLResult(ResultBase):
    """
    A wrapper class for a single unit of ADL results.
    """

    @property
    def money_flow_multiplier(self):
        return to_pydecimal(self._csdata.MoneyFlowMultiplier)

    @money_flow_multiplier.setter
    def money_flow_multiplier(self, value):
        self._csdata.MoneyFlowMultiplier = CsDecimal(value)

    @property
    def money_flow_volume(self):
        return to_pydecimal(self._csdata.MoneyFlowVolume)

    @money_flow_volume.setter
    def money_flow_volume(self, value):
        self._csdata.MoneyFlowVolume = CsDecimal(value)

    @property
    def adl(self):
        return to_pydecimal(self._csdata.Adl)

    @adl.setter
    def adl(self, value):
        self._csdata.Adl = CsDecimal(value)

    @property
    def adl_sma(self):
        return to_pydecimal(self._csdata.AdlSma)

    @adl_sma.setter
    def adl_sma(self, value):
        self._csdata.AdlSma = CsDecimal(value)

T = TypeVar("T", bound=ADLResult)
class ADLResults(IndicatorResults[T]):
    """
    A wrapper class for the list of ADL(Accumulation/Distribution Line) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[T]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def to_quotes(self) -> Iterable[Quote]:
        quotes = CsIndicator.ConvertToQuotes(CsList(type(self._csdata[0]), self._csdata))

        return [ Quote.from_csquote(q) for q in quotes ]
