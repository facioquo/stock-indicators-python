from abc import ABC, abstractmethod

from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.quote import Quote

class Indicator(ABC):
    is_chainable = False
    is_chainee = False
    is_chainor = False
    
    indicator_method = None
    chaining_method = None
    
    def __call__(self, quotes, *params):
        return self._wrap_results(self._calculate(CsList(Quote, quotes), *params))

    def _calculate(self, *params, is_chaining=False):
        if is_chaining:
            if self.is_chainable:
                return self.chaining_method(*params)
            else:
                raise RuntimeError()
        else:
            return self.indicator_method(*params)

    @abstractmethod
    def _wrap_results(self, results):
        pass
