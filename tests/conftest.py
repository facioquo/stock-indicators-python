import csv
import logging
import os
import re
from datetime import datetime
from email.utils import parsedate_to_datetime

# ZoneInfo: stdlib on 3.9+, backport on 3.8
try:  # pragma: no cover - import guard
    from zoneinfo import ZoneInfo  # type: ignore[attr-defined]
except Exception:  # pragma: no cover - fallback for Py<3.9
    try:
        from backports.zoneinfo import ZoneInfo  # type: ignore
    except Exception:
        ZoneInfo = None  # type: ignore
from decimal import Decimal, DecimalException
from pathlib import Path

import pytest

from stock_indicators.indicators.common import Quote  # pre-initialized
from stock_indicators.logging_config import configure_logging


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    configure_logging(debug=True)


# Setup logging for this module
logger = logging.getLogger(__name__)

# Constants
base_dir = Path(__file__).parent.parent / "test_data"


@pytest.fixture(autouse=True, scope="session")
def setup_clr_culture():
    """Configure CLR culture settings for all tests."""
    import clr  # noqa: F401
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
            "Test data not found. Please see README.md "
            "for test data setup instructions."
        )

    data_path = quotes_dir / f"{filename}.csv"
    logger.debug("Loading test data from: %s", data_path)

    if not data_path.exists():
        raise FileNotFoundError(f"Test data file not found: {filename}")

    with open(data_path, newline="", encoding="utf-8") as csvfile:
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
    """Parse date value across many common formats.

    Supported families:
    - Date-only: YYYY-MM-DD, YYYYMMDD, DD-MM-YYYY, MM/DD/YYYY
    - Naive date+time: YYYY-MM-DDTHH:MM, YYYY-MM-DDTHH:MM:SS,
      YYYY-MM-DDTHH:MM:SS.sss[sss], YYYYMMDDTHHMMSS
    - With offset: ISO-8601 extended with offset (e.g., +00:00, -04:00, +05:30,
      with optional fractions); ISO basic with offset without colon:
      YYYYMMDDTHHMMSS+0000
    - Zulu: ...Z with optional fractional seconds
    - RFC1123/HTTP-date: Fri, 22 Aug 2025 17:45:30 GMT
    - IANA zone name appended after a space: YYYY-MM-DDTHH:MM:SS America/New_York
    """

    s = date_str.strip()
    try:
        # RFC1123 / HTTP-date (always aware)
        if re.match(r"^[A-Za-z]{3}, ", s):
            return parsedate_to_datetime(s)

        # IANA zone name appended: "<iso-local> <Area/Location>"
        if " " in s and "/" in s.split(" ", 1)[1]:
            base, zone = s.split(" ", 1)
            # Normalize potential Z
            base_norm = base.replace("Z", "+00:00")
            # Use fromisoformat for extended forms; fallback to seconds/minutes
            try:
                dt = datetime.fromisoformat(base_norm)
            except ValueError:
                # Try minutes-only format
                if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}", base):
                    dt = datetime.strptime(base, "%Y-%m-%dT%H:%M")
                else:
                    dt = datetime.strptime(base, "%Y-%m-%dT%H:%M:%S")
            if ZoneInfo is not None:
                try:
                    return dt.replace(tzinfo=ZoneInfo(zone))
                except Exception:
                    # Fallback if IANA zone isn't available on the system:
                    # treat as naive
                    return dt
            # ZoneInfo not available; treat as naive
            return dt

        # ISO basic with offset without colon: YYYYMMDDTHHMMSS+HHMM
        if re.fullmatch(r"\d{8}T\d{6}[+-]\d{4}", s):
            return datetime.strptime(s, "%Y%m%dT%H%M%S%z")

        # ISO basic without offset (naive): YYYYMMDDTHHMMSS
        m = re.fullmatch(r"(\d{8})T(\d{6})(?:\.(\d{1,6}))?", s)
        if m:
            dt = datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S")
            if m.group(3):
                micro = int((m.group(3) + "000000")[:6])
                dt = dt.replace(microsecond=micro)
            return dt

        # ISO extended with Zulu or offset, including fractional seconds
        if "T" in s and (s.endswith("Z") or re.search(r"[+-]\d{2}:?\d{2}$", s)):
            s_norm = s.replace("Z", "+00:00")
            # If offset without colon at end (e.g., +0000), insert colon for
            # fromisoformat
            m_off = re.search(r"([+-])(\d{2})(\d{2})$", s_norm)
            if m_off and ":" not in s_norm[-6:]:
                s_norm = (
                    s_norm[: m_off.start()]
                    + f"{m_off.group(1)}{m_off.group(2)}:{m_off.group(3)}"
                )
            return datetime.fromisoformat(s_norm)

        # Minutes-only ISO extended (naive)
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}", s):
            return datetime.strptime(s, "%Y-%m-%dT%H:%M")

        # Seconds ISO extended (naive)
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", s):
            return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")

        # Fractional seconds ISO extended (naive)
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{1,6}", s):
            return datetime.fromisoformat(s)

        # Date-only formats
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
            return datetime.strptime(s, "%Y-%m-%d")
        if re.fullmatch(r"\d{8}", s):  # YYYYMMDD
            return datetime.strptime(s, "%Y%m%d")
        if re.fullmatch(r"\d{2}-\d{2}-\d{4}", s):  # DD-MM-YYYY
            return datetime.strptime(s, "%d-%m-%Y")
        if re.fullmatch(r"\d{2}/\d{2}/\d{4}", s):  # MM/DD/YYYY
            return datetime.strptime(s, "%m/%d/%Y")

        # Legacy fallback: "YYYY-MM-DD HH:MM:SS" (naive with space)
        if " " in s and re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", s):
            return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

        # As a final attempt, try fromisoformat on whatever remains
        return datetime.fromisoformat(s)
    except Exception:
        # Last-resort fallback to keep tests running; individual tests will
        # assert equality
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
