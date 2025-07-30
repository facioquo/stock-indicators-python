from datetime import datetime as PyDateTime
from typing import Callable, Iterable, List, Optional, Type, TypeVar

from stock_indicators._cslib import CsResultBase
from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators._cstypes import to_pydatetime


class ResultBase:
    """A base wrapper class for a single unit of the results."""
    
    def __init__(self, base_result: CsResultBase):
        if not isinstance(base_result, CsResultBase):
            raise TypeError("base_result must be an instance of CsResultBase")
        self._csdata = base_result

    @property
    def date(self) -> PyDateTime:
        """Get the date of this result."""
        return to_pydatetime(self._csdata.Date)

    @date.setter
    def date(self, value: PyDateTime) -> None:
        """Set the date of this result."""
        if not isinstance(value, PyDateTime):
            raise TypeError("Date must be a datetime.datetime instance")
        self._csdata.Date = CsDateTime(value)


_T = TypeVar("_T", bound=ResultBase)


class IndicatorResults(List[_T]):
    """
    A base wrapper class for the list of results.
    It provides helper methods written in CSharp implementation.
    """
    
    def __init__(self, data: Iterable, wrapper_class: Type[_T]):
        if not data:
            super().__init__()
            self._csdata = []
        else:
            super().__init__(map(wrapper_class, data))
            self._csdata = data
        self._wrapper_class = wrapper_class

    def _get_csdata_type(self):
        """Get C# result object type."""
        if len(self) == 0:
            raise ValueError("Cannot determine C# data type from empty results")
        return type(self[0]._csdata)

    def _verify_data(func: Callable):
        """Check whether `_csdata` can be passed to helper method."""
        def verify_data(self, *args):
            if not isinstance(self._csdata, Iterable) or len(self) < 1:
                raise ValueError(f"Cannot {func.__name__}() an empty result.")

            if not issubclass(self._get_csdata_type(), CsResultBase):
                raise TypeError(
                    "The data should be an instance of Skender.Stock.Indicators.ResultBase or its subclasses."
                )

            return func(self, *args)

        return verify_data

    @_verify_data
    def __add__(self, other: "IndicatorResults"):
        """Concatenate two IndicatorResults."""
        if not isinstance(other, IndicatorResults):
            raise TypeError("Can only add IndicatorResults to IndicatorResults")
        return self.__class__(list(self._csdata).__add__(list(other._csdata)), self._wrapper_class)

    @_verify_data
    def __mul__(self, value: int):
        """Repeat IndicatorResults."""
        if not isinstance(value, int):
            raise TypeError("Can only multiply IndicatorResults by integer")
        return self.__class__(list(self._csdata).__mul__(value), self._wrapper_class)

    @_verify_data
    def remove_warmup_periods(self, remove_periods: int):
        """Remove a specific quantity of results from the beginning of the results list."""
        if not isinstance(remove_periods, int):
            raise TypeError("remove_periods must be an integer.")
        
        if remove_periods < 0:
            raise ValueError("remove_periods must be non-negative.")
        
        if remove_periods >= len(self):
            return self.__class__([], self._wrapper_class)

        return self.__class__(list(self._csdata)[remove_periods:], self._wrapper_class)

    def find(self, lookup_date: PyDateTime) -> Optional[_T]:
        """
        Find indicator values on a specific date. 
        Returns `None` if no result found.
        
        Args:
            lookup_date: The date to search for
            
        Returns:
            The result for the given date or None if not found
        """
        if not isinstance(lookup_date, PyDateTime):
            raise TypeError("lookup_date must be an instance of datetime.datetime.")

        # Use binary search for better performance on large datasets
        # Since results are typically sorted by date
        try:
            return next((r for r in self if r.date.date() == lookup_date.date()), None)
        except Exception:
            # Fallback to exact match if date comparison fails
            return next((r for r in self if r.date == lookup_date), None)
