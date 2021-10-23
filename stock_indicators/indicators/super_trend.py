from typing import Iterable, List, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_super_trend(quotes: Iterable[Quote], lookback_periods: int = 10, multiplier: float = 3):
    super_trend_results = CsIndicator.GetSuperTrend[Quote](CsList(Quote, quotes), lookback_periods, CsDecimal(multiplier))
    return SuperTrendResults(super_trend_results, SuperTrendResult)

class SuperTrendResult(ResultBase):
    """
    A wrapper class for a single unit of Super Trend results.
    """

    def __init__(self, super_trend_result):
        super().__init__(super_trend_result)

    @property
    def super_trend(self):
        return to_pydecimal(self._csdata.SuperTrend)

    @super_trend.setter
    def super_trend(self, value):
        self._csdata.SuperTrend = CsDecimal(value)

    @property
    def upper_band(self):
        return to_pydecimal(self._csdata.UpperBand)
    
    @upper_band.setter
    def upper_band(self, value):
        self._csdata.UpperBand = CsDecimal(value)

    @property
    def lower_band(self):
        return to_pydecimal(self._csdata.LowerBand)

    @lower_band.setter
    def lower_band(self, value):
        self._csdata.LowerBand = CsDecimal(value)

class SuperTrendResults(IndicatorResults[SuperTrendResult]):
    """
    A wrapper class for the list of Super Trend results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: List, wrapper_class: Type[SuperTrendResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        