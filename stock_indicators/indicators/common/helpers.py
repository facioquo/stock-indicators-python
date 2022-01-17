from typing import Iterable, Optional
from typing_extensions import Self

from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.results import IndicatorResults
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList


class RemoveWarmupMixin:
    """Mixin for remove_warmup_periods()."""
    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None) -> Self:
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)

        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)


class ToQuotesMixin:
    """Mixin for to_quotes()."""
    @IndicatorResults._verify_data
    def to_quotes(self) -> Iterable[Quote]:
        quotes = CsIndicator.ConvertToQuotes(CsList(type(self._csdata[0]), self._csdata))

        return [ Quote.from_csquote(q) for q in quotes ]