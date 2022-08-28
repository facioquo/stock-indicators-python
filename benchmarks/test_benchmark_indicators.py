from stock_indicators import indicators
from stock_indicators.indicators.common.enums import PeriodSize

def test_benchmark_adl(benchmark, quotes):
    benchmark(indicators.get_adl, quotes)

def test_benchmark_adx(benchmark, quotes):
    benchmark(indicators.get_adx, quotes)

def test_benchmark_alligator(benchmark, quotes):
    benchmark(indicators.get_alligator, quotes)

def test_benchmark_alma(benchmark, quotes):
    benchmark(indicators.get_alma, quotes)

def test_benchmark_aroon(benchmark, quotes):
    benchmark(indicators.get_aroon, quotes)

def test_benchmark_atr(benchmark, quotes):
    benchmark(indicators.get_atr, quotes)

def test_benchmark_awesome(benchmark, quotes):
    benchmark(indicators.get_awesome, quotes)

def test_benchmark_beta(benchmark, quotes, other_quotes):
    benchmark(indicators.get_beta, quotes, other_quotes, 20)

def test_benchmark_bollinger_bands(benchmark, quotes):
    benchmark(indicators.get_bollinger_bands, quotes)

def test_benchmark_bop(benchmark, quotes):
    benchmark(indicators.get_bop, quotes)

def test_benchmark_cci(benchmark, quotes):
    benchmark(indicators.get_cci, quotes, 20)

def test_benchmark_chaikin_osc(benchmark, quotes):
    benchmark(indicators.get_chaikin_osc, quotes)

def test_benchmark_chandelier(benchmark, quotes):
    benchmark(indicators.get_chandelier, quotes)

def test_benchmark_chop(benchmark, quotes):
    benchmark(indicators.get_chop, quotes)

def test_benchmark_cmf(benchmark, quotes):
    benchmark(indicators.get_cmf, quotes)

def test_benchmark_connors_rsi(benchmark, quotes):
    benchmark(indicators.get_connors_rsi, quotes)

def test_benchmark_correlation(benchmark, quotes, other_quotes):
    benchmark(indicators.get_correlation, quotes, other_quotes, 20)

def test_benchmark_doji(benchmark, quotes):
    benchmark(indicators.get_doji, quotes)

def test_benchmark_donchian(benchmark, quotes):
    benchmark(indicators.get_donchian, quotes)

def test_benchmark_dema(benchmark, quotes):
    benchmark(indicators.get_dema, quotes, 20)

def test_benchmark_dpo(benchmark, quotes):
    benchmark(indicators.get_dpo, quotes, 14)

def test_benchmark_elder_ray(benchmark, quotes):
    benchmark(indicators.get_elder_ray, quotes)

def test_benchmark_ema(benchmark, quotes):
    benchmark(indicators.get_ema, quotes, 20)

def test_benchmark_epma(benchmark, quotes):
    benchmark(indicators.get_epma, quotes, 20)

def test_benchmark_fcb(benchmark, quotes):
    benchmark(indicators.get_fcb, quotes)

def test_benchmark_fisher_transform(benchmark, quotes):
    benchmark(indicators.get_fisher_transform, quotes)

def test_benchmark_force_index(benchmark, quotes):
    benchmark(indicators.get_force_index, quotes, 13)

def test_benchmark_fractal(benchmark, quotes):
    benchmark(indicators.get_fractal, quotes)

def test_benchmark_gator(benchmark, quotes):
    benchmark(indicators.get_gator, quotes)

def test_benchmark_heikin_ashi(benchmark, quotes):
    benchmark(indicators.get_heikin_ashi, quotes)

def test_benchmark_hma(benchmark, quotes):
    benchmark(indicators.get_hma, quotes, 20)

def test_benchmark_ht_trendline(benchmark, quotes):
    benchmark(indicators.get_ht_trendline, quotes)

def test_benchmark_hurst(benchmark, quotes):
    benchmark(indicators.get_hurst, quotes)

def test_benchmark_hurst_longlong(benchmark, longish_quotes):
    benchmark(indicators.get_hurst, longish_quotes+longish_quotes)

def test_benchmark_ichimoku(benchmark, quotes):
    benchmark(indicators.get_ichimoku, quotes)

def test_benchmark_kama(benchmark, quotes):
    benchmark(indicators.get_kama, quotes)

def test_benchmark_keltner(benchmark, quotes):
    benchmark(indicators.get_keltner, quotes)

def test_benchmark_kvo(benchmark, quotes):
    benchmark(indicators.get_kvo, quotes)

def test_benchmark_ma_envelopes(benchmark, quotes):
    benchmark(indicators.get_ma_envelopes, quotes, 10)

