"""Identity roundtrip across indicators for DateOf* CSV datasets.

Verifies 1:1 date alignment and exact equality across five diverse indicators.
"""

from datetime import timezone

import pytest

from stock_indicators import indicators
from stock_indicators.indicators.common.quote import Quote


def _norm_key(d):
    """Normalize datetime for mixed naive/aware sorting:
    - Aware: convert to UTC and drop tzinfo
    - Naive: keep as-is
    Return tuple (normalized_dt, is_aware) to keep stable ordering between naive and aware at same instant.
    """
    is_aware = d.tzinfo is not None and d.tzinfo.utcoffset(d) is not None
    base = d.astimezone(timezone.utc).replace(tzinfo=None) if is_aware else d
    return (base, is_aware)


def _load_quotes(csv_name: str):
    from tests.conftest import get_data_from_csv, parse_date

    rows = get_data_from_csv(csv_name)
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
    quotes.reverse()  # ascending dates
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
def test_identity_roundtrip_across_indicators(csv_name):
    quotes = _load_quotes(csv_name)

    # Use five diverse indicators (no condense/remove_warmup here to preserve 1:1)
    sar = indicators.get_parabolic_sar(quotes)
    ht = indicators.get_ht_trendline(quotes)
    ichi = indicators.get_ichimoku(quotes, 9, 26, 52)
    rp = indicators.get_rolling_pivots(quotes, 11, 9)
    # Correlation requires a second series; reuse the same to keep shape
    corr = indicators.get_correlation(quotes, quotes, 20)

    # Sort quotes once for order-agnostic comparison
    quotes_sorted = sorted(quotes, key=lambda q: _norm_key(q.date))

    for results in (sar, ht, ichi, rp, corr):
        # 1:1 lengths
        assert len(results) == len(quotes)
        # Element-wise dates must match exactly (order-agnostic)
        results_sorted = sorted(results, key=lambda r: _norm_key(r.date))
        for i in range(len(quotes_sorted)):
            assert results_sorted[i].date == quotes_sorted[i].date
