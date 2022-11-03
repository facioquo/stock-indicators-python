from typing import Callable, Generic, Iterable, List, Optional, TypeVar, overload

from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.basic_quotes import BasicQuoteResult, BasicQuoteResults, get_basic_quote
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.indicator import Indicator
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults


_T = TypeVar("_T", bound=IndicatorResults)
_U = TypeVar("_U", bound=IndicatorResults)
class IndicatorChain(Generic[_T]):
    def __init__(self, quotes: Iterable[Quote], candle_part: CandlePart):
        self.chain: List[Callable] = []
        self.quotes = quotes
        self.last_indicator: Indicator = None
        if candle_part is not None:
            self.add(get_basic_quote, candle_part)

    @overload
    @classmethod
    def use_quotes(cls, quotes: Iterable[Quote]) -> "IndicatorChain[None]": ...
    @overload
    @classmethod
    def use_quotes(cls, quotes: Iterable[Quote], candle_part: CandlePart) -> "IndicatorChain[BasicQuoteResults[BasicQuoteResult]]": ...
    @classmethod
    def use_quotes(cls, quotes: Iterable[Quote], candle_part: Optional[CandlePart] = None):
        """
        Provide quotes and optionally select which candle part to use in the calculation.
        
        Note that if you specify `candle_part`, `quote` will be converted into `BasicQuote` internally.
        And it may affect some of the indicators that must start from `Quote`s.
        """
        instance = cls(quotes, candle_part)
        return instance
    
    def add(self, indicator_method: Callable[..., _U], *args, **kwargs) -> "IndicatorChain[_U]":
        """Add indicator method that calculates lazily."""
        if self.last_indicator and not self.last_indicator.is_chainor:
            raise ValueError((f"{self.chain[-1].__name__}() cannot be further chained with additional transforms. "
                              "See docs for more details."))

        indicator_info, chaining_method = indicator_method(*args, **kwargs, is_chaining = True)
        if self.last_indicator and not indicator_info.is_chainee:
            raise ValueError((f"{chaining_method.__name__}() must be generated from quotes "
                              "and cannot be generated from results of another chain-enabled"
                              "indicator or method. See docs for more details."))
        
        self.chain.append(chaining_method)
        self.last_indicator = indicator_info
        return self

    def calc(self) -> _T:
        """Calculate all chained indicators."""
        results = None
        if self.chain:
            results = CsList(Quote, self.quotes)

            idx = 0
            last_indicator = self.chain.pop()

            for idx, indicator in enumerate(self.chain, 1):
                results = indicator(results, use_chaining = idx > 1)

            results = last_indicator(results, use_chaining = idx > 0, is_last = True)

        return results
