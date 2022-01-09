from decimal import Decimal
from typing import Iterable, Optional, Type, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_sma(quotes: Iterable[Quote], lookback_periods: int):
    """Get SMA calculated.
    
    Simple Moving Average (SMA) is the average of Close price over a lookback window.
    
    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.
        
        `lookback_periods` : int
            Number of periods in the lookback window.
    
    Returns:
        `SMAResults[SMAResult]`
            SMAResults is list of SMAResult with providing useful helper methods.
    
    See more:
         - [SMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Sma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    sma_list = CsIndicator.GetSma[Quote](CsList(Quote, quotes), lookback_periods)
    return SMAResults(sma_list, SMAResult)

def get_sma_extended(quotes: Iterable[Quote], lookback_periods: int):
    """Get SMA calculated, with extra properties.
    
    Simple Moving Average (SMA) is the average of Close price over a lookback window.
    This extended variant includes mean absolute deviation (MAD), mean square error (MSE),
    and mean absolute percentage error (MAPE).

    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.
        
        `lookback_periods` : int
            Number of periods in the lookback window.
    
    Returns:
        `SMAExtendedResults[SMAExtendedResult]`
            SMAExtendedResults is list of SMAExtendedResult with providing useful helper methods.
    
    See more:
         - [SMA-extended Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Sma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    sma_extended_list = CsIndicator.GetSmaExtended[Quote](CsList(Quote, quotes), lookback_periods)
    return SMAExtendedResults(sma_extended_list, SMAExtendedResult)

class SMAResult(ResultBase):
    """
    A wrapper class for a single unit of SMA results.
    """

    @property
    def sma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Sma)

    @sma.setter
    def sma(self, value):
        self._csdata.Sma = CsDecimal(value)

T = TypeVar("T", bound=SMAResult)
class SMAResults(IndicatorResults[T]):
    """
    A wrapper class for the list of SMA(Simple Moving Average) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[T]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)

class SMAExtendedResult(SMAResult):
    """
    A wrapper class for a single unit of SMA-Extended results.
    """

    @property
    def mad(self) -> Optional[float]:
        return self._csdata.Mad

    @mad.setter
    def mad(self, value):
        self._csdata.Mad = value

    @property
    def mse(self) -> Optional[float]:
        return self._csdata.Mse

    @mse.setter
    def mse(self, value):
        self._csdata.Mse = value

    @property
    def mape(self) -> Optional[float]:
        return self._csdata.Mape

    @mape.setter
    def mape(self, value):
        self._csdata.Mape = value

T = TypeVar("T", bound=SMAExtendedResult)
class SMAExtendedResults(IndicatorResults[T]):
    """
    A wrapper class for the list of SMA-Extended results. It is exactly same with built-in `list`
    except for that it provides some useful helper methods written in CSharp implementation.
    """

    def __init__(self, data: Iterable, wrapper_class: Type[T]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        