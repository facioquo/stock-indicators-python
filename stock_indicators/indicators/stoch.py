from typing import Iterable, List, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_stoch(quotes: Iterable[Quote], lookback_periods: int = 14, signal_periods: int = 3, smooth_periods: int = 3):
    stoch_results = CsIndicator.GetStoch[Quote](CsList(Quote, quotes), lookback_periods, signal_periods, smooth_periods)
    return StochResults(stoch_results, StochResult)

class StochResult(ResultBase):
    """
    A wrapper class for a single unit of Stochastic Oscillator and KDJ Index results.
    """

    def __init__(self, macd_result):
        super().__init__(macd_result)

    @property
    def oscillator(self):
        return to_pydecimal(self._csdata.Oscillator)

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = CsDecimal(value)

    @property
    def signal(self):
        return to_pydecimal(self._csdata.Signal)

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = CsDecimal(value)

    @property
    def percent_j(self):
        return to_pydecimal(self._csdata.PercentJ)

    @percent_j.setter
    def percent_j(self, value):
        self._csdata.PercentJ = CsDecimal(value)

    k = oscillator
    d = signal
    j = percent_j


class StochResults(IndicatorResults[StochResult]):
    """
    A wrapper class for the list of Stochastic Oscillator and KDJ Index results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: List, wrapper_class: Type[StochResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        