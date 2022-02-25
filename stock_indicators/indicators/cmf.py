from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_cmf(quotes: Iterable[Quote], lookback_periods: int = 20):
    """Get CMF calculated.

    Chaikin Money Flow (CMF) is the simple moving average
    of Money Flow Volume (MFV).

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 20
            Number of periods for the MFV moving average.

    Returns:
        `CMFResults[CMFResult]`
            CMFResults is list of CMFResult with providing useful helper methods.

    See more:
         - [CMF Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Cmf/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetCmf[Quote](CsList(Quote, quotes), lookback_periods)
    return CMFResults(results, CMFResult)


class CMFResult(ResultBase):
    """
    A wrapper class for a single unit of Chaikin Money Flow (CMF) results.
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
    def cmf(self) -> Optional[float]:
        return self._csdata.Cmf

    @cmf.setter
    def cmf(self, value):
        self._csdata.Cmf = value


_T = TypeVar("_T", bound=CMFResult)
class CMFResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Chaikin Money Flow (CMF) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
