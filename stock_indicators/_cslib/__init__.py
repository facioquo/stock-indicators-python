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
from typing import Optional

from pythonnet import load

# Setup logging
from stock_indicators.logging_config import configure_logging

configure_logging(debug=False)  # Set to True if you need debug this module

logger = logging.getLogger(__name__)


class StockIndicatorsInitializationError(ImportError):
    """Custom exception for Stock Indicators initialization failures."""


def _initialize_clr() -> None:
    """Initialize the CLR runtime."""
    try:
        load(runtime="coreclr")
        import clr
        logger.debug("CLR loaded successfully on %s", platform.system())
        return clr
    except Exception as e:
        error_msg = (
            "Failed to load .NET CLR runtime.\n"
            "Please ensure .NET 6.0+ is installed: https://dotnet.microsoft.com/download\n"
            f"Platform: {platform.system()}\n"
            f"Error: {str(e)}"
        )
        raise StockIndicatorsInitializationError(error_msg) from e


def _setup_assembly_probing(dll_path: Path) -> None:
    """Setup assembly probing path for .NET dependency resolution."""
    try:
        from System import IO, AppDomain

        current_domain = AppDomain.CurrentDomain
        assembly_path = IO.Path.GetDirectoryName(str(dll_path))
        current_domain.SetData("PROBING_PATH", assembly_path)
        logger.debug("Set assembly probing path to: %s", assembly_path)
    except Exception as e:
        logger.warning("Failed to set assembly probing path: %s", str(e))


def _load_assembly(dll_path: Path):
    """Load the Stock Indicators assembly."""
    try:
        from System.Reflection import Assembly

        if not dll_path.exists():
            raise FileNotFoundError(f"Assembly not found at: {dll_path}")

        logger.debug("Loading assembly from: %s", dll_path)
        assembly = Assembly.LoadFile(str(dll_path))
        logger.debug("Assembly loaded: %s", assembly.FullName)

        return assembly
    except Exception as e:
        error_msg = (
            f"Failed to load Stock Indicators assembly from: {dll_path}\n"
            "Please ensure the .NET assembly is present and compatible.\n"
            f"Error: {str(e)}"
        )
        raise StockIndicatorsInitializationError(error_msg) from e


def _add_assembly_reference(assembly, clr) -> None:
    """Add reference to the loaded assembly."""
    try:
        clr.AddReference(assembly.FullName)  # pylint: disable=no-member
        logger.debug("Assembly reference added successfully")
    except Exception as e:
        error_msg = (
            f"Failed to add reference to assembly: {assembly.FullName}\n"
            f"Error: {str(e)}"
        )
        raise StockIndicatorsInitializationError(error_msg) from e


try:
    # Initialize CLR
    clr = _initialize_clr()

    # Get assembly path
    base_path = Path(__file__).parent.resolve()
    dll_path = base_path / "lib" / "Skender.Stock.Indicators.dll"

    # Setup assembly probing
    _setup_assembly_probing(dll_path)

    # Load assembly
    assembly = _load_assembly(dll_path)

    # Add assembly reference
    _add_assembly_reference(assembly, clr)

except Exception as e:
    # Re-raise our custom exception or create one from unexpected errors
    if isinstance(e, StockIndicatorsInitializationError):
        raise
    
    error_msg = (
        "Stock Indicators initialization failed due to unexpected error.\n"
        "Please ensure .NET 6.0+ is installed: https://dotnet.microsoft.com/download\n"
        f"Error: {str(e)}"
    )
    raise StockIndicatorsInitializationError(error_msg) from e

# Library modules (common) - Import after successful initialization
try:
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

    # Built-in System types
    from System import DateTime as CsDateTime
    from System import Decimal as CsDecimal
    from System import Enum as CsEnum
    from System.Collections.Generic import IEnumerable as CsIEnumerable
    from System.Collections.Generic import List as CsList
    from System.Globalization import CultureInfo as CsCultureInfo
    from System.Globalization import NumberStyles as CsNumberStyles

    logger.info("Stock Indicators library initialized successfully")

except ImportError as e:
    error_msg = (
        "Failed to import Stock Indicators types after successful assembly loading.\n"
        "This may indicate a version mismatch or missing dependencies.\n"
        f"Error: {str(e)}"
    )
    raise StockIndicatorsInitializationError(error_msg) from e
