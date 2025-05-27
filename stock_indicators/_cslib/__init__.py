"""
Skender.Stock.Indicators
~~~~~~~~~~~~~~~~~~~~~~~~

This module loads `Skender.Stock.Indicators.dll`(v2.6.1), which is a compiled library
package from <https://github.com/DaveSkender/Stock.Indicators>, written in C#.

The target framework of dll is `.NET 6.0`.
"""

import logging
import platform
from pathlib import Path

from pythonnet import load

# Setup logging
from stock_indicators.logging_config import configure_logging

configure_logging(debug=False)  # Set to True if you need debug this module

logger = logging.getLogger(__name__)

try:
    # Load CLR
    load(runtime="coreclr")
    import clr
    logger.debug("CLR loaded successfully on %s", platform.system())

    # Get absolute paths
    base_path = Path(__file__).parent.resolve()
    dll_path = base_path / "lib" / "Skender.Stock.Indicators.dll"
    
    # Set assembly resolve path
    from System import IO, AppDomain

    current_domain = AppDomain.CurrentDomain
    assembly_path = IO.Path.GetDirectoryName(str(dll_path))
    current_domain.SetData("PROBING_PATH", assembly_path)
    logger.debug("Set assembly probing path to: %s", assembly_path)

    try:
        # Load the assembly first
        from System.Reflection import Assembly

        logger.debug("Loading assembly from: %s", dll_path)
        assembly = Assembly.LoadFile(str(dll_path))
        logger.debug("Assembly loaded: %s", assembly.FullName)

        # Add reference after successful load
        clr.AddReference(assembly.FullName)  # pylint: disable=no-member
        logger.debug("Assembly reference added")

    except Exception as asm_error:
        logger.error("Error loading assembly: %s", str(asm_error))
        if hasattr(asm_error, "LoaderExceptions"):
            for ex in asm_error.LoaderExceptions:
                logger.error("Loader exception: %s", str(ex))
        raise

except Exception as e:
    logger.error("Detailed error information: %s", str(e))
    if hasattr(e, "__cause__") and e.__cause__ is not None:
        logger.error("Caused by: %s", str(e.__cause__))
    error_msg = (
        "Stock Indicators initialization failed.\n"
        "Please ensure .NET 6.0+ is installed: https://dotnet.microsoft.com/download\n"
        f"Error: {str(e)}"
    )
    raise ImportError(error_msg) from e

# Library modules (common)
from Skender.Stock.Indicators import BetaType as CsBetaType
from Skender.Stock.Indicators import CandlePart as CsCandlePart
from Skender.Stock.Indicators import CandleProperties as CsCandleProperties
from Skender.Stock.Indicators import ChandelierType as CsChandelierType
from Skender.Stock.Indicators import EndType as CsEndType
from Skender.Stock.Indicators import Indicator as CsIndicator
from Skender.Stock.Indicators import Match as CsMatch
from Skender.Stock.Indicators import MaType as CsMaType
from Skender.Stock.Indicators import PeriodSize as CsPeriodSize
from Skender.Stock.Indicators import PivotPointType as CsPivotPointType
from Skender.Stock.Indicators import PivotTrend as CsPivotTrend
from Skender.Stock.Indicators import Quote as CsQuote
from Skender.Stock.Indicators import QuoteUtility as CsQuoteUtility
from Skender.Stock.Indicators import ResultBase as CsResultBase
from Skender.Stock.Indicators import ResultUtility as CsResultUtility

# Built-in
from System import DateTime as CsDateTime
from System import Decimal as CsDecimal
from System import Enum as CsEnum
from System.Collections.Generic import IEnumerable as CsIEnumerable
from System.Collections.Generic import List as CsList
from System.Globalization import CultureInfo as CsCultureInfo
from System.Globalization import NumberStyles as CsNumberStyles
