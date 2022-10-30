from abc import ABC, abstractmethod

from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.quote import Quote

class Indicator(ABC):
    @property
    @abstractmethod
    def is_chainable(self):
        pass

    @property
    @abstractmethod
    def is_chainee(self):
        pass

    @property
    @abstractmethod
    def is_chainor(self):
        pass

    @property
    @abstractmethod
    def indicator_method(self):
        pass

    @property
    @abstractmethod
    def chaining_method(self):
        pass

    @property
    @abstractmethod
    def list_wrap_class(self):
        pass

    @property
    @abstractmethod
    def unit_wrap_class(self):
        pass

    def __call__(self, quotes, *params):
        return self.wrap_results(self.calculate((CsList(Quote, quotes), *params)))

    def calculate(self, params, is_chaining = False):
        if is_chaining:
            if self.is_chainable:
                return self.chaining_method(*params)
            else:
                raise RuntimeError(f"{self.__class__.__name__} cannot be used in chaining.")
        else:
            return self.indicator_method(*params)

    def wrap_results(self, results):
        return self.list_wrap_class(results, self.unit_wrap_class)
