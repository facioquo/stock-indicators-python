from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_stoch_rsi(quotes: Iterable[Quote], rsi_periods: int, stoch_periods: int, signal_periods: int, smooth_periods: int = 1):
    """Get Stochastic RSI calculated.

    Stochastic RSI is a Stochastic interpretation of the Relative Strength Index.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `rsi_periods` : int
            Number of periods for the RSI.

        `stoch_periods` : int
            Number of periods for the Stochastic.

        `signal_periods` : int
            Number of periods for the Stochastic RSI SMA signal line.

        `smooth_periods` : int, defaults 1
            Number of periods for Stochastic Smoothing.  Use 1 for Fast or 3 for Slow.

    Returns:
        `StochRSIResults[StochRSIResult]`
            StochRSIResults is list of StochRSIResult with providing useful helper methods.

    See more:
         - [Stochastic RSI Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/StochRsi/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    stoch_rsi_results = CsIndicator.GetStochRsi[Quote](CsList(Quote, quotes), rsi_periods, stoch_periods, signal_periods, smooth_periods)
    return StochRSIResults(stoch_rsi_results, StochRSIResult)


class StochRSIResult(ResultBase):
    """
    A wrapper class for a single unit of Stochastic RSI results.
    """

    @property
    def stoch_rsi(self) -> Optional[float]:
        return self._csdata.StochRsi

    @stoch_rsi.setter
    def stoch_rsi(self, value):
        self._csdata.StochRsi = value

    @property
    def signal(self) -> Optional[float]:
        return self._csdata.Signal

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = value


_T = TypeVar("_T", bound=StochRSIResult)
class StochRSIResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Stochastic RSI results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
