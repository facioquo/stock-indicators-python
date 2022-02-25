from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_keltner(quotes: Iterable[Quote], ema_periods: int = 20,
                multiplier: float = 2, atr_periods: int = 10):
    """Get Keltner Channels calculated.

    Keltner Channels are based on an EMA centerline andATR band widths.
    See also STARC Bands for an SMA centerline equivalent.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `ema_periods` : int, defaults 20
            Number of periods for the centerline EMA.

        `multiplier` : float, defaults 2
            ATR multiplier sets the width of the channel.

        `atr_periods` : int, defaults 10
            Number of periods in the ATR evaluation.

    Returns:
        `KeltnerResults[KeltnerResult]`
            KeltnerResults is list of KeltnerResult with providing useful helper methods.

    See more:
         - [Keltner Channels Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Keltner/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetKeltner[Quote](CsList(Quote, quotes), ema_periods,
                                            CsDecimal(multiplier), atr_periods)
    return KeltnerResults(results, KeltnerResult)


class KeltnerResult(ResultBase):
    """
    A wrapper class for a single unit of Keltner Channels results.
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

    @property
    def width(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Width)

    @width.setter
    def width(self, value):
        self._csdata.Width = CsDecimal(value)


_T = TypeVar("_T", bound=KeltnerResult)
class KeltnerResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Keltner Channels results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
