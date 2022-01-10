---
title: Performance benchmarks for v0.1.0
permalink: /performance/
layout: default
---

# {{ page.title }}

These are the execution times for the current indicators using two years of historical daily stock quotes (502 periods) with default or typical parameters.

``` bash
pytest=v6.2.5, pytest-benchmark=v3.4.1 OS=macOS Monterey 12.0.1
Apple M1, 8 cores
.NET SDK=Mono 6.12.0.90
```

## Indicators

|         Indicators |        Mean |    StdDev |      Median |
|------------------- |------------:|----------:|------------:|
|                ADL |   3.805 ms |  0.651 ms |   3.627 ms |
|                ADX |   4.857 ms |  0.155 ms |   4.844 ms |
|          Alligator |   3.893 ms |  0.054 ms |   3.834 ms |
|               ALMA |   3.791 ms |  0.079 ms |   3.773 ms |
|              Aroon |   4.196 ms |  0.054 ms |   4.187 ms |
|                ATR |   3.680 ms |  0.034 ms |   3.670 ms |
|            Awesome |   4.206 ms |  0.041 ms |   4.192 ms |
|               Beta |   8.550 ms |  0.097 ms |   8.535 ms |
|     BollingerBands |   4.826 ms |  0.070 ms |   4.810 ms |
|         Chandelier |   4.182 ms |  0.048 ms |   4.165 ms |
|           Donchian |   4.265 ms |  0.043 ms |   4.249 ms |
|         Double EMA |   3.727 ms |  0.080 ms |   3.704 ms |
|          Elder Ray |   3.852 ms |  0.037 ms |   3.840 ms |
|                EMA |   3.678 ms |  0.075 ms |   3.660 ms |
|            Fractal |   3.670 ms |  0.049 ms |   3.663 ms |
|        Heikin-Ashi |   4.738 ms |  0.261 ms |   3.886 ms |
|           Ichimoku |   5.890 ms |  0.061 ms |   5.872 ms |
|               MACD |   3.941 ms |  0.070 ms |   3.921 ms |
|      Parabolic SAR |   3.760 ms |  0.129 ms |   3.731 ms |
|                ROC |   3.612 ms |  0.076 ms |   3.582 ms |
|                RSI |   4.104 ms |  0.075 ms |   4.087 ms |
|              Slope |   4.672 ms |  0.170 ms |   4.119 ms |
|                SMA |   3.781 ms |  0.050 ms |   3.766 ms |
|     Stdev Channels |   4.194 ms |  0.090 ms |   4.164 ms |
|       SMA Extended |   7.710 ms |  0.112 ms |   7.692 ms |
|              Stoch |   4.212 ms |  0.044 ms |   4.198 ms |
|          Stoch RSI |   4.984 ms |  0.120 ms |   4.939 ms |
|         SuperTrend |   4.179 ms |  0.058 ms |   4.163 ms |
|         Triple EMA |   3.841 ms |  0.065 ms |   3.821 ms |
|               Trix |   4.068 ms |  0.072 ms |   4.044 ms |
