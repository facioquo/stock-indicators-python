from typing import Iterable, Optional, TypeVar, overload

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


@overload
def get_parabolic_sar(quotes: Iterable[Quote], acceleration_step: float = 0.02,
                      max_acceleration_factor: float = 0.2) -> "ParabolicSARResults[ParabolicSARResult]": ...
@overload
def get_parabolic_sar(quotes: Iterable[Quote], acceleration_step: float,
                      max_acceleration_factor: float, initial_factor: float) -> "ParabolicSARResults[ParabolicSARResult]": ...
def get_parabolic_sar(quotes, acceleration_step = None,
                      max_acceleration_factor = None, initial_factor = None):
    """Get Parabolic SAR calculated.

    Parabolic SAR (stop and reverse) is a price-time based indicator
    used to determine trend direction and reversals.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `acceleration_step` : float
            Incremental step size.

        `max_acceleration_factor` : float
            Maximum step threshold.

        `initial_factor` : float
            Initial starting acceleration factor.

    Returns:
        `ParabolicSARResults[ParabolicSARResult]`
            ParabolicSARResults is list of ParabolicSARResult with providing useful helper methods.

    See more:
         - [Parabolic SAR Reference](https://python.stockindicators.dev/indicators/ParabolicSar/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    if initial_factor is None:
        if acceleration_step is None: acceleration_step = 0.02
        if max_acceleration_factor is None: max_acceleration_factor = 0.2
        results = CsIndicator.GetParabolicSar[Quote](CsList(Quote, quotes), acceleration_step,
                                                 max_acceleration_factor)
    else:
        results = CsIndicator.GetParabolicSar[Quote](CsList(Quote, quotes), acceleration_step,
                                                 max_acceleration_factor, initial_factor)

    return ParabolicSARResults(results, ParabolicSARResult)


class ParabolicSARResult(ResultBase):
    """
    A wrapper class for a single unit of Parabolic SAR(stop and reverse) results.
    """

    @property
    def sar(self) -> Optional[float]:
        return self._csdata.Sar

    @sar.setter
    def sar(self, value):
        self._csdata.Sar = value

    @property
    def is_reversal(self) -> Optional[bool]:
        return self._csdata.IsReversal

    @is_reversal.setter
    def is_reversal(self, value):
        self._csdata.IsReversal = value


_T = TypeVar("_T", bound=ParabolicSARResult)
class ParabolicSARResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Parabolic SAR(stop and reverse) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
