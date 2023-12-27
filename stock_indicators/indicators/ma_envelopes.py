from typing import Iterable, Optional, TypeVar

from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators.indicators.common.enums import MAType
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote


def get_ma_envelopes(quotes: Iterable[Quote], lookback_periods: int,
                percent_offset: float = 2.5, ma_type: MAType = MAType.SMA):
    """Get Moving Average Envelopes calculated.

    Moving Average Envelopes is a price band overlay that is offset
    from the moving average of Close price over a lookback window.

    Parameters:
        `quotes` : Iterable[Quote]
            Historical price quotes.

        `lookback_periods` : int
            Number of periods in the lookback window.

        `percent_offset` : float, defaults 2.5
            Percent offset for envelope width.

        `ma_type` : MAType, defaults MAType.SMA
            Moving average type (e.g. EMA, HMA, TEMA, etc.).

    Returns:
        `MAEnvelopeResults[MAEnvelopeResult]`
            MAEnvelopeResults is list of MAEnvelopeResult with providing useful helper methods.

    See more:
         - [Moving Average Envelopes Reference](https://python.stockindicators.dev/indicators/MaEnvelopes/#content)
         - [Helper Methods](https://python.stockindicators.dev/utilities/#content)
    """
    results = CsIndicator.GetMaEnvelopes[Quote](CsList(Quote, quotes), lookback_periods,
                                            percent_offset, ma_type.cs_value)
    return MAEnvelopeResults(results, MAEnvelopeResult)


class MAEnvelopeResult(ResultBase):
    """
    A wrapper class for a single unit of Moving Average Envelopes results.
    """

    @property
    def upper_envelope(self) -> Optional[float]:
        return self._csdata.UpperEnvelope

    @upper_envelope.setter
    def upper_envelope(self, value):
        self._csdata.UpperEnvelope = value

    @property
    def center_line(self) -> Optional[float]:
        return self._csdata.Centerline

    @center_line.setter
    def center_line(self, value):
        self._csdata.Centerline = value

    @property
    def lower_envelope(self) -> Optional[float]:
        return self._csdata.LowerEnvelope

    @lower_envelope.setter
    def lower_envelope(self, value):
        self._csdata.LowerEnvelope = value


_T = TypeVar("_T", bound=MAEnvelopeResult)
class MAEnvelopeResults(IndicatorResults[_T]):
    """
    A wrapper class for the list of Moving Average Envelopes results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in CSharp implementation.
    """
