from typing import Iterable, Optional, TypeVar
from warnings import warn

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class SMAResult(ResultBase):
    """
    A wrapper class for a single unit of SMA results.
    """

    @property
    def sma(self) -> Optional[float]:
        return self._csdata.Sma

    @sma.setter
    def sma(self, value):
        self._csdata.Sma = value


_T = TypeVar("_T", bound=SMAResult)
class SMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of SMA(Simple Moving Average) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """


class SMA(Indicator):
    is_chainee = True
    is_chainor = True
    
    indicator_method = CsIndicator.GetSma[Quote]
    chaining_method = CsIndicator.GetSma
    
    list_wrap_class = SMAResults
    unit_wrap_class = SMAResult


class SMAAnalysisResult(SMAResult):
    """
    A wrapper class for a single unit of SMA Analysis results.
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


_T = TypeVar("_T", bound=SMAAnalysisResult)
class SMAAnalysisResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of SMA Analysis results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """


class SMAAnalysis(Indicator):
    is_chainee = True
    is_chainor = True
    
    indicator_method = CsIndicator.GetSmaAnalysis[Quote]
    chaining_method = CsIndicator.GetSmaAnalysis
    
    list_wrap_class = SMAAnalysisResults
    unit_wrap_class = SMAAnalysisResult


@calculate_indicator(indicator=SMA())
def get_sma(quotes: Iterable[Quote], lookback_periods: int) -> SMAResults[SMAResult]:
    """Get SMA calculated.

    Simple Moving Average (SMA) is the average of price over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

        `candle_part` : CandlePart, defaults CandlePart.CLOSE
            Selected OHLCV part.

    Returns:
        `SMAResults[SMAResult]`
            SMAResults is list of SMAResult with providing useful helper methods.

    See more:
         - [SMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Sma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, lookback_periods)

@calculate_indicator(indicator=SMAAnalysis())
def get_sma_analysis(quotes: Iterable[Quote], lookback_periods: int) -> SMAAnalysisResults[SMAAnalysisResult]:
    """Get SMA calculated, with more analysis.

    Simple Moving Average (SMA) is the average of price over a lookback window.
    This extended variant includes mean absolute deviation (MAD),
    mean square error (MSE), and mean absolute percentage error (MAPE).

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `SMAAnalysisResults[SMAAnalysisResult]`
            SMAAnalysisResults is list of SMAAnalysisResult with providing useful helper methods.

    See more:
         - [SMA-analysis Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Sma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, lookback_periods)

def get_sma_extended(quotes: Iterable[Quote], lookback_periods: int):
    warn('This method is deprecated. Use get_sma_analysis() instead.', DeprecationWarning, stacklevel=2)
    return get_sma_analysis(quotes, lookback_periods)

