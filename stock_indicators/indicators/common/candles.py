from decimal import Decimal
from typing import Optional, TypeVar

from typing_extensions import Self

from stock_indicators._cslib import CsCandleProperties
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common._contrib.type_resolver import generate_cs_inherited_class
from stock_indicators.indicators.common.enums import Match
from stock_indicators.indicators.common.quote import _Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


class CondenseMixin:
    """Mixin for condense()."""
    @IndicatorResults._verify_data
    def condense(self) -> Self:
        """
        Remove results which have no match, so it only returns meaningful data records.
        """
        return self.__class__(filter(lambda x: x.match != Match.NONE, self), self._wrapper_class)


class _CandleProperties(_Quote):
    """
    A wrapper class for `CsCandleProperties`, which is an extended version of `Quote`.
    It contains additional calculated properties.
    """
    @property
    def size(self) -> Decimal:
        return to_pydecimal(self.high - self.low)

    @property
    def body(self) -> Decimal:
        return to_pydecimal(self.open - self.close \
            if (self.open > self.close) \
            else self.close - self.open)

    @property
    def upper_wick(self) -> Decimal:
        return to_pydecimal(self.high - (
            self.open \
            if self.open > self.close \
            else self.close))

    @property
    def lower_wick(self) -> Decimal:
        return to_pydecimal((self.close \
            if self.open > self.close \
            else self.open) - self.low)

    @property
    def body_pct(self) -> float:
        return float(self.body / self.size) if self.size != 0 else 1

    @property
    def upper_wick_pct(self) -> float:
        return float(self.upper_wick / self.size) if self.size != 0 else 1

    @property
    def lower_wick_pct(self) -> float:
        return float(self.lower_wick / self.size) if self.size != 0 else 1

    @property
    def is_bullish(self) -> bool:
        return self.Close > self.Open

    @property
    def is_bearish(self) -> bool:
        return self.Close < self.Open


CandleProperties = generate_cs_inherited_class(_CandleProperties, CsCandleProperties)


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
        return self._csdata.Match

    @match.setter
    def match(self, value):
        self._csdata.Match = value

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
