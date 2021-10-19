from typing import Iterable, List, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_awesome(quotes: Iterable[Quote], fast_periods: int = 5, slow_periods: int = 34):
    awesome_results = CsIndicator.GetAwesome[Quote](CsList(Quote, quotes), fast_periods, slow_periods)
    return AwesomeResults(awesome_results, AwesomeResult)

class AwesomeResult(ResultBase):
    def __init__(self, awesome_result):
        super().__init__(awesome_result)

    @property
    def oscillator(self):
        return to_pydecimal(self._csdata.Oscillator)

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = CsDecimal(value)

    @property
    def normalized(self):
        return to_pydecimal(self._csdata.Normalized)

    @normalized.setter
    def normalized(self, value):
        self._csdata.Normalized = CsDecimal(value)

class AwesomeResults(IndicatorResults[AwesomeResult]):
    """
    A wrapper class for the list of Awesome Oscillator (aka Super AO) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: List, wrapper_class: Type[AwesomeResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        