from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_chaikin_osc(quotes: Iterable[Quote], fast_periods: int = 3, slow_periods: int = 10):
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
    results = CsIndicator.GetChaikinOsc[Quote](CsList(Quote, quotes), fast_periods, slow_periods)
    return ChaikinOscResults(results, ChaikinOscResult)


class ChaikinOscResult(ResultBase):
    """
    A wrapper class for a single unit of Chaikin Oscillator results.
    """

    @property
    def money_flow_multiplier(self) -> float:
        return self._csdata.MoneyFlowMultiplier

    @money_flow_multiplier.setter
    def money_flow_multiplier(self, value):
        self._csdata.MoneyFlowMultiplier = value

    @property
    def money_flow_volume(self) -> float:
        return self._csdata.MoneyFlowVolume

    @money_flow_volume.setter
    def money_flow_volume(self, value):
        self._csdata.MoneyFlowVolume = value

    @property
    def adl(self) -> float:
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
