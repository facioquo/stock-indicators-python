from decimal import Decimal
from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

# TODO: Need to support CandlePart Enum
def get_ema(quotes: Iterable[Quote], lookback_periods: int):
    """Get EMA calculated.
    
    Exponential Moving Average (EMA) of the Close price.
    
    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.
        
        `lookback_periods` : int
            Number of periods in the lookback window.
    
    Returns:
        `EMAResults[EMAResult]`
            EMAResults is list of EMAResult with providing useful helper methods.
    
    See more:
         - [EMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Ema/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    ema_list = CsIndicator.GetEma[Quote](CsList(Quote, quotes), lookback_periods)
    return EMAResults(ema_list, EMAResult)

class EMAResult(ResultBase):
    """
    A wrapper class for a single unit of EMA results.
    """

    @property
    def ema(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Ema)

    @ema.setter
    def ema(self, value):
        self._csdata.Ema = CsDecimal(value)

T = TypeVar("T", bound=EMAResult)
class EMAResults(IndicatorResults[T]):
    """
    A wrapper class for the list of EMA(Exponential Moving Average) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
