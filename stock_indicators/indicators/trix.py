from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_trix(quotes: Iterable[Quote], lookback_periods: int, signal_periods: Optional[int] = None):
    """Get TRIX calculated.

    Triple EMA Oscillator (TRIX) is the rate of change for a 3 EMA smoothing of the Close price over a lookback window.
    TRIX is often confused with TEMA.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

        `signal_periods` : int, optional
            Number of periods for a TRIX SMA signal line.

    Returns:
        `TRIXResults[TRIXResult]`
            TRIXResults is list of TRIXResult with providing useful helper methods.

    See more:
         - [TRIX Reference](https://python.stockindicators.dev/indicators/Trix/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetTrix[Quote](CsList(Quote, quotes), lookback_periods, signal_periods)
    return TRIXResults(results, TRIXResult)


class TRIXResult(ResultBase):
    """
    A wrapper class for a single unit of Triple EMA Oscillator (TRIX) results.
    """

    @property
    def ema3(self) -> Optional[float]:
        return self._csdata.Ema3

    @ema3.setter
    def ema3(self, value):
        self._csdata.Ema3 = value

    @property
    def trix(self) -> Optional[float]:
        return self._csdata.Trix

    @trix.setter
    def trix(self, value):
        self._csdata.Trix = value

    @property
    def signal(self) -> Optional[float]:
        return self._csdata.Signal

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = value


_T = TypeVar("_T", bound=TRIXResult)
class TRIXResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Triple EMA Oscillator (TRIX) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
