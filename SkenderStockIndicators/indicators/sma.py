from typing import Iterable, Optional, Type
from SkenderStockIndicators._cslib import CsIndicator
from SkenderStockIndicators._cstypes import List as CsList
from SkenderStockIndicators._cstypes import Decimal as CsDecimal
from SkenderStockIndicators._cstypes import to_pydecimal
from SkenderStockIndicators.indicators.common.results import IndicatorResults, ResultBase
from SkenderStockIndicators.indicators.common.quote import Quote


def get_sma(quotes: Iterable[Quote], lookback_periods: int):
    sma_list = CsIndicator.GetSma[Quote](CsList(Quote, quotes), lookback_periods)
    return SMAResults(sma_list, SMAResult)

def get_sma_extended(quotes: Iterable[Quote], lookback_periods: int):
    sma_extended_list = CsIndicator.GetSmaExtended[Quote](CsList(Quote, quotes), lookback_periods)
    return SMAExtendedResults(sma_extended_list, SMAExtendedResult)

def validate_sma(quotes: Iterable[Quote], lookback_periods: int) -> None:
    CsIndicator.ValidateSma[Quote](CsList(Quote, quotes), lookback_periods) 


class SMAResult(ResultBase):
    def __init__(self, sma_result):
        super().__init__(sma_result)

    @property
    def sma(self):
        return to_pydecimal(self._csdata.Sma)

    @sma.setter
    def sma(self, value):
        self._csdata.Sma = CsDecimal(value)


class SMAResults(IndicatorResults[SMAResult]):
    """
    A wrapper class for the list of SMA results. It is exactly same with built-in `list`
    except for that it provides some useful helper methods written in CSharp implementation.
    """

    def __init__(self, data, wrapper_class: Type[SMAResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)

class SMAExtendedResult(SMAResult):
    def __init__(self, sma_extended_result):
        super().__init__(sma_extended_result)

    @property
    def mad(self):
        return to_pydecimal(self._csdata.Mad)
    
    @mad.setter
    def mad(self, value):
        self._csdata.Mad = CsDecimal(value)
    
    @property
    def mse(self):
        return to_pydecimal(self._csdata.Mse)
    
    @mse.setter
    def mse(self, value):
        self._csdata.Mse = CsDecimal(value)
    
    @property
    def mape(self):
        return to_pydecimal(self._csdata.Mape)
    
    @mape.setter
    def mape(self, value):
        self._csdata.Mape = CsDecimal(value)

class SMAExtendedResults(IndicatorResults[SMAExtendedResult]):
    """
    A wrapper class for the list of SMA-Extended results. It is exactly same with built-in `list`
    except for that it provides some useful helper methods written in CSharp implementation.
    """

    def __init__(self, data, wrapper_class: Type[SMAExtendedResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        