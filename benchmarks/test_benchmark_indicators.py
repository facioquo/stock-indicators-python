from stock_indicators import indicators

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

def test_benchmark_chop(benchmark, quotes):
    benchmark(indicators.get_chop, quotes)
    
def test_benchmark_cmf(benchmark, quotes):
    benchmark(indicators.get_cmf, quotes)
    
def test_benchmark_connors_rsi(benchmark, quotes):
    benchmark(indicators.get_connors_rsi, quotes)
    
def test_benchmark_correlation(benchmark, quotes, other_quotes):
    benchmark(indicators.get_correlation, quotes, other_quotes, 20)
    
def test_benchmark_dpo(benchmark, quotes):
    benchmark(indicators.get_dpo, quotes, 14)
    
def test_benchmark_epma(benchmark, quotes):
    benchmark(indicators.get_epma, quotes, 20)
    
def test_benchmark_fcb(benchmark, quotes):
    benchmark(indicators.get_fcb, quotes)
    
def test_chandelier(benchmark, quotes):
    benchmark(indicators.get_chandelier, quotes)

def test_donchian(benchmark, quotes):
    benchmark(indicators.get_donchian, quotes)
    
def test_double_ema(benchmark, quotes):
    benchmark(indicators.get_double_ema, quotes, 20)

def test_elder_ray(benchmark, quotes):
    benchmark(indicators.get_elder_ray, quotes)

def test_benchmark_ema(benchmark, quotes):
    benchmark(indicators.get_ema, quotes, 20)

def test_benchmark_fractal(benchmark, quotes):
    benchmark(indicators.get_fractal, quotes)

def test_heikin_ashi(benchmark, quotes):
    benchmark(indicators.get_heikin_ashi, quotes)

def test_ichimoku(benchmark, quotes):
    benchmark(indicators.get_ichimoku, quotes)

def test_benchmark_macd(benchmark, quotes):
    benchmark(indicators.get_macd, quotes)

def test_parabolic_sar(benchmark, quotes):
    benchmark(indicators.get_parabolic_sar, quotes)

def test_roc(benchmark, quotes):
    benchmark(indicators.get_roc, quotes, 20)

def test_benchmark_rsi(benchmark, quotes):
    benchmark(indicators.get_rsi, quotes)
    
def test_slope(benchmark, quotes):
    benchmark(indicators.get_slope, quotes, 20)

def test_benchmark_sma_extended(benchmark, quotes):
    benchmark(indicators.get_sma_extended, quotes, 20)

def test_benchmark_sma(benchmark, quotes):
    benchmark(indicators.get_sma, quotes, 20)
    
def test_benchmark_stdev_channels(benchmark, quotes):
    benchmark(indicators.get_stdev_channels, quotes, 20, 2)

def test_benchmark_stoch_rsi(benchmark, quotes):
    benchmark(indicators.get_stoch_rsi, quotes, 14, 14, 3, 1)

def test_benchmark_stoch(benchmark, quotes):
    benchmark(indicators.get_stoch, quotes)

def test_benchmark_super_trend(benchmark, quotes):
    benchmark(indicators.get_super_trend, quotes)

def test_triple_ema(benchmark, quotes):
    benchmark(indicators.get_triple_ema, quotes, 20)

def test_trix(benchmark, quotes):
    benchmark(indicators.get_trix, quotes, 20, 5)
