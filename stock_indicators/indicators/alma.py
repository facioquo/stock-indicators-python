from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import to_pydecimal
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def get_alma(quotes: Iterable[Quote], lookback_periods: int = 9, offset: float = .85, sigma : float = 6):
    """Get ALMA calculated.

    Arnaud Legoux Moving Average (ALMA) is a Gaussian distribution
    weighted moving average of Close price over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 9
            Number of periods in the lookback window.

        `offset` : float, defaults 0.85
            Adjusts smoothness versus responsiveness.

        `sigma` : float, defaults 6
            Defines the width of the Gaussian normal distribution.

    Returns:
        `ALMAResults[ALMAResult]`
            ALMAResults is list of ALMAResult with providing useful helper methods.

    See more:
         - [ALMA Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Alma/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    alma_results = CsIndicator.GetAlma[Quote](CsList(Quote, quotes), lookback_periods, offset, sigma)
    return ALMAResults(alma_results, ALMAResult)


class ALMAResult(ResultBase):
    """
    A wrapper class for a single unit of ALMA results.
    """

    @property
    def alma(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Alma)

    @alma.setter
    def alma(self, value):
        self._csdata.Alma = CsDecimal(value)


_T = TypeVar("_T", bound=ALMAResult)
class ALMAResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of ALMA(Arnaud Legoux Moving Average) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
