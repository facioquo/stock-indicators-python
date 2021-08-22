from typing import Iterable, Optional, Type
from Skender.Stock.Indicators import Indicator
from SkenderStockIndicators._cstypes import List as CsList
from SkenderStockIndicators._cstypes import to_pydecimal
from SkenderStockIndicators.indicators.common.results import IndicatorResults, ResultBase
from SkenderStockIndicators.indicators.common.quote import Quote


def get_sma(quotes: Iterable[Quote], lookback_periods: int):
    sma_list = Indicator.GetSma[Quote](CsList(Quote, quotes), lookback_periods)
    return SMAResults(sma_list, SMAResult)

def get_sma_extended(quotes: Iterable[Quote], lookback_periods: int):
    sma_extended_list = Indicator.GetSmaExtended[Quote](CsList(Quote, quotes), lookback_periods)
    return SMAResults(sma_extended_list, SMAExtendedResult)

def validate_sma(quotes: Iterable[Quote], lookback_periods: int) -> None:
    Indicator.ValidateSma[Quote](CsList(Quote, quotes), lookback_periods) 


class SMAResult(ResultBase):
    def __init__(self, sma_result):
        super().__init__(sma_result)
        self.Sma = to_pydecimal(sma_result.Sma)


class SMAExtendedResult(SMAResult):
    def __init__(self, sma_extended_result):
        super().__init__(sma_extended_result)
        self.Mad = to_pydecimal(sma_extended_result.Mad)
        self.Mse = to_pydecimal(sma_extended_result.Mse)
        self.Mape = to_pydecimal(sma_extended_result.Mape)


class SMAResults(IndicatorResults[SMAResult]):
    """
    A wrapper class for the list of SMA results. It is exactly same with built-in `list`
    except for that it provides some useful helper methods written in CSharp implementation.
    """

    def __init__(self, data, wrapper_class: Type[SMAResult]):
        super().__init__(data, wrapper_class)

    
    # For overloading.
    # @overload
    # def remove_warmup_periods(self) -> "SMAResults": ...
    # @overload
    # def remove_warmup_periods(self, remove_periods: int) -> "SMAResults": ...

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = Indicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)

