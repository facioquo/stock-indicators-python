from decimal import Decimal
from typing import Optional, TypeVar
from typing_extensions import override

from stock_indicators._cslib import CsCandleProperties
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common._contrib.type_resolver import generate_cs_inherited_class
from stock_indicators.indicators.common.enums import Match
from stock_indicators.indicators.common.helpers import CondenseMixin
from stock_indicators.indicators.common.quote import _Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


class _CandleProperties(_Quote):
    @property
    def size(self) -> Optional[Decimal]:
        return to_pydecimal(self.High - self.Low)

    @property
    def body(self) -> Optional[Decimal]:
        return to_pydecimal(self.Open - self.Close \
            if (self.Open > self.Close) \
            else self.Close - self.Open)

    @property
    def upper_wick(self) -> Optional[Decimal]:
        return to_pydecimal(self.High - (
            self.Open \
            if self.Open > self.Close \
            else self.Close))

    @property
    def lower_wick(self) -> Optional[Decimal]:
        return to_pydecimal((self.Close \
            if self.Open > self.Close \
            else self.Open) - self.Low)

    @property
    def body_pct(self) -> Optional[float]:
        return float(self.body / self.size) if self.size != 0 else 1

    @property
    def upper_wick_pct(self) -> Optional[float]:
        return float(self.upper_wick / self.size) if self.size != 0 else 1

    @property
    def lower_wick_pct(self) -> Optional[float]:
        return float(self.lower_wick / self.size) if self.size != 0 else 1

    @property
    def is_bullish(self) -> bool:
        return self.Close > self.Open

    @property
    def is_bearish(self) -> bool:
        return self.Close < self.Open


class CandleProperties(generate_cs_inherited_class(_CandleProperties, CsCandleProperties)):
    """An extended version of Quote that contains additional calculated properties."""
    pass


class CandleResult(ResultBase):
    """
    A wrapper class for a single unit of Candlestick pattern results.
    """

    __candle_prop_cache = None

    @property
    def price(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Price)

    @price.setter
    def price(self, value):
        self._csdata.Price = CsDecimal(value)

    @property
    def match(self) -> Match:
        return Match(int(self._csdata.Match))

    @match.setter
    def match(self, value):
        self._csdata.Match = value.cs_value

    @property
    def candle(self) -> CandleProperties:
        if not self.__candle_prop_cache:
            self.__candle_prop_cache = CandleProperties.from_csquote(self._csdata.Candle)

        return self.__candle_prop_cache

    @candle.setter
    def candle(self, value):
        self._csdata.Candle = value
        self.__candle_prop_cache = None


_T = TypeVar("_T", bound=CandleResult)
class CandleResults(CondenseMixin, IndicatorResults[_T]):
    """
    A wrapper class for the list of Candlestick pattern results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """

    @override
    def condense(self):
        return self.__class__(filter(lambda x: x.match != Match.NONE, self), self._wrapper_class)
