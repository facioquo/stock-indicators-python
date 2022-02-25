from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_ht_trendline(quotes: Iterable[Quote]):
    """Get HTL calculated.

    Hilbert Transform Instantaneous Trendline (HTL) is a 5-period
    trendline of high/low price that uses signal processing to reduce noise.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

    Returns:
        `HTTrendlineResults[HTTrendlineResult]`
            HTTrendlineResults is list of HTTrendlineResult with providing useful helper methods.

    See more:
         - [HTL Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/HtTrendline/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetHtTrendline[Quote](CsList(Quote, quotes))
    return HTTrendlineResults(results, HTTrendlineResult)


class HTTrendlineResult(ResultBase):
    """
    A wrapper class for a single unit of Hilbert Transform Instantaneous Trendline (HTL) results.
    """

    @property
    def trendline(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Trendline)

    @trendline.setter
    def trendline(self, value):
        self._csdata.Trendline = CsDecimal(value)

    @property
    def smooth_price(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.SmoothPrice)

    @smooth_price.setter
    def smooth_price(self, value):
        self._csdata.SmoothPrice = CsDecimal(value)


_T = TypeVar("_T", bound=HTTrendlineResult)
class HTTrendlineResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Hilbert Transform Instantaneous Trendline (HTL) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
