from decimal import Decimal
from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

#TODO: Needs to support EndType enums.
# @overload
# def get_fractal(quotes: Iterable[Quote], window_span: int = 2) -> "FractalResults": ...
# @overload
# def get_fractal(quotes: Iterable[Quote], left_span: int, right_span: int) -> "FractalResults": ...
# def get_fractal(quotes: Iterable[Quote], left_span: int, right_span: int = None):
#     fractal_results = CsIndicator.GetFractal[Quote](CsList(Quote, quotes), left_span, right_span)
#     return FractalResults(fractal_results, FractalResult)

def get_fractal(quotes: Iterable[Quote], window_span: int = 2):
    """Get Williams Fractal calculated.

    Williams Fractal is a retrospective price pattern that
    identifies a central high or low point over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `window_span` : int, defaults 2
            Number of span periods to the left and right of the evaluation period.

    Returns:
        `FractalResults[FractalResult]`
            FractalResults is list of FractalResult with providing useful helper methods.

    See more:
         - [Williams Fractal Reference](https://daveskender.github.io/Stock.Indicators.Python/indicators/Fractal/#content)
         - [Helper Methods](https://daveskender.github.io/Stock.Indicators.Python/utilities/#content)
    """
    fractal_results = CsIndicator.GetFractal[Quote](CsList(Quote, quotes), window_span)
    return FractalResults(fractal_results, FractalResult)


class FractalResult(ResultBase):
    """
    A wrapper class for a single unit of Williams Fractal results.
    """

    @property
    def fractal_bear(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.FractalBear)

    @fractal_bear.setter
    def fractal_bear(self, value):
        self._csdata.FractalBear = CsDecimal(value)

    @property
    def fractal_bull(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.FractalBull)

    @fractal_bull.setter
    def fractal_bull(self, value):
        self._csdata.FractalBull = CsDecimal(value)


_T = TypeVar("_T", bound=FractalResult)
class FractalResults(IndicatorResults[_T]):
    """
    A wrapper class for the list of Williams Fractal results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
