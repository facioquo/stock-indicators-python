from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class ChaikinOscResult(ResultBase):
    """
    A wrapper class for a single unit of Chaikin Oscillator results.
    """

    @property
    def money_flow_multiplier(self) -> Optional[float]:
        return self._csdata.MoneyFlowMultiplier

    @money_flow_multiplier.setter
    def money_flow_multiplier(self, value):
        self._csdata.MoneyFlowMultiplier = value

    @property
    def money_flow_volume(self) -> Optional[float]:
        return self._csdata.MoneyFlowVolume

    @money_flow_volume.setter
    def money_flow_volume(self, value):
        self._csdata.MoneyFlowVolume = value

    @property
    def adl(self) -> Optional[float]:
        return self._csdata.Adl

    @adl.setter
    def adl(self, value):
        self._csdata.Adl = value

    @property
    def oscillator(self) -> Optional[float]:
        return self._csdata.Oscillator

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = value


_T = TypeVar("_T", bound=ChaikinOscResult)
class ChaikinOscResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Chaikin Oscillator results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """


class ChaikinOsc(Indicator):
    is_chainee = False
    is_chainor = True

    indicator_method = CsIndicator.GetChaikinOsc[Quote]
    chaining_method = None

    list_wrap_class = ChaikinOscResults
    unit_wrap_class = ChaikinOscResult


@calculate_indicator(indicator=ChaikinOsc())
def get_chaikin_osc(quotes: Iterable[Quote], fast_periods: int = 3,
                    slow_periods: int = 10) -> ChaikinOscResults[ChaikinOscResult]:
    """Get Chaikin Oscillator calculated.

    Chaikin Oscillator is the difference between fast and slow
    Exponential Moving Averages (EMA) of the Accumulation/Distribution Line (ADL).

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `fast_periods` : int, defaults 3
            Number of periods for the ADL fast EMA.

        `slow_periods` : int, defaults 10
            Number of periods for the ADL slow EMA.

    Returns:
        `ChaikinOscResults[ChaikinOscResult]`
            ChaikinOscResults is list of ChaikinOscResult with providing useful helper methods.

    See more:
         - [Chaikin Oscillator Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/ChaikinOsc/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, fast_periods, slow_periods)
