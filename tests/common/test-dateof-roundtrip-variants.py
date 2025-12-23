import pytest

from stock_indicators import indicators
from stock_indicators.indicators.common.quote import Quote


def _mk_utc():
    from datetime import datetime, timezone

    # Naive date-only -> UTC midnight
    return [
        Quote(datetime(2020, 1, 1, tzinfo=timezone.utc), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 2, tzinfo=timezone.utc), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 3, tzinfo=timezone.utc), 1, 1, 1, 1, 1),
    ]


def _mk_offset():
    from datetime import datetime, timedelta, timezone

    tz = timezone(timedelta(hours=-4))
    return [
        Quote(datetime(2020, 1, 1, tzinfo=tz), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 2, tzinfo=tz), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 3, tzinfo=tz), 1, 1, 1, 1, 1),
    ]


def _mk_naive_time():
    from datetime import datetime

    return [
        Quote(datetime(2020, 1, 1, 12, 0, 0), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 2, 12, 0, 0), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 3, 12, 0, 0), 1, 1, 1, 1, 1),
    ]


def _mk_date_only():
    from datetime import datetime

    return [
        Quote(datetime(2020, 1, 1), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 2), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 3), 1, 1, 1, 1, 1),
    ]


@pytest.mark.parametrize(
    ("variant", "maker"),
    [
        ("utc", _mk_utc),
        ("offset", _mk_offset),
        ("naive_time", _mk_naive_time),
        ("date_only", _mk_date_only),
    ],
)
def test_sma_roundtrip_dates_variants(variant, maker):
    quotes = maker()
    assert variant
    results = indicators.get_sma(quotes, 2)

    assert len(results) == len(quotes)
    for i in range(len(quotes)):
        assert results[i].date == quotes[i].date


def test_sma_roundtrip_dates_mixed_variants():
    from datetime import datetime, timezone

    # Mixed: naive date-only, tz-aware, naive time
    quotes = [
        Quote(datetime(2020, 1, 1), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 2, tzinfo=timezone.utc), 1, 1, 1, 1, 1),
        Quote(datetime(2020, 1, 3, 12, 0, 0), 1, 1, 1, 1, 1),
    ]
    results = indicators.get_sma(quotes, 2)

    assert len(results) == len(quotes)
    for i in range(len(quotes)):
        assert results[i].date == quotes[i].date
