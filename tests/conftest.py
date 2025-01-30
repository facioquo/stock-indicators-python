import csv
import logging
import os
import platform
from datetime import datetime
from decimal import Decimal, DecimalException
from pathlib import Path

import pytest

from stock_indicators._cslib import clr
from stock_indicators.indicators.common import Quote  # pre-initialized
from stock_indicators.logging_config import configure_logging


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    configure_logging(debug=True)


# Setup logging for this module
logger = logging.getLogger(__name__)


def verify_dotnet():
    """Verify .NET environment setup"""
    dotnet_root = os.environ.get("DOTNET_ROOT")
    logger.debug("DOTNET_ROOT: %s", dotnet_root)
    if platform.system() == "Darwin" and not dotnet_root:
        raise EnvironmentError(
            "DOTNET_ROOT not set. Please restart terminal after installation."
        )


# Initialize .NET runtime before imports
verify_dotnet()

# Constants
base_dir = Path(__file__).parent.parent / "test_data"


@pytest.fixture(autouse=True)
def verify_environment():
    """Verify environment is properly setup"""
    verify_dotnet()
    return True


@pytest.fixture(autouse=True, scope="session")
def setup_clr_culture():
    """Configure CLR culture settings for all tests."""
    import clr
    from System.Globalization import CultureInfo
    from System.Threading import Thread

    # Get current locale from environment
    locale = os.getenv("LC_ALL", "").split(".")[0].replace("_", "-")
    if locale:
        try:
            culture = CultureInfo(locale)
            Thread.CurrentThread.CurrentCulture = culture
            Thread.CurrentThread.CurrentUICulture = culture
            logger.debug("Set CLR culture to: %s", culture.Name)
        except (ValueError, AttributeError) as e:
            logger.warning("Failed to set CLR culture: %s", e)


# --- Utility Functions ---------------------------------------------------


def get_data_from_csv(filename):
    """Read from CSV file."""

    quotes_dir = base_dir / "quotes"
    if not base_dir.exists() or not quotes_dir.exists():
        raise FileNotFoundError(
            "Test data not found. Please see README.md for test data setup instructions."
        )

    data_path = quotes_dir / f"{filename}.csv"
    logger.debug("Loading test data from: %s", data_path)

    if not data_path.exists():
        raise FileNotFoundError(f"Test data file not found: {filename}")

    with open(data_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data[1:]  # skips the first row, those are headers


def parse_decimal(value):
    """Parse decimal value."""

    try:
        return f"{Decimal(value):f}"
    except DecimalException:
        return None


def parse_date(date_str):
    """Parse date value. Input format must be '%Y-%m-%d'"""

    try:
        if len(date_str) <= 10:
            return datetime.strptime(date_str, "%Y-%m-%d")
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return datetime.now()


# --- Core Quote Fixtures ------------------------------------------------


@pytest.fixture(scope="session")
def quotes(days: int = 502):
    rows = get_data_from_csv("Default")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[1]),
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
            )
        )

    h.reverse()
    return h[:days]


@pytest.fixture(scope="session")
def quotes_bad(days: int = 502):
    rows = get_data_from_csv("Bad")

    h = []
    for row in rows:
        h.append(
            Quote(
                # Quote.date cannot be null.
                parse_date(row[1]),
                # Keep micro values.
                parse_decimal(row[2]),
                parse_decimal(row[3]),
                parse_decimal(row[4]),
                parse_decimal(row[5]),
                parse_decimal(row[6]),
            )
        )

    h.reverse()
    return h[:days]


@pytest.fixture(scope="session")
def quotes_big(days: int = 1246):
    rows = get_data_from_csv("TooBig")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[1]),
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
            )
        )

    h.reverse()
    return h[:days]


@pytest.fixture(scope="session")
def quotes_other(days: int = 502):
    rows = get_data_from_csv("Compare")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[2]),
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
            )
        )

    h.reverse()
    return h[:days]


# --- Specialized Quote Fixtures -----------------------------------------


@pytest.fixture(scope="session")
def quotes_bitcoin(days: int = 1246):
    rows = get_data_from_csv("Bitcoin")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[1]),
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
            )
        )

    h.reverse()
    return h[:days]


@pytest.fixture(scope="session")
def quotes_intraday(days: int = 1564):
    rows = get_data_from_csv("Intraday")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[1]),
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
            )
        )

    h.reverse()
    return h[:days]


@pytest.fixture(scope="session")
def quotes_mismatch(days: int = 502):
    rows = get_data_from_csv("Mismatch")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[0]),
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
            )
        )

    h.reverse()
    return h[:days]


# --- Extended Data Quote Fixtures ---------------------------------------


@pytest.fixture(scope="session")
def quotes_longest():
    rows = get_data_from_csv("Longest")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[2]),
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
            )
        )

    return h


@pytest.fixture(scope="session")
def quotes_longish(days: int = 5285):
    rows = get_data_from_csv("Longish")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[2]),
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
            )
        )

    h.reverse()
    return h[:days]


# --- Market Data Quote Fixtures ----------------------------------------


@pytest.fixture(scope="session")
def quotes_msft(days: int = 8111):
    rows = get_data_from_csv("MSFT")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[0]),
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
            )
        )

    h.reverse()
    return h[:days]


@pytest.fixture(scope="session")
def quotes_penny():
    rows = get_data_from_csv("Penny")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[1]),
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
            )
        )

    return h


@pytest.fixture(scope="session")
def quotes_spx(days: int = 8111):
    rows = get_data_from_csv("SPX")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[0]),
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
            )
        )

    h.reverse()
    return h[:days]


@pytest.fixture(scope="session")
def quotes_zigzag(days: int = 342):
    rows = get_data_from_csv("ZigZag")

    h = []
    for row in rows:
        h.append(
            Quote(
                parse_date(row[0]),
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
            )
        )

    h.reverse()
    return h[:days]
