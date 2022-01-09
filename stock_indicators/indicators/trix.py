from decimal import Decimal
from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_trix(quotes: Iterable[Quote], lookback_periods: int, signal_periods: Optional[int] = None):
    results = CsIndicator.GetTrix[Quote](CsList(Quote, quotes), lookback_periods, signal_periods)
    return TRIXResults(results, TRIXResult)

class TRIXResult(ResultBase):
    """
    A wrapper class for a single unit of Triple EMA Oscillator (TRIX) results.
    """

    @property
    def ema3(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Ema3)

    @ema3.setter
    def ema3(self, value):
        self._csdata.Ema3 = CsDecimal(value)

    @property
    def trix(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Trix)

    @trix.setter
    def trix(self, value):
        self._csdata.Trix = CsDecimal(value)

    @property
    def signal(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Signal)

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = CsDecimal(value)

T = TypeVar("T", bound=TRIXResult)
class TRIXResults(IndicatorResults[T]):
    """
    A wrapper class for the list of Triple EMA Oscillator (TRIX) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
