from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_cci(quotes: Iterable[Quote], lookback_periods: int = 20):
    results = CsIndicator.GetCci[Quote](CsList(Quote, quotes), lookback_periods)
    return CCIResults(results, CCIResult)


class CCIResult(ResultBase):
    """
    A wrapper class for a single unit of Commodity Channel Index (CCI) results.
    """

    @property
    def cci(self) -> Optional[float]:
        return self._csdata.Cci

    @cci.setter
    def cci(self, value):
        self._csdata.Cci = value


T = TypeVar("T", bound=CCIResult)
class CCIResults(RemoveWarmupMixin, IndicatorResults[T]):
    """
    A wrapper class for the list of Commodity Channel Index (CCI) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
