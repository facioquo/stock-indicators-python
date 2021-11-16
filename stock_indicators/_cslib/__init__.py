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

from Skender.Stock.Indicators import Indicator as CsIndicator
from Skender.Stock.Indicators import Quote as CsQuote
from Skender.Stock.Indicators import ResultBase as CsResultBase
