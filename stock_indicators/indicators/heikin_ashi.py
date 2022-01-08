from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_heikin_ashi(quotes: Iterable[Quote]):
    """Get Heikin-Ashi calculated.
    
    Heikin-Ashi is a modified candlestick pattern that uses prior day for smoothing.
    
    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.
    
    Returns:
        `HeikinAshiResults[HeikinAshiResult]`
            HeikinAshiResults is list of HeikinAshiResult with providing useful helper methods.
    
    See more:
         - [Heikin-Ashi Channels Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/HeikinAshi/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetHeikinAshi[Quote](CsList(Quote, quotes))
    return HeikinAshiResults(results, HeikinAshiResult)

class HeikinAshiResult(ResultBase):
    """
    A wrapper class for a single unit of Heikin-Ashi results.
    """

    @property
    def open(self):
        return to_pydecimal(self._csdata.Open)

    @open.setter
    def open(self, value):
        self._csdata.Open = CsDecimal(value)
        
    @property
    def high(self):
        return to_pydecimal(self._csdata.High)
    
    @high.setter
    def high(self, value):
        self._csdata.High = CsDecimal(value)
        
    @property
    def low(self):
        return to_pydecimal(self._csdata.Low)
    
    @low.setter
    def low(self, value):
        self._csdata.Low = CsDecimal(value)
        
    @property
    def close(self):
        return to_pydecimal(self._csdata.Close)
    
    @close.setter
    def close(self, value):
        self._csdata.Close = CsDecimal(value)
        
    @property
    def volume(self):
        return to_pydecimal(self._csdata.Volume)
    
    @volume.setter
    def volume(self, value):
        self._csdata.Volume = CsDecimal(value)

T = TypeVar("T", bound=HeikinAshiResult)
class HeikinAshiResults(IndicatorResults[T]):
    """
    A wrapper class for the list of Heikin-Ashi results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[T]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def to_quotes(self) -> Iterable[Quote]:
        quotes = CsIndicator.ConvertToQuotes(CsList(type(self._csdata[0]), self._csdata))

        return [ Quote.from_csquote(q) for q in quotes ]
