from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin, ToQuotesMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_hurst(quotes: Iterable[Quote], lookback_periods: int = 100):
    """Get Hurst Exponent calculated.

    Hurst Exponent is a measure of randomness, trending, and
    mean-reverting tendencies of incremental return values.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 100
            Number of lookback periods.

    Returns:
        `HurstResults[HurstResult]`
            HurstResults is list of HurstResult with providing useful helper methods.

    See more:
         - [Hurst Exponent Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Hurst/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetHurst[Quote](CsList(Quote, quotes), lookback_periods)
    return HurstResults(results, HurstResult)


class HurstResult(ResultBase):
    """
    A wrapper class for a single unit of Hurst Exponent results.
    """

    @property
    def hurst_exponent(self) -> Optional[float]:
        return self._csdata.HurstExponent

    @hurst_exponent.setter
    def hurst_exponent(self, value):
        self._csdata.HurstExponent = value


_T = TypeVar("_T", bound=HurstResult)
class HurstResults(ToQuotesMixin, RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Hurst Exponent results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
