from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_mfi(quotes: Iterable[Quote], lookback_periods: int = 14):
    """Get MFI calculated.

    Money Flow Index (MFI) is a price-volume oscillator
    that shows buying and selling momentum.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 14
            Number of periods in the lookback window.

    Returns:
        `MFIResults[MFIResult]`
            MFIResults is list of MFIResult with providing useful helper methods.

    See more:
         - [MFI Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Mfi/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetMfi[Quote](CsList(Quote, quotes), lookback_periods)
    return MFIResults(results, MFIResult)


class MFIResult(ResultBase):
    """
    A wrapper class for a single unit of Money Flow Index (MFI) results.
    """

    @property
    def mfi(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Mfi)

    @mfi.setter
    def mfi(self, value):
        self._csdata.Mfi = CsDecimal(value)


_T = TypeVar("_T", bound=MFIResult)
class MFIResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Money Flow Index (MFI) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
