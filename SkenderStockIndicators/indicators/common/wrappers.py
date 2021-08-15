from Skender.Stock.Indicators import Indicator as CsIndicator
from Skender.Stock.Indicators import ResultBase as CsResultBase
from SkenderStockIndicators._cstypes import List, to_pydatetime


class IndicatorResults(list):
    """
    A wrapper class for the list of results. It provides extension methods written in CSharp implementation.
    """

    def __init__(self, data, wrapper_class):
        super(IndicatorResults, self).__init__([ wrapper_class(i) for i in data ])
        self._csdata = data
        self._wrapper_class = wrapper_class


    def _verify_data(func):
        """
        Check whether _csdata can be passed to extension method.    
        """
        def decorator(self):
            if not isinstance(self._csdata, list) or len(self._csdata) < 1:
                raise ValueError("Can't remove from empty result.")

            if not isinstance(self._csdata[0], CsResultBase):
                raise ValueError(
                    "The data should be an instance of Skender.Stock.Indicators.ResultBase class or its subclasses."
                )

            return func(self)

        return decorator


    @_verify_data
    def remove_warmup_periods(self):
        removed_results = CsIndicator.RemoveWarmupPeriods(List(type(self._csdata[0]), self._csdata))
        return IndicatorResults(removed_results, self._wrapper_class)



class ResultBase:
    """
    A wrapper class for a single unit of the results.
    """

    def __init__(self, base_result):
        super().__init__()
        self.Date = to_pydatetime(base_result.Date)