from decimal import Decimal
from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_aroon(quotes: Iterable[Quote], lookback_periods: int = 25):
    """Get Aroon calculated.

    Aroon is a simple oscillator view of how long the new high or low price occured over a lookback window.

    Parameters:
        `quotes` : Iterable[Quotes]
            Historical price quotes.

        `lookback_periods` : int, defaults 25
            Number of periods in the lookback window.

    Returns:
        `AroonResults[AroonResult]`
            AroonResults is list of AroonResult with providing useful helper methods.

    See more:
         - [Aroon Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Aroon/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    aroon_results = CsIndicator.GetAroon[Quote](CsList(Quote, quotes), lookback_periods)
    return AroonResults(aroon_results, AroonResult)

class AroonResult(ResultBase):
    """
    A wrapper class for a single unit of Aroon results.
    """

    @property
    def aroon_up(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.AroonUp)

    @aroon_up.setter
    def aroon_up(self, value):
        self._csdata.AroonUp = CsDecimal(value)

    @property
    def aroon_down(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.AroonDown)

    @aroon_down.setter
    def aroon_down(self, value):
        self._csdata.AroonDown = CsDecimal(value)

    @property
    def oscillator(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Oscillator)

    @oscillator.setter
    def oscillator(self, value):
        self._csdata.Oscillator = CsDecimal(value)

T = TypeVar("T", bound=AroonResult)
class AroonResults(IndicatorResults[T]):
    """
    A wrapper class for the list of Aroon results. It is exactly same with built-in `list`
    except for that it provides some useful helper methods written in C# implementation.
    """

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        