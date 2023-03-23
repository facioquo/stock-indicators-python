from itertools import islice
from typing import Iterable, Union

from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def get_results_as_argument(iterable: Iterable[Union[Quote, ResultBase]]):
    first = next(islice(iterable, 0, None), None)
    
    if not iterable or isinstance(first, Quote):
        return CsList(Quote, iterable)
    elif isinstance(first, ResultBase):
        # Get C# IReusable objects for chaining method.
        if isinstance(iterable, IndicatorResults):
            iterable.reload()
            return iterable._csdata
        else:
            return CsList(type(first._csdata), [ p._csdata for p in iterable ])
