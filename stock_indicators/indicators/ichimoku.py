from decimal import Decimal
from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_ichimoku(quotes: Iterable[Quote], tenkan_periods: int = 9,
                 kijunPeriods: int = 26, senkouBPeriods: int = 52):
    """Get Ichimoku Cloud calculated.
    
    Ichimoku Cloud, also known as Ichimoku Kinkō Hyō, is a collection of indicators
    that depict support and resistance, momentum, and trend direction.
      
    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.
        
        `tenkan_periods` : int, defaults 9
            Number of periods in the lookback window.
        
        `kijunPeriods` : int, defaults 9
            Number of periods in the lookback window.
        
        `tenkan_periods` : int, defaults 9
            Number of periods in the lookback window.
        
        `tenkan_periods` : int, defaults 9
            Number of periods in the lookback window.
    
    Returns:
        `DonchianResults[DonchianResult]`
            DonchianResults is list of DonchianResult with providing useful helper methods.
    
    See more:
         - [Ichimoku Cloud Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Donchian/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetIchimoku[Quote](CsList(Quote, quotes),
                                             tenkan_periods,
                                             kijunPeriods,
                                             senkouBPeriods)
    return IchimokuResults(results, IchimokuResult)

class IchimokuResult(ResultBase):
    """
    A wrapper class for a single unit of Ichimoku Cloud results.
    """

    @property
    def tenkan_sen(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.TenkanSen)

    @tenkan_sen.setter
    def tenkan_sen(self, value):
        self._csdata.TenkanSen = CsDecimal(value)
        
    @property
    def kijun_sen(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.KijunSen)
    
    @kijun_sen.setter
    def kijun_sen(self, value):
        self._csdata.KijunSen = CsDecimal(value)
        
    @property
    def senkou_span_a(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.SenkouSpanA)
    
    @senkou_span_a.setter
    def senkou_span_a(self, value):
        self._csdata.SenkouSpanA = CsDecimal(value)
    
    @property
    def senkou_span_b(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.SenkouSpanB)
    
    @senkou_span_b.setter
    def senkou_span_b(self, value):
        self._csdata.SenkouSpanB = CsDecimal(value)
        
    @property
    def chikou_span(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.ChikouSpan)
    
    @chikou_span.setter
    def chikou_span(self, value):
        self._csdata.ChikouSpan = CsDecimal(value)

T = TypeVar("T", bound=IchimokuResult)
class IchimokuResults(IndicatorResults[T]):
    """
    A wrapper class for the list of Ichimoku Cloud results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[T]):
        super().__init__(data, wrapper_class)
