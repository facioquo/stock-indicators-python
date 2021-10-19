from typing import Iterable, List, Optional, Type
from stock_indicators._cslib import CsIndicator
from stock_indicators._cstypes import List as CsList
from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import IndicatorResults, ResultBase
from stock_indicators.indicators.common.quote import Quote

def get_bollinger_bands(quotes: Iterable[Quote], lookback_periods: int = 20, standard_deviations: float = 2):
    bollinger_bands_results = CsIndicator.GetBollingerBands[Quote](CsList(Quote, quotes), lookback_periods, CsDecimal(standard_deviations))
    return BollingerBandsResults(bollinger_bands_results, BollingerBandsResult)

class BollingerBandsResult(ResultBase):
    def __init__(self, bollinger_bands_result):
        super().__init__(bollinger_bands_result)

    @property
    def sma(self):
        return to_pydecimal(self._csdata.Sma)

    @sma.setter
    def sma(self, value):
        self._csdata.Sma = CsDecimal(value)

    @property
    def upper_band(self):
        return to_pydecimal(self._csdata.UpperBand)

    @upper_band.setter
    def upper_band(self, value):
        self._csdata.UpperBand = CsDecimal(value)

    @property
    def lower_band(self):
        return to_pydecimal(self._csdata.LowerBand)

    @lower_band.setter
    def lower_band(self, value):
        self._csdata.LowerBand = CsDecimal(value)

    @property
    def percent_b(self):
        return to_pydecimal(self._csdata.PercentB)

    @percent_b.setter
    def percent_b(self, value):
        self._csdata.PercentB = CsDecimal(value)

    @property
    def z_score(self):
        return to_pydecimal(self._csdata.ZScore)

    @z_score.setter
    def z_score(self, value):
        self._csdata.ZScore = CsDecimal(value)

    @property
    def width(self):
        return to_pydecimal(self._csdata.Width)

    @width.setter
    def width(self, value):
        self._csdata.Width = CsDecimal(value)

class BollingerBandsResults(IndicatorResults[BollingerBandsResult]):
    """
    A wrapper class for the list of Bollinger Bands results.
    It is exactly same with built-in `list` except for that it provides
    some useful helper methods written in C# implementation.
    """

    def __init__(self, data: List, wrapper_class: Type[BollingerBandsResult]):
        super().__init__(data, wrapper_class)

    @IndicatorResults._verify_data
    def remove_warmup_periods(self, remove_periods: Optional[int] = None):
        if remove_periods is not None:
            return super().remove_warmup_periods(remove_periods)
        
        removed_results = CsIndicator.RemoveWarmupPeriods(CsList(type(self._csdata[0]), self._csdata))

        return self.__class__(removed_results, self._wrapper_class)
        