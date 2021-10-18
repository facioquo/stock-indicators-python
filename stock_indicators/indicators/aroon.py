from typing import Iterable, List, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_aroon(quotes: Iterable[Quote], lookback_periods: int = 25):
    aroon_results = CsIndicator.GetAroon[Quote](CsList(Quote, quotes), lookback_periods)
    return AroonResults(aroon_results, AroonResult)

class AroonResult(ResultBase):
    def __init__(self, aroon_result):
        super().__init__(aroon_result)

    @property
    def aroon_up(self):
        return to_pydecimal(self._csdata.AroonUp)

    @aroon_up.setter
    def aroon_up(self, value):
        self._csdata.AroonUp = CsDecimal(value)

    @property
    def aroon_down(self):
        return to_pydecimal(self._csdata.AroonDown)

    @aroon_down.setter
    def aroon_down(self, value):
        self._csdata.AroonDown = CsDecimal(value)

    @property
    def oscillator(self):
        return to_pydecimal(self._csdata.Oscillator)

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = CsDecimal(value)

class AroonResults(IndicatorResults[AroonResult]):
    """
    A wrapper class for the list of Aroon results. It is exactly same with built-in `list`
    except for that it provides some useful helper methods written in C# implementation.
    """

    def __init__(self, data: List, wrapper_class: Type[AroonResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        