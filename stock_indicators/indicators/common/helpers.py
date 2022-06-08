from warnings import warn
from typing import List, Optional

from typing_extensions import Self

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.quote import Quote
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


class ToQuotesMixin:
    """Mixin for to_quotes()."""
    @IndicatorResults._verify_data
    def to_quotes(self) -> List[Quote]:
        """Deprecated.
        Convert indicator results into historical quotes."""
        warn('The .to_quotes() method is deprecated.', DeprecationWarning, stacklevel=2)

        quotes = CsIndicator.ConvertToQuotes(CsList(self._get_csdata_type(), self._csdata))

        return [ Quote.from_csquote(q) for q in quotes ]
