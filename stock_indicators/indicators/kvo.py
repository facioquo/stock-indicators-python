from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_kvo(quotes: Iterable[Quote], fast_periods: int = 34,
            slow_periods: int = 55, signal_periods: int = 13):
    """Get KVO calculated.

    Klinger Volume Oscillator (KVO) depicts volume-based divergence
    between short and long-term money flow.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `fast_periods` : int, defaults 34
            Number of periods for the short EMA.

        `slow_periods` : int, defaults 55
            Number of periods for the long EMA.

        `signal_periods` : int, defaults 13
            Number of periods Signal line.

    Returns:
        `KVOResults[KVOResult]`
            KVOResults is list of KVOResult with providing useful helper methods.

    See more:
         - [KVO Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Kvo/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetKvo[Quote](CsList(Quote, quotes), fast_periods,
                                        slow_periods, signal_periods)
    return KVOResults(results, KVOResult)


class KVOResult(ResultBase):
    """
    A wrapper class for a single unit of Klinger Volume Oscillator (KVO) results.
    """

    @property
    def oscillator(self) -> Optional[float]:
        return self._csdata.Oscillator

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = value

    @property
    def signal(self) -> Optional[float]:
        return self._csdata.Signal

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = value


_T = TypeVar("_T", bound=KVOResult)
class KVOResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Klinger Volume Oscillator (KVO) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
