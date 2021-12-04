from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_beta(market_history: Iterable[Quote], eval_history: Iterable[Quote], lookback_periods: int):
    """Get Beta calculated.
    
    Beta shows how strongly one stock responds to systemic volatility of the entire market.
    
    Parameters:
        `market_history` : Iterable[Quotes]
            Historical price quotes for Market.

        `eval_history` : Iterable[Quotes]
            Historical price quotes for Evaluation.
        
        `lookback_periods` : int
            Number of periods in the lookback window.
    
    Returns:
        `BetaResults[BetaResult]`
            BetaResults is list of BetaResult with providing useful helper methods.
    
    See more:
         - [Beta Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Beta/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
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

T = TypeVar("T", bound=BetaResult)
class BetaResults(IndicatorResults[T]):
    """
    A wrapper class for the list of Beta results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[T]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        