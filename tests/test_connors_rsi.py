import pytest
from stock_indicators import indicators

class TestConnorsRSI:
    def test_standard(self, quotes):
        rsi_periods = 3
        streak_periods = 2
        rank_periods = 100
        start_periods = max(rsi_periods, max(streak_periods, rank_periods)) + 2
        
        results = indicators.get_connors_rsi(quotes, rsi_periods, streak_periods, rank_periods)
        
        assert 502 == len(results)
        assert 502 - start_periods + 1 == len(list(
            filter(lambda x: x.connors_rsi is not None, results)))
        
        r = results[501]
        assert 68.8087 == round(float(r.rsi_close), 4)
        assert 67.4899 == round(float(r.rsi_streak), 4)
        assert 88.0000 == round(float(r.percent_rank), 4)
        assert 74.7662 == round(float(r.connors_rsi), 4)
        
        results = indicators.get_connors_rsi(quotes, 14, 20, 10)
        r = results[501]
        assert 42.0773 == round(float(r.rsi_close), 4)
        assert 52.7386 == round(float(r.rsi_streak), 4)
        assert 90.0000 == round(float(r.percent_rank), 4)
        assert 61.6053 == round(float(r.connors_rsi), 4)
        
    def test_bad_data(self, bad_quotes):
        r = indicators.get_connors_rsi(bad_quotes, 4, 3, 25)
        assert 502 == len(r)
        
    def test_removed(self, quotes):
        rsi_periods = 3
        streak_periods = 2
        rank_periods = 100
        
        removed_periods = max(rsi_periods, max(streak_periods, rank_periods)) + 2
        
        results = indicators.get_connors_rsi(quotes, rsi_periods, streak_periods, rank_periods)
        results = results.remove_warmup_periods()
        
        last = results.pop()
        assert 68.8087 == round(float(last.rsi_close), 4)
        assert 67.4899 == round(float(last.rsi_streak), 4)
        assert 88.0000 == round(float(last.percent_rank), 4)
        assert 74.7662 == round(float(last.connors_rsi), 4)
        
    def test_exceptions(self, quotes):
        from System import ArgumentOutOfRangeException
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_connors_rsi(quotes, 1, 2, 100)
        
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_connors_rsi(quotes, 3, 1, 100)
            
        with pytest.raises(ArgumentOutOfRangeException):
            indicators.get_connors_rsi(quotes, 3, 2, 1)
