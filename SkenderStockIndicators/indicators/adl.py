from typing import Iterable, List, Optional, Type
from SkenderStockIndicators._cslib import CsIndicator
from SkenderStockIndicators._cstypes import List as CsList
from SkenderStockIndicators._cstypes import to_pydecimal
from SkenderStockIndicators.indicators.common.results import IndicatorResults, ResultBase
from SkenderStockIndicators.indicators.common.quote import Quote

def get_adl(quotes: Iterable[Quote], sma_periods: Optional[int] = None):
    adl_results = CsIndicator.GetAdl[Quote](CsList(Quote, quotes), sma_periods)
    return ADLResults(adl_results, ADLResult)


class ADLResult(ResultBase):
    def __init__(self, adl_result):
        super().__init__(adl_result)
        self.money_flow_multiplier = to_pydecimal(adl_result.MoneyFlowMultiplier)
        self.money_flow_volume = to_pydecimal(adl_result.MoneyFlowVolume)
        self.adl = to_pydecimal(adl_result.Adl)
        self.adl_sma = to_pydecimal(adl_result.AdlSma)

class ADLResults(IndicatorResults[ADLResult]):
    """
    A wrapper class for the list of ADL results. It is exactly same with built-in `list`
    except for that it provides some useful helper methods written in C# implementation.
    """

    def __init__(self, data, wrapper_class: Type[ADLResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def to_quotes(self) -> List[Quote]:
        quotes = CsIndicator.ConvertToQuotes(CsList(type(self._csdata[0]), self._csdata))

        return quotes