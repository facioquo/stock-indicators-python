"""SMA roundtrip date alignment for DateOf* CSV datasets.

Ensures 1:1 date alignment and exact equality between input Quotes and
SMA results across all date/time variants, order-agnostic.
"""

from datetime import datetime, timezone

import pytest

from stock_indicators import indicators
from stock_indicators.indicators.common.quote import Quote


def _norm_key(d: datetime):
    """Normalize datetime for mixed naive/aware sorting:
    - Aware: convert to UTC and drop tzinfo
    - Naive: keep as-is
    Return tuple (normalized_dt, is_aware) to keep stable ordering
    between naive and aware at same instant.
    """
    is_aware = d.tzinfo is not None and d.tzinfo.utcoffset(d) is not None
    base = d.astimezone(timezone.utc).replace(tzinfo=None) if is_aware else d
    return (base, is_aware)


def _load_quotes_from_csv(name: str):
    # Reuse test helper functions for consistent parsing
    from tests.conftest import get_data_from_csv, parse_date

    rows = get_data_from_csv(name)
    quotes = []
    for row in rows:
        quotes.append(
            Quote(
                date=parse_date(row[1]),
                open=row[2],
                high=row[3],
                low=row[4],
                close=row[5],
                volume=row[6],
            )
        )

    quotes.reverse()  # match standard fixture orientation (ascending by date)
    return quotes


@pytest.mark.parametrize(
    "csv_name",
    [
        "DateOfUTCDate",
        "DateOfUTCZDate",
        "DateOfUTCFracZDate",
        "DateOfOffsetDate",
        "DateOfOffsetFracDate",
        "DateOfOffsetBasicDate",
        "DateOfNaiveMinDate",
        "DateOfNaiveSecDate",
        "DateOfNaiveMsDate",
        "DateOfNaiveBasicDate",
        "DateOfDateOnly",
        "DateOfDateOnlyBasic",
        "DateOfDateOnlyDMY",
        "DateOfDateOnlyUS",
        "DateOfRFC1123Date",
        "DateOfIANAZoneDate",
    ],
)
def test_sma_roundtrip_dates_from_short_csv(csv_name):
    src = _load_quotes_from_csv(csv_name)

    # Sanity
    assert len(src) > 20

    results = indicators.get_sma(src, 10)

    # 1:1 alignment and exact date equality for each element (order-agnostic)
    assert len(results) == len(src)

    # Sort both by date for order-agnostic comparison
    src_sorted = sorted(src, key=lambda q: _norm_key(q.date))
    results_sorted = sorted(results, key=lambda r: _norm_key(r.date))

    for i in range(len(src_sorted)):
        assert results_sorted[i].date == src_sorted[i].date
