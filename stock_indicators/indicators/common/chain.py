from functools import wraps
from typing import Callable, Iterable, List, Optional

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.indicator import Indicator
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def calculate_indicator(indicator: Indicator):
    def decorator(interface_func: Callable):
        def calculate(*args, **kwargs):
            is_chaining = kwargs.pop("is_chaining", False)

            if is_chaining:
                if indicator.is_chainable:
                    @wraps(interface_func)
                    def calculate_lazily(quotes, use_chaining = True, is_last = False):
                        indicator_params = interface_func(quotes, *args, **kwargs)
                        results = indicator.calculate(indicator_params, use_chaining)
                        if is_last:
                            return indicator.wrap_results(results)
                        return results
                    return indicator, calculate_lazily
                else:
                    raise ValueError(f"{interface_func.__name__} cannot be chained.")

            return indicator.__call__(*interface_func(*args, **kwargs))
        return calculate
    return decorator

class BaseQuote(Indicator):
    is_chainable = True
    is_chainee = False
    is_chainor = True
    
    indicator_method = CsIndicator.GetBaseQuote[Quote]
    chaining_method = None
    
    list_wrap_class = None
    unit_wrap_class = None
    
@calculate_indicator(indicator=BaseQuote())
def get_base(quotes, candle_part):
    return (quotes, candle_part.cs_value)

class IndicatorChain:
    def __init__(self, quotes: Iterable[Quote], candle_part: CandlePart):
        self.chain: List[Callable] = []
        self.quotes = quotes
        self.last_indicator: Indicator = None
        if candle_part:
            # TODO: Add BaseQuote as a new indicator. And replace with using add().
            self.add(get_base, candle_part)
            # self.last_indicator = BaseQuote()
            # self.quotes = CsIndicator.GetBaseQuote[Quote](self.quotes, candle_part.cs_value)

    @classmethod
    def use_quotes(cls, quotes: Iterable[Quote], candle_part: Optional[CandlePart] = None):
        """
        Provide quotes and optionally select which candle part to use in the calculation.
        
        Note that if you specify `candle_part`, `quote` will be converted internally.
        And it may affect some of the indicators that must start from `Quote`s.
        """
        instance = cls(quotes, candle_part)
        return instance
    
    def add(self, indicator_method: Callable, *args, **kwargs):
        """Add indicator method that calculates lazily."""
        if self.last_indicator and not self.last_indicator.is_chainor:
            raise ValueError((f"{self.chain[-1].__name__} cannot be further chained with additional transforms. "
                              "See docs for more details."))

        indicator_info, chaining_method = indicator_method(*args, **kwargs, is_chaining = True)
        if self.last_indicator and not indicator_info.is_chainee:
            raise ValueError((f"{indicator_method.__name__} must be generated from quotes "
                              "and cannot be generated from results of another chain-enabled"
                              "indicator or method. See docs for more details."))
        
        self.chain.append(chaining_method)
        self.last_indicator = indicator_info
        return self

    def calc(self) -> Optional[IndicatorResults[ResultBase]]:
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
