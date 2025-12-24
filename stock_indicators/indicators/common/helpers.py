from typing import Optional

from typing_extensions import Self

from stock_indicators._cslib import CsIEnumerable, CsIndicator, CsResultUtility
from stock_indicators._cstypes import List as CsList
from stock_indicators.exceptions import IndicatorCalculationError
from stock_indicators.indicators.common.results import IndicatorResults


class RemoveWarmupMixin:
    """IndicatorResults Mixin for remove_warmup_periods()."""

    @IndicatorResults._verify_data
    def remove_warmup_periods(
        self: IndicatorResults, remove_periods: Optional[int] = None
    ) -> Self:
        """
        Remove the recommended(or specified) quantity of results from the beginning of the results list.

        Args:
            remove_periods: Number of periods to remove. If None, removes recommended warmup periods.

        Returns:
            New IndicatorResults instance with warmup periods removed.
        """
        if remove_periods is not None:
            if not isinstance(remove_periods, int):
                raise TypeError("remove_periods must be an integer")
            if remove_periods < 0:
                raise ValueError("remove_periods must be non-negative")
            return super().remove_warmup_periods(remove_periods)

        try:
            removed_results = CsIndicator.RemoveWarmupPeriods(
                CsList(self._get_csdata_type(), self._csdata)
            )
            return self.__class__(removed_results, self._wrapper_class)
        except Exception as e:
            raise IndicatorCalculationError("remove_warmup_periods failed") from e


class CondenseMixin:
    """IndicatorResults Mixin for condense()."""

    @IndicatorResults._verify_data
    def condense(self: IndicatorResults) -> Self:
        """
        Removes non-essential records containing null values with unique consideration for this indicator.

        Returns:
            New IndicatorResults instance with null values removed.
        """
        cs_results_type = self._get_csdata_type()

        try:
            # Try to find the specific overloaded method first
            try:
                condense_method = CsIndicator.Condense.Overloads[
                    CsIEnumerable[cs_results_type]
                ]
            except TypeError:
                # Fall back to generic utility method
                condense_method = CsResultUtility.Condense[cs_results_type]

            condensed_results = condense_method(CsList(cs_results_type, self._csdata))
            return self.__class__(condensed_results, self._wrapper_class)

        except Exception as e:
            raise ValueError("Failed to condense results") from e
