from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_ema(quotes: Iterable[Quote], lookback_periods: int,
            candle_part: CandlePart = CandlePart.CLOSE):
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
         - [EMA Reference](https://python.stockindicators.dev/indicators/Ema/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    quotes = Quote.use(quotes, candle_part) # Error occurs if not assigned to local var.
    ema_list = CsIndicator.GetEma(quotes, lookback_periods)
    return EMAResults(ema_list, EMAResult)


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
