from typing import Iterable, Union

from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase


def get_results_as_argument(param: Iterable[Union[Quote, ResultBase]]):
    if not param or isinstance(param[0], Quote):
        arg = CsList(Quote, param)
    else:
        # Get C# IReusable objects for chaining method.
        if isinstance(param, IndicatorResults):
            param.reload()
            arg = param._csdata
        else:
            arg = CsList(type(param[0]._csdata), [ p._csdata for p in param ])

    return arg
