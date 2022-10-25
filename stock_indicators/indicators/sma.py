from typing import Iterable, Optional, TypeVar
from warnings import warn

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.chain import chainable
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def _wrap_results(results):
    return SMAResults(results, SMAResult)

def _calculate(indicator_params, is_chaining):
    if is_chaining:
        return CsIndicator.GetSma(*indicator_params)
    else:
        quotes, *params, candle_part = indicator_params
        quotes = Quote.use(quotes, candle_part) # Error occurs if not assigned to local var.
        return CsIndicator.GetSma(quotes, *params)

@chainable(is_chainable=True, calc_func=_calculate, wrap_func=_wrap_results)
def get_sma(quotes: Iterable[Quote], lookback_periods: int,
            candle_part: CandlePart = CandlePart.CLOSE):
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
    return (quotes, lookback_periods, candle_part)

def get_sma_analysis(quotes: Iterable[Quote], lookback_periods: int):
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
    sma_extended_list = CsIndicator.GetSmaAnalysis[Quote](CsList(Quote, quotes), lookback_periods)
    return SMAAnalysisResults(sma_extended_list, SMAAnalysisResult)

def get_sma_extended(quotes: Iterable[Quote], lookback_periods: int):
    warn('This method is deprecated. Use get_sma_analysis() instead.', DeprecationWarning, stacklevel=2)
    return get_sma_analysis(quotes, lookback_periods)


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
