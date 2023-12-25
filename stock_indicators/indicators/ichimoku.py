from decimal import Decimal
from typing import Iterable, Optional, TypeVar, overload

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


@overload
def get_ichimoku(quotes: Iterable[Quote], tenkan_periods: int = 9,
                 kijun_periods: int = 26, senkou_b_periods: int = 52) -> "IchimokuResults[IchimokuResult]": ...
@overload
def get_ichimoku(quotes: Iterable[Quote], tenkan_periods: int,
                 kijun_periods: int, senkou_b_periods: int,
                 offset_periods: int) -> "IchimokuResults[IchimokuResult]": ...
@overload
def get_ichimoku(quotes: Iterable[Quote], tenkan_periods: int,
                 kijun_periods: int, senkou_b_periods: int,
                 senkou_offset: int, chikou_offset: int) -> "IchimokuResults[IchimokuResult]": ...
def get_ichimoku(quotes: Iterable[Quote], tenkan_periods: int = None,
                 kijun_periods: int = None, senkou_b_periods: int = None,
                 senkou_offset: int = None, chikou_offset: int = None):
    """Get Ichimoku Cloud calculated.

    Ichimoku Cloud, also known as Ichimoku Kinkō Hyō, is a collection of indicators
    that depict support and resistance, momentum, and trend direction.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `tenkan_periods` : int
            Number of periods in the Tenkan-sen midpoint evaluation.

        `kijun_periods` : int
            Number of periods in the shorter Kijun-sen midpoint evaluation.
            This value is also used to offset Senkou and Chinkou spans, if the both aren't specified.

        `senkou_b_periods` : int
            Number of periods in the longer Senkou leading span B midpoint evaluation.

        `offset_periods` : int
            Number of periods to displace the Senkou and Chikou Spans.

        `senkou_offset` : int
            Number of periods to displace the Senkou Spans.

        `chikou_offset` : int
            Number of periods in displace the Chikou Span.

    Returns:
        `IchimokuResults[IchimokuResult]`
            IchimokuResults is list of IchimokuResult with providing useful helper methods.

    See more:
         - [Ichimoku Cloud Reference](https://python.stockindicators.dev/indicators/Ichimoku/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    if chikou_offset is None:
        if senkou_offset is None:
            if tenkan_periods is None: tenkan_periods = 9
            if kijun_periods is None: kijun_periods = 26
            if senkou_b_periods is None: senkou_b_periods = 52
            senkou_offset = kijun_periods
        chikou_offset = senkou_offset

    results = CsIndicator.GetIchimoku[Quote](CsList(Quote, quotes), tenkan_periods,
                                             kijun_periods, senkou_b_periods,
                                             senkou_offset, chikou_offset)
    return IchimokuResults(results, IchimokuResult)


class IchimokuResult(ResultBase):
    """
    A wrapper class for a single unit of Ichimoku Cloud results.
    """

    @property
    def tenkan_sen(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.TenkanSen)

    @tenkan_sen.setter
    def tenkan_sen(self, value):
        self._csdata.TenkanSen = CsDecimal(value)

    @property
    def kijun_sen(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.KijunSen)

    @kijun_sen.setter
    def kijun_sen(self, value):
        self._csdata.KijunSen = CsDecimal(value)

    @property
    def senkou_span_a(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.SenkouSpanA)

    @senkou_span_a.setter
    def senkou_span_a(self, value):
        self._csdata.SenkouSpanA = CsDecimal(value)

    @property
    def senkou_span_b(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.SenkouSpanB)

    @senkou_span_b.setter
    def senkou_span_b(self, value):
        self._csdata.SenkouSpanB = CsDecimal(value)

    @property
    def chikou_span(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.ChikouSpan)

    @chikou_span.setter
    def chikou_span(self, value):
        self._csdata.ChikouSpan = CsDecimal(value)


_T = TypeVar("_T", bound=IchimokuResult)
class IchimokuResults(IndicatorResults[_T]):
    """
    A wrapper class for the list of Ichimoku Cloud results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """
