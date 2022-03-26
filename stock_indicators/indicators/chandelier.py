from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.enums import ChandelierType
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_chandelier(quotes: Iterable[Quote], lookback_periods: int = 22,
                   multiplier: float = 3, chandelier_type: ChandelierType = ChandelierType.LONG):
    """Get Chandelier Exit calculated.

    Chandelier Exit is typically used for stop-loss and can be
    computed for both long or short types.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 22
            Number of periods in the lookback window.

        `multiplier` : float, defaults 3.0
            Multiplier.

        `chandelier_type` : ChandelierType, defaults ChandelierType.LONG
            Short or Long variant selection.

    Returns:
        `ChandelierResults[ChandelierResult]`
            ChandelierResults is list of ChandelierResult with providing useful helper methods.

    See more:
         - [Chandelier Exit Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Chandelier/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetChandelier[Quote](CsList(Quote, quotes), lookback_periods,
                                               multiplier, chandelier_type)
    return ChandelierResults(results, ChandelierResult)


class ChandelierResult(ResultBase):
    """
    A wrapper class for a single unit of Chandelier Exit results.
    """

    @property
    def chandelier_exit(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.ChandelierExit)

    @chandelier_exit.setter
    def chandelier_exit(self, value):
        self._csdata.ChandelierExit = CsDecimal(value)


_T = TypeVar("_T", bound=ChandelierResult)
class ChandelierResults(RemoveWarmupMixin,IndicatorResults[_T]):
    """
    A wrapper class for the list of Chandelier Exit results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
