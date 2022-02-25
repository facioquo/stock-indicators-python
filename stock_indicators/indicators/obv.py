from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import ToQuotesMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_obv(quotes: Iterable[Quote], sma_periods: Optional[int] = None):
    """Get OBV calculated.

    On-balance Volume (OBV) is a rolling accumulation of
    volume based on Close price direction.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `sma_periods` : int, optional
            Number of periods for an SMA of the OBV line.

    Returns:
        `OBVResults[OBVResult]`
            OBVResults is list of OBVResult with providing useful helper methods.

    See more:
         - [OBV Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Obv/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetObv[Quote](CsList(Quote, quotes), sma_periods)
    return OBVResults(results, OBVResult)


class OBVResult(ResultBase):
    """
    A wrapper class for a single unit of On-balance Volume (OBV) results.
    """

    @property
    def obv(self) -> float:
        return self._csdata.Obv

    @obv.setter
    def obv(self, value):
        self._csdata.Obv = value

    @property
    def obv_sma(self) -> Optional[float]:
        return self._csdata.ObvSma

    @obv_sma.setter
    def obv_sma(self, value):
        self._csdata.ObvSma = value


_T = TypeVar("_T", bound=OBVResult)
class OBVResults(ToQuotesMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of On-balance Volume (OBV) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
