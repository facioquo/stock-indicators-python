from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_chaikin_osc(quotes: Iterable[Quote], fast_periods: int = 3, slow_periods: int = 10):
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


T = TypeVar("T", bound=ChaikinOscResult)
class ChaikinOscResults(RemoveWarmupMixin, IndicatorResults[T]):
    """
    A wrapper class for the list of Chaikin Oscillator results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
