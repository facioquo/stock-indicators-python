from typing import Iterable, List, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_macd(quotes: Iterable[Quote], fast_periods: int = 12, slow_periods: int = 26, signal_periods: int = 9):
    macd_results = CsIndicator.GetMacd[Quote](CsList(Quote, quotes), fast_periods, slow_periods, signal_periods)
    return MACDResults(macd_results, MACDResult)

class MACDResult(ResultBase):
    """
    A wrapper class for a single unit of MACD results.
    """

    def __init__(self, macd_result):
        super().__init__(macd_result)

    @property
    def macd(self):
        return to_pydecimal(self._csdata.Macd)

    @macd.setter
    def macd(self, value):
        self._csdata.Macd = CsDecimal(value)

    @property
    def signal(self):
        return to_pydecimal(self._csdata.Signal)

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = CsDecimal(value)

    @property
    def histogram(self):
        return to_pydecimal(self._csdata.Histogram)

    @histogram.setter
    def histogram(self, value):
        self._csdata.Histogram = CsDecimal(value)


class MACDResults(IndicatorResults[MACDResult]):
    """
    A wrapper class for the list of MACD(Moving Average Convergence/Divergence) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: List, wrapper_class: Type[MACDResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        