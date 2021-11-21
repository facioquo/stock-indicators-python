from typing import Iterable, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_beta(market_history: Iterable[Quote], eval_history: Iterable[Quote], lookback_periods: int):
    beta_results = CsIndicator.GetBeta[Quote](CsList(Quote, market_history), CsList(Quote, eval_history), lookback_periods)
    return BetaResults(beta_results, BetaResult)

class BetaResult(ResultBase):
    """
    A wrapper class for a single unit of Beta results.
    """

    @property
    def beta(self):
        return to_pydecimal(self._csdata.Beta)

    @beta.setter
    def beta(self, value):
        self._csdata.Beta = CsDecimal(value)

class BetaResults(IndicatorResults[BetaResult]):
    """
    A wrapper class for the list of Beta results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[BetaResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        