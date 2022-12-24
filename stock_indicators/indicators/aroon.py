from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class AroonResult(ResultBase):
    """
    A wrapper class for a single unit of Aroon results.
    """

    @property
    def aroon_up(self) -> Optional[float]:
        return self._csdata.AroonUp

    @aroon_up.setter
    def aroon_up(self, value):
        self._csdata.AroonUp = value

    @property
    def aroon_down(self) -> Optional[float]:
        return self._csdata.AroonDown

    @aroon_down.setter
    def aroon_down(self, value):
        self._csdata.AroonDown = value

    @property
    def oscillator(self) -> Optional[float]:
        return self._csdata.Oscillator

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = value


_T = TypeVar("_T", bound=AroonResult)
class AroonResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Aroon results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """


class Aroon(Indicator):
    is_chainee = False
    is_chainor = True

    indicator_method = CsIndicator.GetAroon[Quote]
    chaining_method = None

    list_wrap_class = AroonResults
    unit_wrap_class = AroonResult


@calculate_indicator(indicator=Aroon())
def get_aroon(quotes: Iterable[Quote], lookback_periods: int = 25) -> AroonResults[AroonResult]:
    """Get Aroon calculated.

    Aroon is a simple oscillator view of how long the new high or low price occured over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 25
            Number of periods in the lookback window.

    Returns:
        `AroonResults[AroonResult]`
            AroonResults is list of AroonResult with providing useful helper methods.

    See more:
         - [Aroon Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Aroon/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, lookback_periods)
