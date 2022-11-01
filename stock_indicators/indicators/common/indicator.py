from abc import ABC, abstractmethod
from functools import wraps
from typing import Callable

from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.quote import Quote

class Indicator(ABC):
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

    @property
    def is_chainable(self):
        return self.is_chainee or self.is_chainor

    def __call__(self, quotes, *params):
        return self.wrap_results(self.calculate((CsList(Quote, quotes), *params)))

    def calculate(self, params, is_chaining = False):
        if is_chaining:
            if self.is_chainee:
                return self.chaining_method(*params)
            else:
                raise RuntimeError(f"{self.__class__.__name__} cannot be used as chainee.")
        else:
            return self.indicator_method(*params)

    def wrap_results(self, results):
        return self.list_wrap_class(results, self.unit_wrap_class)


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
