from typing import Optional

from typing_extensions import Self

from stock_indicators._cslib import CsIndicator, CsIEnumerable, CsResultUtility
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.results import IndicatorResults


class RemoveWarmupMixin:
    """IndicatorResults Mixin for remove_warmup_periods()."""
    @IndicatorResults._verify_data
    def remove_warmup_periods(self: IndicatorResults, remove_periods: Optional[int] = None) -> Self:
        """
        Remove the recommended(or specified) quantity of results from the beginning of the results list.
        """
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(self._get_csdata_type(), self._csdata))
        return self.__class__(removed_results, self._wrapper_class)


class CondenseMixin:
    """IndicatorResults Mixin for condense()."""
    @IndicatorResults._verify_data
    def condense(self: IndicatorResults) -> Self:
        """
        Removes non-essential records containing null values with unique consideration for this indicator.
        """
        cs_results_type = self._get_csdata_type()
        try: # to check whether there's matched overloaded method.
            condense_method = CsIndicator.Condense.Overloads[CsIEnumerable[cs_results_type]]
        except TypeError:
            condense_method = CsResultUtility.Condense[cs_results_type]

        condensed_results = condense_method(CsList(cs_results_type, self._csdata))
        return self.__class__(condensed_results, self._wrapper_class)
