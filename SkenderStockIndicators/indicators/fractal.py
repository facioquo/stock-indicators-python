from typing import Iterable, List, Type, overload
from SkenderStockIndicators._cslib import CsIndicator
from SkenderStockIndicators._cstypes import List as CsList
from SkenderStockIndicators._cstypes import Decimal as CsDecimal
from SkenderStockIndicators._cstypes import to_pydecimal
from SkenderStockIndicators.indicators.common.results import IndicatorResults, ResultBase
from SkenderStockIndicators.indicators.common.quote import Quote

#TODO: Needs to support EndType enums.
# @overload
# def get_fractal(quotes: Iterable[Quote], window_span: int) -> "FractalResults": ...
# @overload
# def get_fractal(quotes: Iterable[Quote], left_span: int, right_span: int) -> "FractalResults": ...
# def get_fractal(quotes: Iterable[Quote], left_span: int, right_span: int = None):
#     fractal_results = CsIndicator.GetFractal[Quote](CsList(Quote, quotes), left_span, right_span)
#     return FractalResults(fractal_results, FractalResult)

def get_fractal(quotes: Iterable[Quote], window_span: int):
    fractal_results = CsIndicator.GetFractal[Quote](CsList(Quote, quotes), window_span)
    return FractalResults(fractal_results, FractalResult)
 

class FractalResult(ResultBase):
    """
    A wrapper class for a single unit of Williams Fractal results.
    """

    def __init__(self, fractal_result):
        super().__init__(fractal_result)

    @property
    def fractal_bear(self):
        return to_pydecimal(self._csdata.FractalBear)

    @fractal_bear.setter
    def fractal_bear(self, value):
        self._csdata.FractalBear = CsDecimal(value)

    @property
    def fractal_bull(self):
        return to_pydecimal(self._csdata.FractalBull)

    @fractal_bull.setter
    def fractal_bull(self, value):
        self._csdata.FractalBull = CsDecimal(value)

class FractalResults(IndicatorResults[FractalResult]):
    """
    A wrapper class for the list of Williams Fractal results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: List, wrapper_class: Type[FractalResult]):
        super().__init__(data, wrapper_class)
