from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.enums import BetaType
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_beta(market_history: Iterable[Quote], eval_history: Iterable[Quote],
             lookback_periods: int, beta_type: BetaType = BetaType.STANDARD):
    """Get Beta calculated.

    Beta shows how strongly one stock responds to systemic volatility of the entire market.

    Parameters:
        `market_history` : Iterable[Quote]
            Historical price quotes for Market.

        `eval_history` : Iterable[Quote]
            Historical price quotes for Evaluation.

        `lookback_periods` : int
            Number of periods in the lookback window.

        `beta_type` : BetaType
            Type of Beta to calculate.

    Returns:
        `BetaResults[BetaResult]`
            BetaResults is list of BetaResult with providing useful helper methods.

    See more:
         - [Beta Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Beta/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    beta_results = CsIndicator.GetBeta[Quote](CsList(Quote, market_history), CsList(Quote, eval_history),
                                              lookback_periods, beta_type)
    return BetaResults(beta_results, BetaResult)


class BetaResult(ResultBase):
    """
    A wrapper class for a single unit of Beta results.
    """

    @property
    def beta(self) -> Optional[float]:
        return self._csdata.Beta

    @beta.setter
    def beta(self, value):
        self._csdata.Beta = value

    @property
    def beta_up(self) -> Optional[float]:
        return self._csdata.BetaUp

    @beta_up.setter
    def beta_up(self, value):
        self._csdata.BetaUp = value

    @property
    def beta_down(self) -> Optional[float]:
        return self._csdata.BetaDown

    @beta_down.setter
    def beta_down(self, value):
        self._csdata.BetaDown = value

    @property
    def ratio(self) -> Optional[float]:
        return self._csdata.Ratio

    @ratio.setter
    def ratio(self, value):
        self._csdata.Ratio = value

    @property
    def convexity(self) -> Optional[float]:
        return self._csdata.Convexity

    @convexity.setter
    def convexity(self, value):
        self._csdata.Convexity = value

    @property
    def returns_eval(self) -> Optional[float]:
        return self._csdata.ReturnsEval

    @returns_eval.setter
    def returns_eval(self, value):
        self._csdata.ReturnsEval = value

    @property
    def returns_mrkt(self) -> Optional[float]:
        return self._csdata.ReturnsMrkt

    @returns_mrkt.setter
    def returns_mrkt(self, value):
        self._csdata.ReturnsMrkt = value


_T = TypeVar("_T", bound=BetaResult)
class BetaResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Beta results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
