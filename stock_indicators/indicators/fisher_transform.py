from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class FisherTransformResult(ResultBase):
    """
    A wrapper class for a single unit of Ehlers Fisher Transform results.
    """

    @property
    def fisher(self) -> Optional[float]:
        return self._csdata.Fisher

    @fisher.setter
    def fisher(self, value):
        self._csdata.Fisher = value

    @property
    def trigger(self) -> Optional[float]:
        return self._csdata.Trigger

    @trigger.setter
    def trigger(self, value):
        self._csdata.Trigger = value


_T = TypeVar("_T", bound=FisherTransformResult)
class FisherTransformResults(IndicatorResults[_T]):
    """
    A wrapper class for the list of Ehlers Fisher Transform results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """


class FisherTransform(Indicator):
    is_chainee = True
    is_chainor = True

    indicator_method = CsIndicator.GetFisherTransform[Quote]
    chaining_method = CsIndicator.GetFisherTransform

    list_wrap_class = FisherTransformResults
    unit_wrap_class = FisherTransformResult


@calculate_indicator(indicator=FisherTransform())
def get_fisher_transform(quotes: Iterable[Quote], lookback_periods: int = 10) -> FisherTransformResults[FisherTransformResult]:
    """Get Ehlers Fisher Transform calculated.

    Ehlers Fisher Transform converts prices
    into a Gaussian normal distribution.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int, defaults 10
            Number of periods in the lookback window.

    Returns:
        `FisherTransformResults[FisherTransformResult]`
            FisherTransformResults is list of
            FisherTransformResult with providing useful helper methods.

    See more:
         - [Fisher Transform Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/FisherTransform/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, lookback_periods)
