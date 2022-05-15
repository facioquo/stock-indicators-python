from typing import Iterable

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.candles import CandleResult, CandleResults
from stock_indicators.indicators.common.quote import Quote


def get_marubozu(quotes: Iterable[Quote], min_body_percent: float = 95):
    """Get Marubozu calculated.

    (preview)
    Marubozu is a single candlestick pattern that has no wicks,
    representing consistent directional movement.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `min_body_percent` : float, defaults 95
            Minimum candle body size as decimalized percentage.

    Returns:
        `CandleResults[CandleResult]`
            CandleResults is list of CandleResult with providing useful helper methods.

    See more:
         - [Marubozu Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Marubozu/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetMarubozu[Quote](CsList(Quote, quotes), min_body_percent)
    return CandleResults(results, CandleResult)
