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

def test_benchmark_ema(benchmark, quotes):
    benchmark(indicators.get_ema, quotes, 20)

def test_benchmark_fractal(benchmark, quotes):
    benchmark(indicators.get_fractal, quotes)

def test_benchmark_macd(benchmark, quotes):
    benchmark(indicators.get_macd, quotes)

def test_benchmark_rsi(benchmark, quotes):
    benchmark(indicators.get_rsi, quotes)

def test_benchmark_sma_extended(benchmark, quotes):
    benchmark(indicators.get_sma_extended, quotes, 20)

def test_benchmark_sma(benchmark, quotes):
    benchmark(indicators.get_sma, quotes, 20)

def test_benchmark_stoch_rsi(benchmark, quotes):
    benchmark(indicators.get_stoch_rsi, quotes, 14, 14, 3, 1)

def test_benchmark_stoch(benchmark, quotes):
    benchmark(indicators.get_stoch, quotes)

def test_benchmark_super_trend(benchmark, quotes):
    benchmark(indicators.get_super_trend, quotes)
