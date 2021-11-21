from typing import Iterable, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_elder_ray(quotes: Iterable[Quote], lookback_periods: int = 13):
    results = CsIndicator.GetElderRay[Quote](CsList(Quote, quotes), lookback_periods)
    return ElderRayResults(results, ElderRayResult)

class ElderRayResult(ResultBase):
    """
    A wrapper class for a single unit of Elder-ray Index results.
    """

    @property
    def ema(self):
        return to_pydecimal(self._csdata.Ema)

    @ema.setter
    def ema(self, value):
        self._csdata.Ema = CsDecimal(value)
        
    @property
    def bull_power(self):
        return to_pydecimal(self._csdata.BullPower)
    
    @bull_power.setter
    def bull_power(self, value):
        self._csdata.BullPower = CsDecimal(value)
        
    @property
    def bear_power(self):
        return to_pydecimal(self._csdata.BearPower)
    
    @bear_power.setter
    def bear_power(self, value):
        self._csdata.BearPower = CsDecimal(value)


class ElderRayResults(IndicatorResults[ElderRayResult]):
    """
    A wrapper class for the list of Elder-ray Index results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[ElderRayResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        