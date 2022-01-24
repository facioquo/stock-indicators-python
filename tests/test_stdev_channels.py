import pytest
from stock_indicators import indicators

class TestStdevChannels:
    def test_standard(self, quotes):
        results = indicators.get_stdev_channels(quotes, 20, 2)
        
        assert 502 == len(results)
        assert 500 == len(list(filter(lambda x: x.center_line is not None, results)))
        assert 500 == len(list(filter(lambda x: x.upper_channel is not None, results)))
        assert 500 == len(list(filter(lambda x: x.lower_channel is not None, results)))
        
        r = results[1]
        assert r.center_line is None
        assert r.upper_channel is None
        assert r.lower_channel is None
        assert r.break_point is False
        
        r = results[2]
        assert 213.7993 == round(float(r.center_line), 4)
        assert 215.7098 == round(float(r.upper_channel), 4)
        assert 211.8888 == round(float(r.lower_channel), 4)
        assert r.break_point is True
        
        r = results[141]
        assert 236.1744 == round(float(r.center_line), 4)
        assert 240.4784 == round(float(r.upper_channel), 4)
        assert 231.8704 == round(float(r.lower_channel), 4)
        assert r.break_point is False
        
        r = results[142]
        assert 236.3269 == round(float(r.center_line), 4)
        assert 239.5585 == round(float(r.upper_channel), 4)
        assert 233.0953 == round(float(r.lower_channel), 4)
        assert r.break_point is True
        
        r = results[249]
        assert 259.6044 == round(float(r.center_line), 4)
        assert 267.5754 == round(float(r.upper_channel), 4)
        assert 251.6333 == round(float(r.lower_channel), 4)
        assert r.break_point is False
        
        r = results[482]
        assert 267.9069 == round(float(r.center_line), 4)
        assert 289.7473 == round(float(r.upper_channel), 4)
        assert 246.0664 == round(float(r.lower_channel), 4)
        assert r.break_point is True
        
        r = results[501]
        assert 235.8131 == round(float(r.center_line), 4)
        assert 257.6536 == round(float(r.upper_channel), 4)
        assert 213.9727 == round(float(r.lower_channel), 4)
        assert r.break_point is False
        
    def test_full_history(self, quotes):
        results = indicators.get_stdev_channels(quotes, None, 2)
        
        assert 502 == len(results)
        assert 502 == len(list(filter(lambda x: x.center_line is not None, results)))
        assert 502 == len(list(filter(lambda x: x.upper_channel is not None, results)))
        assert 502 == len(list(filter(lambda x: x.lower_channel is not None, results)))
        assert 501 == len(list(filter(lambda x: x.break_point is False, results)))
        
        r = results[0]
        assert 219.2605 == round(float(r.center_line), 4)
        assert 258.7104 == round(float(r.upper_channel), 4)
        assert 179.8105 == round(float(r.lower_channel), 4)
        assert r.break_point is True
        
        r = results[249]
        assert 249.3814 == round(float(r.center_line), 4)
        assert 288.8314 == round(float(r.upper_channel), 4)
        assert 209.9315 == round(float(r.lower_channel), 4)
        
        r = results[501]
        assert 279.8653 == round(float(r.center_line), 4)
        assert 319.3152 == round(float(r.upper_channel), 4)
        assert 240.4153 == round(float(r.lower_channel), 4)
    
    def test_bad_data(self, bad_quotes):
        r = indicators.get_stdev_channels(bad_quotes)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        results = indicators.get_stdev_channels(quotes, 20, 2).remove_warmup_periods()
        
        assert 500 == len(results)
        
        last = results.pop()
        assert 235.8131 == round(float(last.center_line), 4)
        assert 257.6536 == round(float(last.upper_channel), 4)
        assert 213.9727 == round(float(last.lower_channel), 4)
        assert last.break_point is False
    
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stdev_channels(quotes, 0)

        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_stdev_channels(quotes, 20,0)
