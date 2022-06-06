from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.enums import EndType
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_zig_zag(quotes: Iterable[Quote], end_type: EndType = EndType.CLOSE,
                percent_change: float = 5):
    """Get Zig Zag calculated.

    Zig Zag is a price chart overlay that simplifies the up and down
    movements and transitions based on a percent change smoothing threshold.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `end_type` : EndType, defaults EndType.CLOSE
           Determines use of Close or High/Low wicks for extreme points.

        `percent_change` : float, defaults 5
           Percent price change to set threshold for minimum size movements.

    Returns:
        `ZigZagResults[ZigZagResult]`
            ZigZagResults is list of ZigZagResult with providing useful helper methods.

    See more:
         - [Zig Zag Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/ZigZag/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetZigZag[Quote](CsList(Quote, quotes), end_type,
                                           CsDecimal(percent_change))
    return ZigZagResults(results, ZigZagResult)


class ZigZagResult(ResultBase):
    """
    A wrapper class for a single unit of Zig Zag results.
    """

    @property
    def zig_zag(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.ZigZag)

    @zig_zag.setter
    def zig_zag(self, value):
        self._csdata.ZigZag = CsDecimal(value)

    @property
    def point_type(self) -> Optional[str]:
        return self._csdata.PointType

    @point_type.setter
    def point_type(self, value):
        self._csdata.PointType = value

    @property
    def retrace_high(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.RetraceHigh)

    @retrace_high.setter
    def retrace_high(self, value):
        self._csdata.RetraceHigh = CsDecimal(value)

    @property
    def retrace_low(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.RetraceLow)

    @retrace_low.setter
    def retrace_low(self, value):
        self._csdata.RetraceLow = CsDecimal(value)


_T = TypeVar("_T", bound=ZigZagResult)
class ZigZagResults(IndicatorResults[_T]):
    """
    A wrapper class for the list of Zig Zag results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
