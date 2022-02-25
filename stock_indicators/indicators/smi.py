from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_smi(quotes: Iterable[Quote], lookback_periods: int,
            first_smooth_periods: int, second_smooth_periods: int,
            signal_periods: int = 3):
    """Get SMI calculated.

    Stochastic Momentum Index (SMI) is a double-smoothed variant of
    the Stochastic Oscillator on a scale from -100 to 100.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods for the Stochastic lookback.

        `first_smooth_periods` : int
            Number of periods in the first smoothing.

        `second_smooth_periods` : int
            Number of periods in the second smoothing.

        `signal_periods` : int, defaults 3
            Number of periods in the EMA of SMI.

    Returns:
        `SMIResults[SMIResult]`
            SMIResults is list of SMIResult with providing useful helper methods.

    See more:
         - [SMI Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Smi/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetSmi[Quote](CsList(Quote, quotes), lookback_periods,
                                        first_smooth_periods, second_smooth_periods,
                                        signal_periods)
    return SMIResults(results, SMIResult)


class SMIResult(ResultBase):
    """
    A wrapper class for a single unit of Stochastic Momentum Index (SMI) results.
    """

    @property
    def smi(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Smi)

    @smi.setter
    def smi(self, value):
        self._csdata.Smi = CsDecimal(value)

    @property
    def signal(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Signal)

    @signal.setter
    def signal(self, value):
        self._csdata.Signal = CsDecimal(value)


_T = TypeVar("_T", bound=SMIResult)
class SMIResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Stochastic Momentum Index (SMI) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
