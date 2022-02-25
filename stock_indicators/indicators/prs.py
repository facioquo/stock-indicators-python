from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_prs(base_history: Iterable[Quote], eval_history: Iterable[Quote],
            lookback_periods: Optional[int] = None, sma_periods: Optional[int] = None):
    """Get PRS calculated.

    Price Relative Strength (PRS), also called Comparative Relative Strength,
    shows the ratio of two quote histories, based on Close price.
    It is often used to compare against a market index or sector ETF.
    When using the optional lookbackPeriods, this also return relative percent
    change over the specified periods.

    Parameters:
        `base_history` : Iterable[Quote]
            This is usually market index data,
            but could be any baseline data that you might use for comparison.

        `base_history` : Iterable[Quote]
            Historical price quotes for evaluation.

        `lookback_periods` : int, optional
            Number of periods for % difference.

        `sma_periods` : int, optional
            Number of periods for a PRS SMA signal line.

    Returns:
        `PRSResults[PRSResult]`
            PRSResults is list of PRSResult with providing useful helper methods.

    See more:
         - [PRS Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Prs/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetPrs[Quote](CsList(Quote, base_history), CsList(Quote, eval_history),
                                        lookback_periods, sma_periods)
    return PRSResults(results, PRSResult)


class PRSResult(ResultBase):
    """
    A wrapper class for a single unit of Price Relative Strength (PRS) results.
    """

    @property
    def prs(self) -> Optional[float]:
        return self._csdata.Prs

    @prs.setter
    def prs(self, value):
        self._csdata.Prs = value

    @property
    def prs_sma(self) -> Optional[float]:
        return self._csdata.PrsSma

    @prs_sma.setter
    def prs_sma(self, value):
        self._csdata.PrsSma = value

    @property
    def prs_percent(self) -> Optional[float]:
        return self._csdata.PrsPercent

    @prs_percent.setter
    def prs_percent(self, value):
        self._csdata.PrsPercent = value


_T = TypeVar("_T", bound=PRSResult)
class PRSResults(IndicatorResults[_T]):
    """
    A wrapper class for the list of Price Relative Strength (PRS) results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
