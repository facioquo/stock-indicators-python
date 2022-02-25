from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_connors_rsi(quotes: Iterable[Quote], rsi_periods: int = 3,
                    streak_periods: int = 2, rank_periods: int = 100):
    """Get Connors RSI calculated.

    Connors RSI is a composite oscillator that incorporates
    RSI, winning/losing streaks, and percentile gain metrics on scale of 0 to 100.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `rsi_periods` : int, defaults 3
            Number of periods in the RSI.

        `streak_periods` : int, defaults 2
            Number of periods for streak RSI.

        `rank_periods` : int, defaults 100
            Number of periods for the percentile ranking.

    Returns:
        `ConnorsRSIResults[ConnorsRSIResult]`
            ConnorsRSIResults is list of ConnorsRSIResult with providing useful helper methods.

    See more:
         - [Connors RSI Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/ConnorsRsi/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    results = CsIndicator.GetConnorsRsi[Quote](CsList(Quote, quotes), rsi_periods,
                                               streak_periods, rank_periods)
    return ConnorsRSIResults(results, ConnorsRSIResult)


class ConnorsRSIResult(ResultBase):
    """
    A wrapper class for a single unit of Connors RSI results.
    """

    @property
    def rsi_close(self) -> Optional[float]:
        return self._csdata.RsiClose

    @rsi_close.setter
    def rsi_close(self, value):
        self._csdata.RsiClose = value

    @property
    def rsi_streak(self) -> Optional[float]:
        return self._csdata.RsiStreak

    @rsi_streak.setter
    def rsi_streak(self, value):
        self._csdata.RsiStreak = value

    @property
    def percent_rank(self) -> Optional[float]:
        return self._csdata.PercentRank

    @percent_rank.setter
    def percent_rank(self, value):
        self._csdata.PercentRank = value

    @property
    def connors_rsi(self) -> Optional[float]:
        return self._csdata.ConnorsRsi

    @connors_rsi.setter
    def connors_rsi(self, value):
        self._csdata.ConnorsRsi = value


_T = TypeVar("_T", bound=ConnorsRSIResult)
class ConnorsRSIResults(RemoveWarmupMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Connors RSI results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
