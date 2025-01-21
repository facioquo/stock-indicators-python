"""
Skender.Stock.Indicators
~~~~~~~~~~~~~~~~~~~~~~~~

This module loads `Skender.Stock.Indicators.dll`(v2.5.0), which is a compiled library package
from <https://github.com/DaveSkender/Stock.Indicators>, written in C#.

The target framework of dll is `.NET 6.0`.
"""

import sys
import platform
from pathlib import Path
import os
from pythonnet import load
import logging
import json

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def verify_dotnet_environment():
    """Verify .NET environment setup"""
    dotnet_root = os.environ.get("DOTNET_ROOT")
    logger.debug(f"DOTNET_ROOT: {dotnet_root}")

    if platform.system() == "Darwin":
        if not dotnet_root:
            os.environ["DOTNET_ROOT"] = "/usr/local/share/dotnet"
            logger.debug("Setting DOTNET_ROOT for macOS")

try:
    verify_dotnet_environment()

    # Get absolute paths
    base_path = Path(__file__).parent.resolve()
    runtime_config_path = base_path / "runtimeconfig.json"
    dll_path = base_path / "lib" / "Skender.Stock.Indicators.dll"

    logger.debug(f"Base path: {base_path}")
    logger.debug(f"Runtime config path: {runtime_config_path}")
    logger.debug(f"DLL path: {dll_path}")

    if not runtime_config_path.exists():
        raise FileNotFoundError(f"runtimeconfig.json not found at: {runtime_config_path}")

    if not dll_path.exists():
        raise FileNotFoundError(f"DLL not found at: {dll_path}")

    # Initialize runtime based on platform using runtimeconfig.json
    if platform.system() == "Darwin":
        load("coreclr",
             dotnet_root=os.environ["DOTNET_ROOT"],
             runtime_config=str(runtime_config_path))
    else:
        load("coreclr", runtime_config=str(runtime_config_path))

    import clr
    logger.debug(f"CLR loaded successfully on {platform.system()}")

    # Set assembly resolve path
    from System import AppDomain, IO
    current_domain = AppDomain.CurrentDomain
    assembly_path = IO.Path.GetDirectoryName(str(dll_path))
    current_domain.SetData("PROBING_PATH", assembly_path)
    logger.debug(f"Set assembly probing path to: {assembly_path}")

    try:
        # Load the assembly first
        from System.Reflection import Assembly
        logger.debug(f"Loading assembly from: {dll_path}")
        assembly = Assembly.LoadFile(str(dll_path))
        logger.debug(f"Assembly loaded: {assembly.FullName}")

        # Add reference after successful load
        clr.AddReference(assembly.FullName)
        logger.debug("Assembly reference added")

    except Exception as asm_error:
        logger.error(f"Error loading assembly: {str(asm_error)}")
        if hasattr(asm_error, 'LoaderExceptions'):
            for ex in asm_error.LoaderExceptions:
                logger.error(f"Loader exception: {str(ex)}")
        raise

except Exception as e:
    logger.error(f"Detailed error information: {str(e)}")
    if hasattr(e, '__cause__'):
        logger.error(f"Caused by: {str(e.__cause__)}")
    raise ImportError(
        "Stock Indicators initialization failed.\n"
        "Please ensure .NET 6.0+ is installed: https://dotnet.microsoft.com/download\n"
        f"Error: {str(e)}"
    ) from e

# Built-in
from System import DateTime as CsDateTime
from System import Decimal as CsDecimal
from System import Enum as CsEnum
from System.Collections.Generic import IEnumerable as CsIEnumerable
from System.Collections.Generic import List as CsList
from System.Globalization import CultureInfo as CsCultureInfo

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

# Export initialized modules
__all__ = ['clr']
