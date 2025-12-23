from datetime import datetime, timezone
from decimal import Decimal

from stock_indicators.indicators.common.quote import Quote


def test_quote_constructor_retains_timezone():
    dt = datetime.fromisoformat("2000-03-26T23:00:00+00:00")
    q = Quote(
        date=dt,
        open=Decimal("23"),
        high=Decimal("26"),
        low=Decimal("20"),
        close=Decimal("25"),
        volume=Decimal("323"),
    )

    assert str(q.date.tzinfo) == "UTC"
    assert str(q.date.time()) == "23:00:00"


def test_quote_constructor_handles_various_date_formats():
    dt1 = datetime.fromisoformat("2000-03-26T23:00:00+00:00")
    dt2 = datetime.strptime("2000-03-26 23:00:00", "%Y-%m-%d %H:%M:%S")
    dt3 = datetime.strptime("2000-03-26", "%Y-%m-%d")

    q1 = Quote(
        date=dt1,
        open=Decimal("23"),
        high=Decimal("26"),
        low=Decimal("20"),
        close=Decimal("25"),
        volume=Decimal("323"),
    )

    q2 = Quote(
        date=dt2,
        open=Decimal("23"),
        high=Decimal("26"),
        low=Decimal("20"),
        close=Decimal("25"),
        volume=Decimal("323"),
    )

    q3 = Quote(
        date=dt3,
        open=Decimal("23"),
        high=Decimal("26"),
        low=Decimal("20"),
        close=Decimal("25"),
        volume=Decimal("323"),
    )

    assert str(q1.date.tzinfo) == "UTC"
    assert str(q1.date.time()) == "23:00:00"

    assert str(q2.date.tzinfo) == "None"
    assert str(q2.date.time()) == "23:00:00"

    assert str(q3.date.tzinfo) == "None"
    assert str(q3.date.time()) == "00:00:00"


def test_quote_constructor_handles_system_local_timezone():
    # Build a tz-aware datetime in the system local zone and ensure it preserves the instant
    local_tz = datetime.now().astimezone().tzinfo
    dt = datetime(2025, 8, 22, 14, 30, 0, tzinfo=local_tz)

    q = Quote(
        date=dt,
        open=Decimal("23"),
        high=Decimal("26"),
        low=Decimal("20"),
        close=Decimal("25"),
        volume=Decimal("323"),
    )

    # tz-aware should normalize to UTC but represent the same instant
    d = q.date
    assert str(d.tzinfo) == "UTC"
    assert d.replace(microsecond=0) == dt.astimezone(timezone.utc).replace(
        microsecond=0
    )
