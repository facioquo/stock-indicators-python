from datetime import datetime, timezone

import pytest

from stock_indicators._cstypes import DateTime as CsDateTime
from stock_indicators._cstypes import to_pydatetime


def test_to_pydatetime_sets_utc_for_tzaware():
    # Start with an offset-aware datetime and ensure roundtrip yields UTC tz
    dt = datetime.fromisoformat("2022-06-02T10:29:00-04:00")
    expected_utc = dt.astimezone(timezone.utc)

    cs_dt = CsDateTime(dt)
    py_dt = to_pydatetime(cs_dt)

    # tz-aware should come back as UTC
    assert str(py_dt.tzinfo) == "UTC"
    # Time should reflect conversion to UTC
    assert py_dt.replace(microsecond=0) == expected_utc.replace(microsecond=0)


def test_to_pydatetime_keeps_naive_naive():
    # Naive input should remain naive and preserve second-level components
    dt = datetime.fromisoformat("2023-01-02T03:04:05")  # no microseconds

    cs_dt = CsDateTime(dt)
    py_dt = to_pydatetime(cs_dt)

    assert py_dt.tzinfo is None
    assert (
        py_dt.year,
        py_dt.month,
        py_dt.day,
        py_dt.hour,
        py_dt.minute,
        py_dt.second,
    ) == (
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second,
    )


def test_csdatetime_rejects_non_datetime_input():
    with pytest.raises(TypeError):
        CsDateTime("2020-01-01")  # type: ignore[arg-type]


def test_to_pydatetime_handles_system_local_timezone_roundtrip():
    # Create a tz-aware datetime using the system's local timezone
    local_tz = datetime.now().astimezone().tzinfo
    dt_local = datetime(2025, 8, 22, 14, 30, 0, tzinfo=local_tz)

    cs_dt = CsDateTime(dt_local)
    py_dt = to_pydatetime(cs_dt)

    # Interop always returns tz-aware as UTC; ensure the instant is preserved
    assert str(py_dt.tzinfo) == "UTC"
    assert py_dt.replace(microsecond=0) == dt_local.astimezone(timezone.utc).replace(
        microsecond=0
    )
