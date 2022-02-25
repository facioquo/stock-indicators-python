from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_starc_bands(quotes: Iterable[Quote], sma_periods: int = 20,
            multiplier: float = 2, atr_periods: int = 10):
    """Get STARC Bands calculated.

    Stoller Average Range Channel (STARC) Bands, are based
    on an SMA centerline and ATR band widths.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `sma_periods` : int, defaults 20
            Number of periods for the centerline SMA.

        `multiplier` : float, defaults 2
            ATR multiplier sets the width of the channel.

        `atr_periods` : int, defaults 10
            Number of periods in the ATR evaluation.

    Returns:
        `STARCBandsResults[STARCBandsResult]`
            STARCBandsResults is list of STARCBandsResult with providing useful helper methods.

    See more:
         - [STARC Bands Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/StarcBands/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetStarcBands[Quote](CsList(Quote, quotes), sma_periods,
                                               CsDecimal(multiplier), atr_periods)
    return STARCBandsResults(results, STARCBandsResult)


class STARCBandsResult(ResultBase):
    """
    A wrapper class for a single unit of Stoller Average Range Channel (STARC) Bands results.
    """

    @property
    def upper_band(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.UpperBand)

    @upper_band.setter
    def upper_band(self, value):
        self._csdata.UpperBand = CsDecimal(value)

    @property
    def center_line(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Centerline)

    @center_line.setter
    def center_line(self, value):
        self._csdata.Centerline = CsDecimal(value)

    @property
    def lower_band(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.LowerBand)

    @lower_band.setter
    def lower_band(self, value):
        self._csdata.LowerBand = CsDecimal(value)


_T = TypeVar("_T", bound=STARCBandsResult)
class STARCBandsResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Stoller Average Range Channel (STARC) Bands results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
