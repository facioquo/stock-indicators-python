"""
Skender.Stock.Indicators
~~~~~~~~~~~~~~~~~~~~~~~~

This module loads `Skender.Stock.Indicators.dll`(v2.5.0), which is a compiled library package
from <https://github.com/DaveSkender/Stock.Indicators>, written in C#.

The target framework of dll is `.NET 6.0`.
"""

import os
from pythonnet import load

try:
    load(runtime="coreclr")
    import clr
except Exception as e:
    raise ImportError("Stock Indicators for Python has a dependency on CLR.\n"
                      "Install .NET SDK 6.0 (or newer) in your environment to add the required CLR capability.") from e

skender_stock_indicators_dll_path = os.path.join(
    os.path.dirname(__file__),
    "lib/Skender.Stock.Indicators.dll"
)
clr.AddReference(skender_stock_indicators_dll_path)
clr.AddReference('System.Collections')

# Built-in
from System import DateTime as CsDateTime
from System import Decimal as CsDecimal
from System import Enum as CsEnum
from System.Globalization import CultureInfo as CsCultureInfo
from System.Collections.Generic import IEnumerable as CsIEnumerable
from System.Collections.Generic import List as CsList

# Classes
from Skender.Stock.Indicators import CandleProperties as CsCandleProperties
from Skender.Stock.Indicators import Indicator as CsIndicator
from Skender.Stock.Indicators import Quote as CsQuote
from Skender.Stock.Indicators import QuoteUtility as CsQuoteUtility
from Skender.Stock.Indicators import ResultBase as CsResultBase
from Skender.Stock.Indicators import ResultUtility as CsResultUtility

# Enums
from Skender.Stock.Indicators import BetaType as CsBetaType
from Skender.Stock.Indicators import CandlePart as CsCandlePart
from Skender.Stock.Indicators import ChandelierType as CsChandelierType
from Skender.Stock.Indicators import EndType as CsEndType
from Skender.Stock.Indicators import MaType as CsMaType
from Skender.Stock.Indicators import PeriodSize as CsPeriodSize
from Skender.Stock.Indicators import PivotPointType as CsPivotPointType
from Skender.Stock.Indicators import PivotTrend as CsPivotTrend
from Skender.Stock.Indicators import Match as CsMatch

# Exceptions
from System import FormatException as CsFormatException
