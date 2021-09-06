"""
Skender.Stock.Indicators
~~~~~~~~~~~~~~~~~~~~~~~~

This module loads `Skender.Stock.Indicators.dll`, which is a compiled library package
from <https://github.com/DaveSkender/Stock.Indicators>, written in C#.

It is currently using `.NET Standard 2.0`.
"""

import os
import sys
import clr

dir = os.path.dirname(__file__)
skender_stock_indicators_dll = os.path.join(dir, "lib/Skender.Stock.Indicators.dll")
clr.AddReference(skender_stock_indicators_dll)
clr.AddReference('System.Collections')

from Skender.Stock.Indicators import Indicator as CsIndicator
from Skender.Stock.Indicators import Quote as CsQuote
from Skender.Stock.Indicators import ResultBase as CsResultBase