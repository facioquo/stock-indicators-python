import pytest

from stock_indicators import indicators
from stock_indicators.indicators.common.enums import EndType
from tests.utiltest import load_quotes_from_json


class TestZigZag:
    def test_standard_close(self, quotes):
        results = indicators.get_zig_zag(quotes, EndType.CLOSE, 3)

        assert 502 == len(results)
        assert 234 == len(list(filter(lambda x: x.zig_zag is not None, results)))
        assert 234 == len(list(filter(lambda x: x.retrace_high is not None, results)))
        assert 221 == len(list(filter(lambda x: x.retrace_low is not None, results)))
        assert 14 == len(list(filter(lambda x: x.point_type is not None, results)))

        r = results[249]
        assert r.zig_zag is None
        assert r.retrace_high is None
        assert r.retrace_low is None
        assert r.point_type is None

        r = results[277]
        assert 248.13 == float(round(r.zig_zag, 2))
        assert 272.248 == float(round(r.retrace_high, 3))
        assert 248.13 == float(round(r.retrace_low, 2))
        assert "L" == r.point_type

        r = results[483]
        assert 272.52 == float(round(r.zig_zag, 2))
        assert 272.52 == float(round(r.retrace_high, 2))
        assert 248.799 == float(round(r.retrace_low, 3))
        assert "H" == r.point_type

        r = results[439]
        assert 276.0133 == float(round(r.zig_zag, 4))
        assert 280.9158 == float(round(r.retrace_high, 4))
        assert 264.5769 == float(round(r.retrace_low, 4))
        assert r.point_type is None

        r = results[500]
        assert 241.4575 == float(round(r.zig_zag, 4))
        assert 246.7933 == float(round(r.retrace_high, 4))
        assert r.retrace_low is None
        assert r.point_type is None

        r = results[501]
        assert 245.28 == float(round(r.zig_zag, 2))
        assert 245.28 == float(round(r.retrace_high, 2))
        assert r.retrace_low is None
        assert r.point_type is None

    def test_standard_high_low(self, quotes):
        results = indicators.get_zig_zag(quotes, EndType.HIGH_LOW, 3)

        assert 502 == len(results)
        assert 463 == len(list(filter(lambda x: x.zig_zag is not None, results)))
        assert 463 == len(list(filter(lambda x: x.retrace_high is not None, results)))
        assert 442 == len(list(filter(lambda x: x.retrace_low is not None, results)))
        assert 30 == len(list(filter(lambda x: x.point_type is not None, results)))

        r = results[38]
        assert r.zig_zag is None
        assert r.retrace_high is None
        assert r.retrace_low is None
        assert r.point_type is None

        r = results[277]
        assert 252.9550 == float(round(r.zig_zag, 4))
        assert 262.8054 == float(round(r.retrace_high, 4))
        assert 245.4467 == float(round(r.retrace_low, 4))
        assert r.point_type is None

        r = results[316]
        assert 249.48 == float(round(r.zig_zag, 2))
        assert 258.34 == float(round(r.retrace_high, 2))
        assert 249.48 == float(round(r.retrace_low, 2))
        assert "L" == r.point_type

        r = results[456]
        assert 261.3325 == float(round(r.zig_zag, 4))
        assert 274.3419 == float(round(r.retrace_high, 4))
        assert 256.1050 == float(round(r.retrace_low, 4))
        assert r.point_type is None

        r = results[500]
        assert 240.1667 == float(round(r.zig_zag, 4))
        assert 246.95083 == float(round(r.retrace_high, 5))
        assert r.retrace_low is None
        assert r.point_type is None

        r = results[501]
        assert 245.54 == float(round(r.zig_zag, 2))
        assert 245.54 == float(round(r.retrace_high, 2))
        assert r.retrace_low is None
        assert r.point_type is None

    def test_no_entry(self):
        quotes = load_quotes_from_json("../test_data/zig_zag/data.ethusdt.json")
        results = indicators.get_zig_zag(quotes, EndType.CLOSE, 5)
        assert 0 == len(list(filter(lambda x: x.point_type is not None, results)))

    def test_issue_632(self):
        quotes = load_quotes_from_json("../test_data/zig_zag/data.issue632.json")
        results = indicators.get_zig_zag(quotes, EndType.CLOSE, 5)
        assert 17 == len(results)

    def test_schrodinger_scenario(self):
        quotes = load_quotes_from_json("../test_data/zig_zag/data.schrodinger.json")
        quotes.sort(key=lambda x: x.date)

        results = indicators.get_zig_zag(quotes, EndType.CLOSE, 0.25)
        assert 342 == len(results)

        results = indicators.get_zig_zag(quotes, EndType.HIGH_LOW, 3)
        assert 342 == len(results)

    def test_quotes_no(self, quotes):
        r = indicators.get_zig_zag([])
        assert 0 == len(r)

        r = indicators.get_zig_zag(quotes[:1])
        assert 1 == len(r)

    def test_bad_data(self, quotes_bad):
        r = indicators.get_zig_zag(quotes_bad, EndType.CLOSE)
        assert 502 == len(r)

        r = indicators.get_zig_zag(quotes_bad, EndType.HIGH_LOW)
        assert 502 == len(r)

    def test_condense(self, quotes):
        results = indicators.get_zig_zag(quotes, EndType.CLOSE, 3).condense()

        assert 14 == len(results)

        last = results.pop()
        assert 229.99 == float(round(last.zig_zag, 2))
        assert 251.33 == float(round(last.retrace_high, 2))
        assert 229.99 == float(round(last.retrace_low, 2))
        assert "L" == last.point_type

    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_zig_zag(quotes, EndType.CLOSE, 0)
