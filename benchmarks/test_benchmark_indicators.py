import pytest

from stock_indicators import indicators
from stock_indicators.indicators.common.enums import PeriodSize


@pytest.mark.performance
class TestPerformance:
    def test_benchmark_adl(self, benchmark, quotes):
        benchmark(indicators.get_adl, quotes)

    def test_benchmark_adx(self, benchmark, quotes):
        benchmark(indicators.get_adx, quotes)

    def test_benchmark_alligator(self, benchmark, quotes):
        benchmark(indicators.get_alligator, quotes)

    def test_benchmark_alma(self, benchmark, quotes):
        benchmark(indicators.get_alma, quotes)

    def test_benchmark_aroon(self, benchmark, quotes):
        benchmark(indicators.get_aroon, quotes)

    def test_benchmark_atr_stop(self, benchmark, quotes):
        benchmark(indicators.get_atr_stop, quotes)

    def test_benchmark_atr(self, benchmark, quotes):
        benchmark(indicators.get_atr, quotes)

    def test_benchmark_awesome(self, benchmark, quotes):
        benchmark(indicators.get_awesome, quotes)

    def test_benchmark_beta(self, benchmark, quotes, quotes_other):
        benchmark(indicators.get_beta, quotes, quotes_other, 20)

    def test_benchmark_bollinger_bands(self, benchmark, quotes):
        benchmark(indicators.get_bollinger_bands, quotes)

    def test_benchmark_bop(self, benchmark, quotes):
        benchmark(indicators.get_bop, quotes)

    def test_benchmark_cci(self, benchmark, quotes):
        benchmark(indicators.get_cci, quotes, 20)

    def test_benchmark_chaikin_osc(self, benchmark, quotes):
        benchmark(indicators.get_chaikin_osc, quotes)

    def test_benchmark_chandelier(self, benchmark, quotes):
        benchmark(indicators.get_chandelier, quotes)

    def test_benchmark_chop(self, benchmark, quotes):
        benchmark(indicators.get_chop, quotes)

    def test_benchmark_cmf(self, benchmark, quotes):
        benchmark(indicators.get_cmf, quotes)

    def test_benchmark_cmo(self, benchmark, quotes):
        benchmark(indicators.get_cmo, quotes, 14)

    def test_benchmark_connors_rsi(self, benchmark, quotes):
        benchmark(indicators.get_connors_rsi, quotes)

    @pytest.mark.perf_focus
    def test_benchmark_correlation(self, benchmark, quotes, quotes_other):
        benchmark(indicators.get_correlation, quotes, quotes_other, 20)

    def test_benchmark_doji(self, benchmark, quotes):
        benchmark(indicators.get_doji, quotes)

    def test_benchmark_donchian(self, benchmark, quotes):
        benchmark(indicators.get_donchian, quotes)

    def test_benchmark_dema(self, benchmark, quotes):
        benchmark(indicators.get_dema, quotes, 20)

    def test_benchmark_dpo(self, benchmark, quotes):
        benchmark(indicators.get_dpo, quotes, 14)

    def test_benchmark_dynamic(self, benchmark, quotes):
        benchmark(indicators.get_dynamic, quotes, 14)

    def test_benchmark_elder_ray(self, benchmark, quotes):
        benchmark(indicators.get_elder_ray, quotes)

    def test_benchmark_ema(self, benchmark, quotes):
        benchmark(indicators.get_ema, quotes, 20)

    def test_benchmark_epma(self, benchmark, quotes):
        benchmark(indicators.get_epma, quotes, 20)

    def test_benchmark_fcb(self, benchmark, quotes):
        benchmark(indicators.get_fcb, quotes)

    def test_benchmark_fisher_transform(self, benchmark, quotes):
        benchmark(indicators.get_fisher_transform, quotes)

    def test_benchmark_force_index(self, benchmark, quotes):
        benchmark(indicators.get_force_index, quotes, 13)

    def test_benchmark_fractal(self, benchmark, quotes):
        benchmark(indicators.get_fractal, quotes)

    def test_benchmark_gator(self, benchmark, quotes):
        benchmark(indicators.get_gator, quotes)

    def test_benchmark_heikin_ashi(self, benchmark, quotes):
        benchmark(indicators.get_heikin_ashi, quotes)

    def test_benchmark_hma(self, benchmark, quotes):
        benchmark(indicators.get_hma, quotes, 20)

    @pytest.mark.perf_focus
    def test_benchmark_ht_trendline(self, benchmark, quotes):
        benchmark(indicators.get_ht_trendline, quotes)

    def test_benchmark_hurst(self, benchmark, quotes):
        benchmark(indicators.get_hurst, quotes)

    def test_benchmark_hurst_longlong(self, benchmark, quotes_longish):
        benchmark(indicators.get_hurst, quotes_longish + quotes_longish)

    @pytest.mark.perf_focus
    def test_benchmark_ichimoku(self, benchmark, quotes):
        benchmark(indicators.get_ichimoku, quotes)

    def test_benchmark_kama(self, benchmark, quotes):
        benchmark(indicators.get_kama, quotes)

    def test_benchmark_keltner(self, benchmark, quotes):
        benchmark(indicators.get_keltner, quotes)

    def test_benchmark_kvo(self, benchmark, quotes):
        benchmark(indicators.get_kvo, quotes)

    def test_benchmark_ma_envelopes(self, benchmark, quotes):
        benchmark(indicators.get_ma_envelopes, quotes, 10)

    def test_benchmark_macd(self, benchmark, quotes):
        benchmark(indicators.get_macd, quotes)

    def test_benchmark_mama(self, benchmark, quotes):
        benchmark(indicators.get_mama, quotes)

    def test_benchmark_marubozu(self, benchmark, quotes):
        benchmark(indicators.get_marubozu, quotes)

    def test_benchmark_mfi(self, benchmark, quotes):
        benchmark(indicators.get_mfi, quotes)

    def test_benchmark_obv(self, benchmark, quotes):
        benchmark(indicators.get_obv, quotes)

    @pytest.mark.perf_focus
    def test_benchmark_parabolic_sar(self, benchmark, quotes):
        benchmark(indicators.get_parabolic_sar, quotes)

    def test_benchmark_pivot_points(self, benchmark, quotes):
        benchmark(indicators.get_pivot_points, quotes, PeriodSize.MONTH)

    def test_benchmark_pivots(self, benchmark, quotes):
        benchmark(indicators.get_pivots, quotes)

    def test_benchmark_pmo(self, benchmark, quotes):
        benchmark(indicators.get_pmo, quotes)

    def test_benchmark_prs(self, benchmark, quotes):
        benchmark(indicators.get_prs, quotes, quotes)

    def test_benchmark_pvo(self, benchmark, quotes):
        benchmark(indicators.get_pvo, quotes)

    def test_benchmark_renko(self, benchmark, quotes):
        benchmark(indicators.get_renko, quotes, 2.5)

    def test_benchmark_roc(self, benchmark, quotes):
        benchmark(indicators.get_roc, quotes, 20)

    @pytest.mark.perf_focus
    def test_benchmark_rolling_pivots(self, benchmark, quotes):
        benchmark(indicators.get_rolling_pivots, quotes, 14, 1)

    def test_benchmark_rsi(self, benchmark, quotes):
        benchmark(indicators.get_rsi, quotes)

    def test_benchmark_slope(self, benchmark, quotes):
        benchmark(indicators.get_slope, quotes, 20)

    def test_benchmark_sma(self, benchmark, quotes):
        benchmark(indicators.get_sma, quotes, 20)

    def test_benchmark_sma_longlong(self, benchmark, quotes_longish):
        benchmark(indicators.get_sma, quotes_longish + quotes_longish, 20)

    def test_benchmark_smi(self, benchmark, quotes):
        benchmark(indicators.get_smi, quotes, 14, 20, 5, 3)

    def test_benchmark_smma(self, benchmark, quotes):
        benchmark(indicators.get_smma, quotes, 20)

    def test_benchmark_starc_bands(self, benchmark, quotes):
        benchmark(indicators.get_starc_bands, quotes, 10)

    def test_benchmark_stc(self, benchmark, quotes):
        benchmark(indicators.get_stc, quotes)

    def test_benchmark_stdev_channels(self, benchmark, quotes):
        benchmark(indicators.get_stdev_channels, quotes, 20, 2)

    def test_benchmark_stdev(self, benchmark, quotes):
        benchmark(indicators.get_stdev, quotes, 10)

    def test_benchmark_stoch_rsi(self, benchmark, quotes):
        benchmark(indicators.get_stoch_rsi, quotes, 14, 14, 3, 1)

    def test_benchmark_stoch(self, benchmark, quotes):
        benchmark(indicators.get_stoch, quotes)

    def test_benchmark_super_trend(self, benchmark, quotes):
        benchmark(indicators.get_super_trend, quotes)

    def test_benchmark_t3(self, benchmark, quotes):
        benchmark(indicators.get_t3, quotes)

    def test_benchmark_triple_ema(self, benchmark, quotes):
        benchmark(indicators.get_tema, quotes, 20)

    def test_benchmark_trix(self, benchmark, quotes):
        benchmark(indicators.get_trix, quotes, 20, 5)

    def test_benchmark_tsi(self, benchmark, quotes):
        benchmark(indicators.get_tsi, quotes)

    def test_benchmark_ulcer_index(self, benchmark, quotes):
        benchmark(indicators.get_ulcer_index, quotes)

    def test_benchmark_ultimate(self, benchmark, quotes):
        benchmark(indicators.get_ultimate, quotes)

    def test_benchmark_volatility_stop(self, benchmark, quotes):
        benchmark(indicators.get_volatility_stop, quotes)

    def test_benchmark_vortex(self, benchmark, quotes):
        benchmark(indicators.get_vortex, quotes, 14)

    def test_benchmark_vwap(self, benchmark, quotes):
        benchmark(indicators.get_vwap, quotes)

    def test_benchmark_vwma(self, benchmark, quotes):
        benchmark(indicators.get_vwma, quotes, 10)

    def test_benchmark_williams_r(self, benchmark, quotes):
        benchmark(indicators.get_williams_r, quotes)

    def test_benchmark_wma(self, benchmark, quotes):
        benchmark(indicators.get_wma, quotes, 20)

    def test_benchmark_zig_zag(self, benchmark, quotes):
        benchmark(indicators.get_zig_zag, quotes)

    def test_benchmark_converting_to_IndicatorResults(self, benchmark, quotes):
        from stock_indicators._cslib import CsIndicator
        from stock_indicators.indicators.common.enums import CandlePart
        from stock_indicators.indicators.common.quote import Quote
        from stock_indicators.indicators.sma import SMAResult, SMAResults

        candle_part: CandlePart = CandlePart.CLOSE
        lookback_periods = 12
        quotes = Quote.use(
            quotes * 1000, candle_part
        )  # Error occurs if not assigned to local var.
        results = CsIndicator.GetSma(quotes, lookback_periods)

        benchmark(SMAResults, results, SMAResult)

    def test_benchmark_converting_to_CsDecimal(self, benchmark, raw_data):
        from stock_indicators._cstypes import Decimal as CsDecimal

        raw_data = raw_data * 1000

        def convert_to_quotes(rows):
            for row in rows:
                CsDecimal(row[2])

        benchmark(convert_to_quotes, raw_data)
