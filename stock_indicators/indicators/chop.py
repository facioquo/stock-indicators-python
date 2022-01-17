from decimal import Decimal
from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.decimal import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_chop(quotes: Iterable[Quote], lookback_periods: int = 14):
    results = CsIndicator.GetChop[Quote](CsList(Quote, quotes), lookback_periods)
    return ChopResults(results, ChopResult)


class ChopResult(ResultBase):
    """
    A wrapper class for a single unit of Choppiness Index (CHOP) results.
    """

    @property
    def chop(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Chop)

    @chop.setter
    def chop(self, value):
        self._csdata.Chop = CsDecimal(value)


T = TypeVar("T", bound=ChopResult)
class ChopResults(RemoveWarmupMixin, IndicatorResults[T]):
    """
    A wrapper class for the list of Choppiness Index (CHOP)) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
