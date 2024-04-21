from typing import Callable, Optional

from typing_extensions import Self

from stock_indicators._cslib import CsIndicator, CsResultUtility, CsCandleResult, CsCandlesticks, CsIEnumerable
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.results import IndicatorResults


class RemoveWarmupMixin:
    """Mixin for remove_warmup_periods()."""
    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None) -> Self:
        """
        Remove the recommended(or specified) quantity of results from the beginning of the results list.
        """
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(self._get_csdata_type(), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)


class CondenseMixin:
    """Mixin for condense()."""
    @IndicatorResults._verify_data
    def condense(self) -> Self:
        """
        Removes non-essential records containing null values with unique consideration for this indicator.
        """
        cs_results = CsList(self._get_csdata_type(), self._csdata)
        condensed_results = self._get_condense_method(self._get_csdata_type()).__call__(cs_results)

        return self.__class__(condensed_results, self._wrapper_class)

    def _get_condense_method(self, cs_result_type) -> Callable:
        if issubclass(cs_result_type, CsCandleResult):
            return CsCandlesticks.Condense

        try: # to check whether there's matched overloaded method.
            return CsIndicator.Condense.Overloads[CsIEnumerable[cs_result_type]]
        except TypeError:
            return CsResultUtility.Condense[cs_result_type]
