from typing import Iterable, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.candles import CandleResult, CondenseMixin
from stock_indicators.indicators.common.results import IndicatorResults
from stock_indicators.indicators.common.quote import Quote


def get_marubozu(quotes: Iterable[Quote], min_body_percent: float = 0.95):
    """Get Marubozu calculated.

    (preview)
    Marubozu is a single candlestick pattern that has no wicks,
    representing consistent directional movement.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `min_body_percent` : float, defaults 0.95
            Minimum candle body size as decimalized percentage.

    Returns:
        `MarubozuResults[MarubozuResult]`
            MarubozuResults is list of MarubozuResult with providing useful helper methods.

    See more:
         - [Marubozu Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Marubozu/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetMarubozu[Quote](CsList(Quote, quotes), min_body_percent)
    return MarubozuResults(results, MarubozuResult)


class MarubozuResult(CandleResult):
    """
    A wrapper class for a single unit of Marubozu results.
    """


_T = TypeVar("_T", bound=MarubozuResult)
class MarubozuResults(CondenseMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Marubozu results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
