from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_awesome(quotes: Iterable[Quote], fast_periods: int = 5, slow_periods: int = 34):
    """Get Awesome Oscillator calculated.
    
    Awesome Oscillator (aka Super AO) is a measure of the gap between a fast and slow period modified moving average.
    
    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.
        
        `fast_periods` : int, defaults 5
            Number of periods in the Fast moving average.
            
        `slow_periods` : int, defaults 34
            Number of periods in the Slow moving average.
    
    Returns:
        `AwesomeResults[AwesomeResult]`
            AwesomeResults is list of AwesomeResult with providing useful helper methods.
    
    See more:
         - [Awesome Oscillator Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Awesome/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    awesome_results = CsIndicator.GetAwesome[Quote](CsList(Quote, quotes), fast_periods, slow_periods)
    return AwesomeResults(awesome_results, AwesomeResult)

class AwesomeResult(ResultBase):
    """
    A wrapper class for a single unit of Awesome Oscillator results.
    """

    @property
    def oscillator(self) -> Optional[float]:
        return self._csdata.Oscillator

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = value

    @property
    def normalized(self) -> Optional[float]:
        return self._csdata.Normalized

    @normalized.setter
    def normalized(self, value):
        self._csdata.Normalized = value

T = TypeVar("T", bound=AwesomeResult)
class AwesomeResults(IndicatorResults[T]):
    """
    A wrapper class for the list of Awesome Oscillator (aka Super AO) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        