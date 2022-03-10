"""
Skender.Stock.Indicators
~~~~~~~~~~~~~~~~~~~~~~~~

This module loads `Skender.Stock.Indicators.dll`, which is a compiled library package
from <https://github.com/DaveSkender/Stock.Indicators>, written in C#.

It is currently using `.NET Standard 2.0`.
"""

import os
import clr

skender_stock_indicators_dll_path = os.path.join(
    os.path.dirname(__file__),
    "lib/Skender.Stock.Indicators.dll"
)
clr.AddReference(skender_stock_indicators_dll_path)
clr.AddReference('System.Collections')

from System import DateTime as CsDateTime
from System import Decimal as CsDecimal
from System import Enum as CsEnum
from System.Globalization import CultureInfo
from System.Collections.Generic import List as CsList

from Skender.Stock.Indicators import Indicator as CsIndicator
from Skender.Stock.Indicators import Quote as CsQuote
from Skender.Stock.Indicators import ResultBase as CsResultBase
from Skender.Stock.Indicators import CandlePart as CsCandlePart
from Skender.Stock.Indicators import Signal as CsSignal
