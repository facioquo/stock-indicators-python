from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_macd(quotes: Iterable[Quote], fast_periods: int = 12,
             slow_periods: int = 26, signal_periods: int = 9,
             candle_part: CandlePart = CandlePart.CLOSE):
    """Get MACD calculated.

    Moving Average Convergence/Divergence (MACD) is a simple oscillator view
    of two converging/diverging exponential moving averages.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `fast_periods` : int, defaults 12
            Number of periods in the Fast EMA.

        `slow_periods` : int, defaults 26
            Number of periods in the Slow EMA.

        `signal_periods` : int, defaults 9
            Number of periods for the Signal moving average.

        `candle_part` : CandlePart, defaults CandlePart.CLOSE
            Selected OHLCV part.

    Returns:
        `MACDResults[MACDResult]`
            MACDResults is list of MACDResult with providing useful helper methods.

    See more:
         - [MACD Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Macd/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    macd_results = CsIndicator.GetMacd[Quote](CsList(Quote, quotes), fast_periods,
                                              slow_periods, signal_periods,
                                              candle_part)
    return MACDResults(macd_results, MACDResult)


class MACDResult(ResultBase):
    """
    A wrapper class for a single unit of MACD results.
    """

    @property
    def macd(self) -> Optional[float]:
        return self._csdata.Macd

    @macd.setter
    def macd(self, value):
        self._csdata.Macd = value

    @property
    def signal(self) -> Optional[float]:
        return self._csdata.Signal

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = value

    @property
    def histogram(self) -> Optional[float]:
        return self._csdata.Histogram

    @histogram.setter
    def histogram(self, value):
        self._csdata.Histogram = value

    @property
    def fast_ema(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.FastEma)

    @fast_ema.setter
    def fast_ema(self, value):
        self._csdata.FastEma = CsDecimal(value)

    @property
    def slow_ema(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.SlowEma)

    @slow_ema.setter
    def slow_ema(self, value):
        self._csdata.SlowEma = CsDecimal(value)


_T = TypeVar("_T", bound=MACDResult)
class MACDResults(RemoveWarmupMixin ,IndicatorResults[_T]):
    """
    A wrapper class for the list of MACD(Moving Average Convergence/Divergence) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
