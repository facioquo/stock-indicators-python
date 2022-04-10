from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.enums import EndType, PivotTrend
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_pivots(quotes: Iterable[Quote], left_span: int = 2,
               right_span: int = 2, max_trend_periods: int = 20,
               end_type: EndType = EndType.HIGH_LOW):
    """Get Pivots calculated.

    Pivots is an extended version of Williams Fractal that includes
    identification of Higher High, Lower Low, Higher Low, and Lower Low trends
    between pivots in a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `left_span` : int, defaults 2
            Number of span periods to the left of the evaluation period.

        `right_span` : int, defaults 2
            Number of span periods to the right of the evaluation period.

        `max_trend_periods` : int, defaults 20
            Number of periods in the lookback window.

        `end_type` : EndType, defaults EndType.HIGH_LOW
            Determines use of Close or High/Low wicks for points.

    Returns:
        `PivotsResults[PivotsResult]`
            PivotsResults is list of PivotsResult with providing useful helper methods.

    See more:
         - [Pivots Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Pivots/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetPivots[Quote](CsList(Quote, quotes), left_span,
                                           right_span, max_trend_periods,
                                           end_type)
    return PivotsResults(results, PivotsResult)


class PivotsResult(ResultBase):
    """
    A wrapper class for a single unit of Pivots results.
    """

    @property
    def high_point(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.HighPoint)

    @high_point.setter
    def high_point(self, value):
        self._csdata.HighPoint = CsDecimal(value)

    @property
    def low_point(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.LowPoint)

    @low_point.setter
    def low_point(self, value):
        self._csdata.LowPoint = CsDecimal(value)

    @property
    def high_line(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.HighLine)

    @high_line.setter
    def high_line(self, value):
        self._csdata.HighLine = CsDecimal(value)

    @property
    def low_line(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.LowLine)

    @low_line.setter
    def low_line(self, value):
        self._csdata.LowLine = CsDecimal(value)

    @property
    def high_trend(self) -> Optional[PivotTrend]:
        return self._csdata.HighTrend

    @high_trend.setter
    def high_trend(self, value):
        self._csdata.HighTrend = value

    @property
    def low_trend(self) -> Optional[PivotTrend]:
        return self._csdata.LowTrend

    @low_trend.setter
    def low_trend(self, value):
        self._csdata.LowTrend = value


_T = TypeVar("_T", bound=PivotsResult)
class PivotsResults(IndicatorResults[_T]):
    """
    A wrapper class for the list of Pivots results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
