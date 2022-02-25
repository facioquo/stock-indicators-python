from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_elder_ray(quotes: Iterable[Quote], lookback_periods: int = 13):
    """Get Elder-ray Index calculated.

    The Elder-ray Index depicts buying and selling pressure, also known as Bull and Bear Power.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 13
            Number of periods for the EMA.

    Returns:
        `ElderRayResults[ElderRayResult]`
            ElderRayResults is list of ElderRayResult with providing useful helper methods.

    See more:
         - [Elder-ray Index Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/ElderRay/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetElderRay[Quote](CsList(Quote, quotes), lookback_periods)
    return ElderRayResults(results, ElderRayResult)


class ElderRayResult(ResultBase):
    """
    A wrapper class for a single unit of Elder-ray Index results.
    """

    @property
    def ema(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Ema)

    @ema.setter
    def ema(self, value):
        self._csdata.Ema = CsDecimal(value)

    @property
    def bull_power(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.BullPower)

    @bull_power.setter
    def bull_power(self, value):
        self._csdata.BullPower = CsDecimal(value)

    @property
    def bear_power(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.BearPower)

    @bear_power.setter
    def bear_power(self, value):
        self._csdata.BearPower = CsDecimal(value)


_T = TypeVar("_T", bound=ElderRayResult)
class ElderRayResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Elder-ray Index results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
