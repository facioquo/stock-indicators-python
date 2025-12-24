from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from stock_indicators import indicators
from stock_indicators.indicators.common.quote import Quote


def _norm_key(d: datetime):
    """Normalize datetime for mixed naive/aware sorting:
    - Aware: convert to UTC and drop tzinfo
    - Naive: keep as-is
    Return tuple (normalized_dt, is_aware) to keep stable ordering between naive and aware at same instant.
    """
    is_aware = d.tzinfo is not None and d.tzinfo.utcoffset(d) is not None
    base = d.astimezone(timezone.utc).replace(tzinfo=None) if is_aware else d
    return (base, is_aware)


def _clone_with_date(quotes, transform):
    # Rebuild Quotes with transformed dates while preserving OHLCV
    out = []
    for q in quotes:
        d = q.date
        nd = transform(d)
        out.append(
            Quote(
                date=nd,
                open=Decimal(q.open),
                high=Decimal(q.high),
                low=Decimal(q.low),
                close=Decimal(q.close),
                volume=Decimal(q.volume),
            )
        )
    return out


def _mk_utc(d: datetime) -> datetime:
    # Force tz-aware UTC at same Y-M-D h:m:s
    return datetime(
        d.year, d.month, d.day, d.hour, d.minute, d.second, tzinfo=timezone.utc
    )


def _mk_offset(d: datetime) -> datetime:
    # Create an offset-aware time (e.g., -04:00); library normalizes to UTC internally
    tz = timezone(timedelta(hours=-4))
    return datetime(d.year, d.month, d.day, d.hour, d.minute, d.second, tzinfo=tz)


def _mk_naive_time(d: datetime) -> datetime:
    # Keep naive but add a non-midnight time component
    return datetime(d.year, d.month, d.day, 12, 34, 56)


def _mk_date_only(d: datetime) -> datetime:
    # Naive date-only (00:00:00)
    return datetime(d.year, d.month, d.day)


@pytest.mark.parametrize(
    ("variant", "maker"),
    [
        ("utc", _mk_utc),
        ("offset", _mk_offset),
        ("naive_time", _mk_naive_time),
        ("date_only", _mk_date_only),
    ],
)
def test_sma_roundtrip_dates_variants(quotes, variant, maker):
    # Use a small subset to keep tests fast but ensure period coverage
    base = list(quotes)[:40]
    converted = _clone_with_date(base, maker)
    # touch variant to avoid unused param warnings in linters
    assert variant in ("utc", "offset", "naive_time", "date_only")

    results = indicators.get_sma(converted, 10)

    # 1:1 alignment and exact date equality for each element (order-agnostic)
    assert len(results) == len(converted)

    # Library returns results sorted by date ascending, so sort inputs the same way
    converted_sorted = sorted(converted, key=lambda q: _norm_key(q.date))
    results_sorted = sorted(results, key=lambda r: _norm_key(r.date))

    for i in range(len(converted_sorted)):
        assert results_sorted[i].date == converted_sorted[i].date


def test_sma_roundtrip_dates_mixed_variants(quotes):
    base = list(quotes)[:48]  # multiple of 4 for even cycling
    makers = (_mk_utc, _mk_offset, _mk_naive_time, _mk_date_only)

    def pick(i: int):
        return makers[i % 4]

    mixed = [
        Quote(
            date=pick(i)(q.date),
            open=Decimal(q.open),
            high=Decimal(q.high),
            low=Decimal(q.low),
            close=Decimal(q.close),
            volume=Decimal(q.volume),
        )
        for i, q in enumerate(base)
    ]

    results = indicators.get_sma(mixed, 10)

    assert len(results) == len(mixed)

    # Sort both by date for order-agnostic comparison
    mixed_sorted = sorted(mixed, key=lambda q: _norm_key(q.date))
    results_sorted = sorted(results, key=lambda r: _norm_key(r.date))

    for i in range(len(mixed_sorted)):
        # After normalization, indicator result dates must equal Quote dates
        assert results_sorted[i].date == mixed_sorted[i].date
