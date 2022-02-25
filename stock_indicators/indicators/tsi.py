from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_tsi(quotes: Iterable[Quote], lookback_periods: int = 25,
           smooth_periods: int = 13, signal_periods: int = 7):
    """Get TSI calculated.

    True Strength Index (TSI) is a momentum oscillator
    that depicts trends in price changes.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 25
           Number of periods for the first EMA.

        `smooth_periods` : int, defaults 13
            Number of periods in the second smoothing.

        `signal_periods` : int, defaults 7
            Number of periods in the TSI SMA signal line.

    Returns:
        `TSIResults[TSIResult]`
            TSIResults is list of TSIResult with providing useful helper methods.

    See more:
         - [TSI Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Tsi/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetTsi[Quote](CsList(Quote, quotes), lookback_periods,
                                       smooth_periods, signal_periods)
    return TSIResults(results, TSIResult)


class TSIResult(ResultBase):
    """
    A wrapper class for a single unit of True Strength Index (TSI) results.
    """

    @property
    def tsi(self) -> Optional[float]:
        return self._csdata.Tsi

    @tsi.setter
    def tsi(self, value):
        self._csdata.Tsi = value

    @property
    def signal(self) -> Optional[float]:
        return self._csdata.Signal

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = value


_T = TypeVar("_T", bound=TSIResult)
class TSIResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of True Strength Index (TSI) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
