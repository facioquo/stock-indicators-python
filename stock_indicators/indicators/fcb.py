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
    """Get FCB calculated.

    Fractal Chaos Bands (FCB) outline high and low price channels
    to depict broad less-chaotic price movements.
    FCB is a channelized depiction of Williams Fractals.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `window_span` : int, defaults 2
            Number of span periods in the evaluation window.

    Returns:
        `FCBResults[FCBResult]`
            FCBResults is list of FCBResult with providing useful helper methods.

    See more:
         - [FCB Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Fcb/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
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


_T = TypeVar("_T", bound=FCBResult)
class FCBResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Fractal Chaos Bands (FCB) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
