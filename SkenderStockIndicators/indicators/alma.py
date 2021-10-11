from typing import Iterable, Optional, Type
from SkenderStockIndicators._cslib import CsIndicator
from SkenderStockIndicators._cstypes import to_pydecimal
from SkenderStockIndicators._cstypes import List as CsList
from SkenderStockIndicators._cstypes import Decimal as CsDecimal
from SkenderStockIndicators.indicators.common.quote import Quote
from SkenderStockIndicators.indicators.common.results import IndicatorResults, ResultBase

def get_alma(quotes: Iterable[Quote], lookback_periods: int = 9, offset: float = .85, sigma : float = 6):
    alma_results = CsIndicator.GetAlma[Quote](CsList(Quote, quotes), lookback_periods, offset, sigma)
    return ALMAResults(alma_results, ALMAResult)

class ALMAResult(ResultBase):
    def __init__(self, alma_result):
        super().__init__(alma_result)

    @property
    def alma(self):
        return to_pydecimal(self._csdata.Alma)

    @alma.setter
    def alma(self, value):
        self._csdata.Alma = CsDecimal(value)

class ALMAResults(IndicatorResults[ALMAResult]):
    """
    A wrapper class for the list of ALMA(Arnaud Legoux Moving Average) results. 
    It is exactly same with built-in `list` except for that it provides 
    some useful helper methods written in CSharp implementation.
    """
    def __init__(self, data: Iterable, wrapper_class: Type[ALMAResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
