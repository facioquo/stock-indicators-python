from functools import wraps
from typing import Callable, Iterable, List, Optional

from stock_indicators._cslib import CsIndicator, CsIReusableResult
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def chainable(is_chainable: bool, calc_func: Callable, wrap_func: Callable):
    def decorator(interface_func: Callable):
        def create_chaining_method(*args, **kwargs):
            is_chaining = kwargs.pop("is_chaining", False)

            if is_chaining:
                if is_chainable:
                    @wraps(interface_func)
                    def calculate_lazily(quotes, is_last: bool = False):
                        indicator_params = interface_func(CsList(CsIReusableResult, quotes), *args, **kwargs)
                        results = calc_func(indicator_params, is_chaining)
                        if is_last:
                            return wrap_func(results)
                        return results
                    return calculate_lazily
                else:
                    raise ValueError(f"{interface_func.__name__} cannot be chained.")
            
            quotes, *indicator_params = interface_func(*args, **kwargs)
            results = calc_func((CsList(Quote, quotes), *indicator_params), is_chaining)
            return wrap_func(results)
        return create_chaining_method
    return decorator


class IndicatorChain:
    def __init__(self, quotes: Iterable, candle_part: CandlePart):
        self.chain: List[Callable] = []
        self.quotes = CsIndicator.GetBaseQuote[Quote](CsList(Quote, quotes), candle_part.cs_value)

    @classmethod
    def use_quotes(cls, quotes: Iterable, candle_part: CandlePart = CandlePart.CLOSE):
        """Provide quotes and optionally select which candle part to use in the calculation."""
        instance = cls(quotes, candle_part)
        return instance
    
    def add(self, indicator: Callable, *args, **kwargs):
        """Add indicator method that calculates lazily."""
        chaining_method = indicator(*args, **kwargs, is_chaining = True)
        self.chain.append(chaining_method)
        return self

    def calc(self) -> Optional[IndicatorResults[ResultBase]]:
        """Calculate all chained indicators."""
        results = self.quotes
        if self.chain:
            results = self.quotes
            last_indicator = self.chain.pop()

            try:
                for idx, indicator in enumerate(self.chain):
                    results = indicator(results)
                    
                idx += 1
                results = last_indicator(results, is_last = True)
            except TypeError as e:
                if idx < 1:
                    raise ValueError((f"{self.chain[idx].__name__}(index:{idx}) must be generated"
                                      "from quotes and cannot be generated from results of another chain-enabled"
                                      "indicator or method. See docs for more details.")) from e
                else:
                    raise ValueError((f"{self.chain[idx-1].__name__}(index:{idx-1}) cannot be further chained with additional transforms.")) from e

        return results
