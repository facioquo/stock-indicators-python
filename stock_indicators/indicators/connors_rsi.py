from decimal import Decimal
from typing import Iterable, Optional, TypeVar
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes.decimal import to_pydecimal
from stock_indicators.indicators.common.helpers import RemoveWarmupMixin
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_connors_rsi(quotes: Iterable[Quote], rsi_periods: int = 3,
                    streak_periods: int = 2, rank_periods: int = 100):
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


T = TypeVar("T", bound=ConnorsRSIResult)
class ConnorsRSIResults(RemoveWarmupMixin, IndicatorResults[T]):
    """
    A wrapper class for the list of Connors RSI results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
