from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.indicator import Indicator, calculate_indicator
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


class BasicQuoteResult(ResultBase):
    """
    A wrapper class for a single unit of Basic Quote results.
    """

    @property
    def value(self) -> Optional[float]:
        return self._csdata.Value

    @value.setter
    def value(self, value):
        self._csdata.Value = value


_T = TypeVar("_T", bound=BasicQuoteResult)
class BasicQuoteResults(IndicatorResults[_T]):
    """
    A wrapper class for the list of Basic Quote results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """


class BasicQuote(Indicator):
    is_chainee = False
    is_chainor = True
    
    indicator_method = CsIndicator.GetBaseQuote[Quote]
    chaining_method = None
    
    list_wrap_class = BasicQuoteResults
    unit_wrap_class = BasicQuoteResult


@calculate_indicator(indicator=BasicQuote())
def get_basic_quote(quotes: Iterable[Quote], candle_part: CandlePart = CandlePart.CLOSE):
    """Get Basic Quote calculated.

    A simple quote transform (e.g. HL2, OHL3, etc.) and isolation of individual
    price quote candle parts from a full OHLCV quote.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `candle_part` : CandlePart, defaults CandlePart.CLOSE
            The OHLCV element or simply calculated value type.

    Returns:
        `BasicQuoteResults[BasicQuoteResult]`
            BasicQuoteResults is list of BasicQuoteResult with providing useful helper methods.

    See more:
         - [Basic Quote Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/BasicQuote/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    return (quotes, candle_part.cs_value)
