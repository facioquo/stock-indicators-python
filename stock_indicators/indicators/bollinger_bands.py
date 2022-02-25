from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_bollinger_bands(quotes: Iterable[Quote], lookback_periods: int = 20, standard_deviations: float = 2):
    """Get Bollinger Bands&#174; calculated.

    Bollinger Bands&#174; depict volatility as standard deviation
    boundary lines from a moving average of Close price.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 20
            Number of periods in the lookback window.

        `standard_deviations` : float, defaults 2
            Width of bands. Number of Standard Deviations from the moving average.

    Returns:
        `BollingerBandsResults[BollingerBandsResult]`
            BollingerBandsResults is list of BollingerBandsResult with providing useful helper methods.

    See more:
         - [Bollinger Bands&#174; Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/BollingerBands/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    bollinger_bands_results = CsIndicator.GetBollingerBands[Quote](CsList(Quote, quotes), lookback_periods, standard_deviations)
    return BollingerBandsResults(bollinger_bands_results, BollingerBandsResult)


class BollingerBandsResult(ResultBase):
    """
    A wrapper class for a single unit of Bollinger Bands results.
    """

    @property
    def sma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Sma)

    @sma.setter
    def sma(self, value):
        self._csdata.Sma = CsDecimal(value)

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

    @property
    def percent_b(self) -> Optional[float]:
        return self._csdata.PercentB

    @percent_b.setter
    def percent_b(self, value):
        self._csdata.PercentB = value

    @property
    def z_score(self) -> Optional[float]:
        return self._csdata.ZScore

    @z_score.setter
    def z_score(self, value):
        self._csdata.ZScore = value

    @property
    def width(self) -> Optional[float]:
        return self._csdata.Width

    @width.setter
    def width(self, value):
        self._csdata.Width = value


_T = TypeVar("_T", bound=BollingerBandsResult)
class BollingerBandsResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Bollinger Bands results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
