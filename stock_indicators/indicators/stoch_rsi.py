from typing import Iterable, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_stoch_rsi(quotes: Iterable[Quote], rsi_periods: int, stoch_periods: int, signal_periods: int, smooth_periods: int = 1):
    stoch_rsi_results = CsIndicator.GetStochRsi[Quote](CsList(Quote, quotes), rsi_periods, stoch_periods, signal_periods, smooth_periods)
    return StochRSIResults(stoch_rsi_results, StochRSIResult)

class StochRSIResult(ResultBase):
    """
    A wrapper class for a single unit of Stochastic RSI results.
    """

    def __init__(self, stoch_rsi_result):
        super().__init__(stoch_rsi_result)

    @property
    def stoch_rsi(self):
        return to_pydecimal(self._csdata.StochRsi)

    @stoch_rsi.setter
    def stoch_rsi(self, value):
        self._csdata.StochRsi = CsDecimal(value)

    @property
    def signal(self):
        return to_pydecimal(self._csdata.Signal)

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = CsDecimal(value)

class StochRSIResults(IndicatorResults[StochRSIResult]):
    """
    A wrapper class for the list of Stochastic RSI results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[StochRSIResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        