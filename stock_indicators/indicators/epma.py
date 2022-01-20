from decimal import Decimal
from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.decimal import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_epma(quotes: Iterable[Quote], lookback_periods: int):
    results = CsIndicator.GetEpma[Quote](CsList(Quote, quotes), lookback_periods)
    return EPMAResults(results, EPMAResult)


class EPMAResult(ResultBase):
    """
    A wrapper class for a single unit of Endpoint Moving Average (EPMA) results.
    """

    @property
    def epma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Epma)

    @epma.setter
    def epma(self, value):
        self._csdata.Epma = CsDecimal(value)


T = TypeVar("T", bound=EPMAResult)
class EPMAResults(RemoveWarmupMixin, IndicatorResults[T]):
    """
    A wrapper class for the list of Endpoint Moving Average (EPMA) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
