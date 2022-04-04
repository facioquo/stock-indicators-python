from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.enums import PivotPointType
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_rolling_pivots(quotes: Iterable[Quote], window_periods: int,
                      offset_periods: int, point_type: PivotPointType = PivotPointType.STANDARD):
    """Get Rolling Pivot Points calculated.

    Rolling Pivot Points is a modern update to traditional fixed calendar window Pivot Points.
    It depicts support and resistance levels, based on a defined rolling window and offset.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `window_periods` : int
            Number of periods in the evaluation window.

        `offset_periods` : int
            Number of periods to offset the window from the current period.

        `point_type` : PivotPointType, defaults PivotPointType.STANDARD
            Pivot Point type.

    Returns:
        `RollingPivotsResults[RollingPivotsResult]`
            RollingPivotsResults is list of RollingPivotsResult with providing useful helper methods.

    See more:
         - [Rolling Pivot Points Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/RollingPivots/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetRollingPivots[Quote](CsList(Quote, quotes), window_periods,
                                                 offset_periods, point_type)
    return RollingPivotsResults(results, RollingPivotsResult)


class RollingPivotsResult(ResultBase):
    """
    A wrapper class for a single unit of Rolling Pivot Points results.
    """

    @property
    def r4(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.R4)

    @r4.setter
    def r4(self, value):
        self._csdata.R4 = CsDecimal(value)

    @property
    def r3(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.R3)

    @r3.setter
    def r3(self, value):
        self._csdata.R3 = CsDecimal(value)

    @property
    def r2(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.R2)

    @r2.setter
    def r2(self, value):
        self._csdata.R2 = CsDecimal(value)

    @property
    def r1(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.R1)

    @r1.setter
    def r1(self, value):
        self._csdata.R1 = CsDecimal(value)

    @property
    def pp(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.PP)

    @pp.setter
    def pp(self, value):
        self._csdata.PP = CsDecimal(value)

    @property
    def s1(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.S1)

    @s1.setter
    def s1(self, value):
        self._csdata.S1 = CsDecimal(value)

    @property
    def s2(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.S2)

    @s2.setter
    def s2(self, value):
        self._csdata.S2 = CsDecimal(value)

    @property
    def s3(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.S3)

    @s3.setter
    def s3(self, value):
        self._csdata.S3 = CsDecimal(value)

    @property
    def s4(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.S4)

    @s4.setter
    def s4(self, value):
        self._csdata.S4 = CsDecimal(value)


_T = TypeVar("_T", bound=RollingPivotsResult)
class RollingPivotsResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Rolling Pivot Points results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
