from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_roc(quotes: Iterable[Quote], lookback_periods: int, sma_periods: int = None):
    results = CsIndicator.GetRoc[Quote](CsList(Quote, quotes), lookback_periods, sma_periods)
    return ROCResults(results, ROCResult)

def get_roc_with_band(quotes: Iterable[Quote], lookback_periods: int, ema_periods: int, std_dev_periods: int):
    results = CsIndicator.GetRocWb[Quote](CsList(Quote, quotes), lookback_periods, ema_periods, std_dev_periods)
    return ROCWBResults(results, ROCWBResult)

class ROCResult(ResultBase):
    """
    A wrapper class for a single unit of ROC results.
    """

    @property
    def roc(self) -> Optional[float]:
        return to_pydecimal(self._csdata.Roc)

    @roc.setter
    def roc(self, value):
        self._csdata.Roc = CsDecimal(value)
        
    @property
    def roc_sma(self) -> Optional[float]:
        return to_pydecimal(self._csdata.RocSma)

    @roc_sma.setter
    def roc_sma(self, value):
        self._csdata.RocSma = CsDecimal(value)
        
T = TypeVar("T", bound=ROCResult)
class ROCResults(IndicatorResults[T]):
    """
    A wrapper class for the list of ROC(Rate of Change) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        

class ROCWBResult(ResultBase):
    """
    A wrapper class for a single unit of ROC with band results.
    """

    @property
    def roc(self) -> Optional[float]:
        return to_pydecimal(self._csdata.Roc)

    @roc.setter
    def roc(self, value):
        self._csdata.Roc = CsDecimal(value)
        
    @property
    def roc_ema(self) -> Optional[float]:
        return to_pydecimal(self._csdata.RocEma)

    @roc_ema.setter
    def roc_ema(self, value):
        self._csdata.RocEma = CsDecimal(value)
        
    @property
    def upper_band(self) -> Optional[float]:
        return to_pydecimal(self._csdata.UpperBand)
    
    @upper_band.setter
    def upper_band(self, value):
        self._csdata.UpperBand = CsDecimal(value)
        
    @property
    def lower_band(self) -> Optional[float]:
        return to_pydecimal(self._csdata.LowerBand)
    
    @lower_band.setter
    def lower_band(self, value):
        self._csdata.LowerBand = CsDecimal(value)
        
T = TypeVar("T", bound=ROCWBResult)
class ROCWBResults(IndicatorResults[T]):
    """
    A wrapper class for the list of ROC(Rate of Change) with band results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
