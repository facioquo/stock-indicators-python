from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class EMAResult(ResultBase):
    """
    A wrapper class for a single unit of EMA results.
    """

    @property
    def ema(self) -> Optional[float]:
        return self._csdata.Ema

    @ema.setter
    def ema(self, value):
        self._csdata.Ema = value


_T = TypeVar("_T", bound=EMAResult)
class EMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of EMA(Exponential Moving Average) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """


class EMA(Indicator):
    is_chainee = True
    is_chainor = True
    
    indicator_method = CsIndicator.GetEma[Quote]
    chaining_method = CsIndicator.GetEma
    
    list_wrap_class = EMAResults
    unit_wrap_class = EMAResult


@calculate_indicator(indicator=EMA())
def get_ema(quotes: Iterable[Quote], lookback_periods: int) -> EMAResults[EMAResult]:
    """Get EMA calculated.

    Exponential Moving Average (EMA) of the Close price.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

        `candle_part` : CandlePart, defaults CandlePart.CLOSE
            Selected OHLCV part.

    Returns:
        `EMAResults[EMAResult]`
            EMAResults is list of EMAResult with providing useful helper methods.

    See more:
         - [EMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Ema/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, lookback_periods)
