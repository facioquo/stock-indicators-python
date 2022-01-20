from decimal import Decimal
from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_fcb(quotes: Iterable[Quote], window_span: int = 2):
    results = CsIndicator.GetFcb[Quote](CsList(Quote, quotes), window_span)
    return FCBResults(results, FCBResult)


class FCBResult(ResultBase):
    """
    A wrapper class for a single unit of Fractal Chaos Bands (FCB) results.
    """

    @property
    def upper_band(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.UpperBand)

    @upper_band.setter
    def upper_band(self, value):
        self._csdata.UpperBand = CsDecimal(value)

    @property
    def lower_band(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.LowerBand)

    @lower_band.setter
    def lower_band(self, value):
        self._csdata.LowerBand = CsDecimal(value)


T = TypeVar("T", bound=FCBResult)
class FCBResults(RemoveWarmupMixin, IndicatorResults[T]):
    """
    A wrapper class for the list of Fractal Chaos Bands (FCB) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
