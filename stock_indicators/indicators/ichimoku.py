from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_ichimoku(quotes: Iterable[Quote],
                 tenkan_periods: int = 9,
                 kijunPeriods: int = 26,
                 senkouBPeriods: int = 52):
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
    def tenkan_sen(self):
        return to_pydecimal(self._csdata.TenkanSen)

    @tenkan_sen.setter
    def tenkan_sen(self, value):
        self._csdata.TenkanSen = CsDecimal(value)
        
    @property
    def kijun_sen(self):
        return to_pydecimal(self._csdata.KijunSen)
    
    @kijun_sen.setter
    def kijun_sen(self, value):
        self._csdata.KijunSen = CsDecimal(value)
        
    @property
    def senkou_span_a(self):
        return to_pydecimal(self._csdata.SenkouSpanA)
    
    @senkou_span_a.setter
    def senkou_span_a(self, value):
        self._csdata.SenkouSpanA = CsDecimal(value)
    
    @property
    def senkou_span_b(self):
        return to_pydecimal(self._csdata.SenkouSpanB)
    
    @senkou_span_b.setter
    def senkou_span_b(self, value):
        self._csdata.SenkouSpanB = CsDecimal(value)
        
    @property
    def chikou_span(self):
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

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        