def test_benchmark_macd(benchmark, quotes):
    benchmark(indicators.get_macd, quotes)

def test_benchmark_mama(benchmark, quotes):
    benchmark(indicators.get_mama, quotes)

def test_benchmark_marubozu(benchmark, quotes):
    benchmark(indicators.get_marubozu, quotes)

def test_benchmark_mfi(benchmark, quotes):
    benchmark(indicators.get_mfi, quotes)

def test_benchmark_obv(benchmark, quotes):
    benchmark(indicators.get_obv, quotes)

def test_benchmark_parabolic_sar(benchmark, quotes):
    benchmark(indicators.get_parabolic_sar, quotes)

def test_benchmark_pivot_points(benchmark, quotes):
    benchmark(indicators.get_pivot_points, quotes, PeriodSize.MONTH)

def test_benchmark_pivots(benchmark, quotes):
    benchmark(indicators.get_pivots, quotes)

def test_benchmark_pmo(benchmark, quotes):
    benchmark(indicators.get_pmo, quotes)

def test_benchmark_prs(benchmark, quotes):
    benchmark(indicators.get_prs, quotes, quotes)

def test_benchmark_pvo(benchmark, quotes):
    benchmark(indicators.get_pvo, quotes)

def test_benchmark_renko(benchmark, quotes):
    benchmark(indicators.get_renko, quotes, 2.5)

def test_benchmark_roc(benchmark, quotes):
    benchmark(indicators.get_roc, quotes, 20)

def test_benchmark_rolling_pivots(benchmark, quotes):
    benchmark(indicators.get_rolling_pivots, quotes, 11, 9)

def test_benchmark_rsi(benchmark, quotes):
    benchmark(indicators.get_rsi, quotes)

def test_benchmark_slope(benchmark, quotes):
    benchmark(indicators.get_slope, quotes, 20)

def test_benchmark_sma_extended(benchmark, quotes):
    benchmark(indicators.get_sma_extended, quotes, 20)

def test_benchmark_sma(benchmark, quotes):
    benchmark(indicators.get_sma, quotes, 20)

def test_benchmark_smi(benchmark, quotes):
    benchmark(indicators.get_smi, quotes, 14, 20, 5, 3)

def test_benchmark_smma(benchmark, quotes):
    benchmark(indicators.get_smma, quotes, 20)

def test_benchmark_starc_bands(benchmark, quotes):
    benchmark(indicators.get_starc_bands, quotes)

def test_benchmark_stc(benchmark, quotes):
    benchmark(indicators.get_stc, quotes)

def test_benchmark_stdev_channels(benchmark, quotes):
    benchmark(indicators.get_stdev_channels, quotes, 20, 2)

def test_benchmark_stdev(benchmark, quotes):
    benchmark(indicators.get_stdev, quotes, 10)

def test_benchmark_stoch_rsi(benchmark, quotes):
    benchmark(indicators.get_stoch_rsi, quotes, 14, 14, 3, 1)

def test_benchmark_stoch(benchmark, quotes):
    benchmark(indicators.get_stoch, quotes)

def test_benchmark_super_trend(benchmark, quotes):
    benchmark(indicators.get_super_trend, quotes)

def test_benchmark_t3(benchmark, quotes):
    benchmark(indicators.get_t3, quotes)

def test_benchmark_triple_ema(benchmark, quotes):
    benchmark(indicators.get_tema, quotes, 20)

def test_benchmark_trix(benchmark, quotes):
    benchmark(indicators.get_trix, quotes, 20, 5)

def test_benchmark_tsi(benchmark, quotes):
    benchmark(indicators.get_tsi, quotes)

def test_benchmark_ulcer_index(benchmark, quotes):
    benchmark(indicators.get_ulcer_index, quotes)

def test_benchmark_ultimate(benchmark, quotes):
    benchmark(indicators.get_ultimate, quotes)

def test_benchmark_volatility_stop(benchmark, quotes):
    benchmark(indicators.get_volatility_stop, quotes)

def test_benchmark_vortex(benchmark, quotes):
    benchmark(indicators.get_vortex, quotes, 14)

def test_benchmark_vwap(benchmark, quotes):
    benchmark(indicators.get_vwap, quotes)

def test_benchmark_vwma(benchmark, quotes):
    benchmark(indicators.get_vwma, quotes, 10)

def test_benchmark_williams_r(benchmark, quotes):
    benchmark(indicators.get_williams_r, quotes)

def test_benchmark_wma(benchmark, quotes):
    benchmark(indicators.get_wma, quotes, 20)

def test_benchmark_zig_zag(benchmark, quotes):
    benchmark(indicators.get_zig_zag, quotes)
