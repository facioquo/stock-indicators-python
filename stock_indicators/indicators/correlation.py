from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_correlation(quotes_a: Iterable[Quote], quotes_b: Iterable[Quote],
                    lookback_periods: int):
    """Get Correlation Coefficient calculated.

    Correlation Coefficient between two quote histories, based on Close price.

    Parameters:
        `quotes_a` : Iterable[Quote]
            Historical price quotes A for comparison.

        `quotes_b` : Iterable[Quote]
            Historical price quotes B for comparison.

        `lookback_periods` : int
            Number of periods in the lookback window.

    Returns:
        `CorrelationResults[CorrelationResult]`
            CorrelationResults is list of CorrelationResult with providing useful helper methods.

    See more:
         - [Correlation Coefficient Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Correlation/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetCorrelation[Quote](CsList(Quote, quotes_a), CsList(Quote, quotes_b),
                                                lookback_periods)
    return CorrelationResults(results, CorrelationResult)


class CorrelationResult(ResultBase):
    """
    A wrapper class for a single unit of Correlation Coefficient results.
    """

    @property
    def variance_a(self) -> Optional[float]:
        return self._csdata.VarianceA

    @variance_a.setter
    def variance_a(self, value):
        self._csdata.VarianceA = value

    @property
    def variance_b(self) -> Optional[float]:
        return self._csdata.VarianceB

    @variance_b.setter
    def variance_b(self, value):
        self._csdata.VarianceB = value

    @property
    def covariance(self) -> Optional[float]:
        return self._csdata.Covariance

    @covariance.setter
    def covariance(self, value):
        self._csdata.Covariance = value

    @property
    def correlation(self) -> Optional[float]:
        return self._csdata.Correlation

    @correlation.setter
    def correlation(self, value):
        self._csdata.Correlation = value

    @property
    def r_squared(self) -> Optional[float]:
        return self._csdata.RSquared

    @r_squared.setter
    def r_squared(self, value):
        self._csdata.RSquared = value


_T = TypeVar("_T", bound=CorrelationResult)
class CorrelationResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Correlation Coefficient results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
