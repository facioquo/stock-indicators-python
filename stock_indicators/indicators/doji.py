from typing import Iterable

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.candles import CandleResult, CandleResults
from stock_indicators.indicators.common.quote import Quote


def get_doji(quotes: Iterable[Quote], max_price_change_percent: float = 0.1):
    """Get Doji calculated.

    (preview)
    Doji is a single candlestick pattern where open and
    close price are virtually identical, representing market indecision.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `max_price_change_percent` : float, defaults 0.1
            Maximum absolute decimalized percent difference in open and close price.

    Returns:
        `CandleResults[CandleResult]`
            CandleResults is list of CandleResult with providing useful helper methods.

    See more:
         - [Doji Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Doji/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetDoji[Quote](CsList(Quote, quotes), max_price_change_percent)
    return CandleResults(results, CandleResult)
