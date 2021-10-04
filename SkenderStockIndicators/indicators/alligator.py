from typing import Iterable, List, Optional, Type
from SkenderStockIndicators._cslib import CsIndicator
from SkenderStockIndicators._cstypes import List as CsList
from SkenderStockIndicators._cstypes import Decimal as CsDecimal
from SkenderStockIndicators._cstypes import to_pydecimal
from SkenderStockIndicators.indicators.common.results import IndicatorResults, ResultBase
from SkenderStockIndicators.indicators.common.quote import Quote

def get_alligator(quotes: Iterable[Quote]):
    alligator_results = CsIndicator.GetAlligator[Quote](CsList(Quote, quotes))
    return AlligatorResults(alligator_results, AlligatorResult)

class AlligatorResult(ResultBase):
    def __init__(self, alligator_result):
        super().__init__(alligator_result)

    @property
    def jaw(self):
        return to_pydecimal(self._csdata.Jaw)

    @jaw.setter
    def jaw(self, value):
        self._csdata.Jaw = CsDecimal(value)

    @property
    def teeth(self):
        return to_pydecimal(self._csdata.Teeth)

    @teeth.setter
    def teeth(self, value):
        self._csdata.Teeth = CsDecimal(value)

    @property
    def lips(self):
        return to_pydecimal(self._csdata.Lips)

    @lips.setter
    def lips(self, value):
        self._csdata.Lips = CsDecimal(value)

class AlligatorResults(IndicatorResults[AlligatorResult]):
    """
    A wrapper class for the list of Williams Alligator results. It is exactly same with built-in `list`
    except for that it provides some useful helper methods written in C# implementation.
    """

    def __init__(self, data: List, wrapper_class: Type[AlligatorResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
