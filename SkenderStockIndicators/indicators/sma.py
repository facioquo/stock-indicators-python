from Skender.Stock.Indicators import Indicator
from SkenderStockIndicators._cstypes import List, to_pydecimal
from SkenderStockIndicators.indicators.common.wrappers import IndicatorResults, ResultBase
from SkenderStockIndicators.indicators.common.quote import Quote


def get_sma(quotes, lookbackPeriods: int):
    sma_list = Indicator.GetSma[Quote](List(Quote, quotes), lookbackPeriods)
    return IndicatorResults(sma_list, SmaResult)

def get_sma_extended(quotes, lookbackPeriods: int):
    sma_extended_list = Indicator.GetSmaExtended[Quote](List(Quote, quotes), lookbackPeriods)
    return IndicatorResults(sma_extended_list, SmaExtendedResult)


class SmaResult(ResultBase):
    def __init__(self, sma_result):
        super().__init__(sma_result)
        self.Sma = to_pydecimal(sma_result.Sma)

class SmaExtendedResult(SmaResult):
    def __init__(self, sma_extended_result):
        super().__init__(sma_extended_result)
        self.Mad = to_pydecimal(sma_extended_result.Mad)
        self.Mse = to_pydecimal(sma_extended_result.Mse)
        self.Mape = to_pydecimal(sma_extended_result.Mape)


