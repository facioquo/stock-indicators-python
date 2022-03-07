
from decimal import Decimal
from typing import Optional

from stock_indicators._cstypes import Decimal as CsDecimal
from stock_indicators._cstypes import to_pydecimal
from stock_indicators.indicators.common.results import ResultBase


class CandleResult(ResultBase):
    """
    A wrapper class for a single unit of Candles.
    """

    @property
    def price(self) -> Optional[Decimal]:
        return to_pydecimal(self._csdata.Price)

    @price.setter
    def price(self, value):
        self._csdata.Price = CsDecimal(value)