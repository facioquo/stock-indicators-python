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

|             Method |        Mean |    StdDev |      Median |
|------------------- |------------:|----------:|------------:|
|             GetAdl |   3.805 ms |  0.651 ms |   3.627 ms |
|             GetAdx |   4.857 ms |  0.155 ms |   4.844 ms |
|       GetAlligator |   3.893 ms |  0.054 ms |   3.834 ms |
|            GetAlma |   3.791 ms |  0.079 ms |   3.773 ms |
|           GetAroon |   4.196 ms |  0.054 ms |   4.187 ms |
|             GetAtr |   3.680 ms |  0.034 ms |   3.670 ms |
|         GetAwesome |   4.206 ms |  0.041 ms |   4.192 ms |
|            GetBeta |   8.550 ms |  0.097 ms |   8.535 ms |
|  GetBollingerBands |   4.826 ms |  0.070 ms |   4.810 ms |
|             GetEma |   3.678 ms |  0.075 ms |   3.660 ms |
|         GetFractal |   3.670 ms |  0.049 ms |   3.663 ms |
|            GetMacd |   3.941 ms |  0.070 ms |   3.921 ms |
|             GetRsi |   4.104 ms |  0.075 ms |   4.087 ms |
|             GetSma |   3.781 ms |  0.050 ms |   3.766 ms |
|     GetSmaExtended |   7.710 ms |  0.112 ms |   7.692 ms |
|           GetStoch |   4.212 ms |  0.044 ms |   4.198 ms |
|        GetStochRsi |   4.984 ms |  0.120 ms |   4.939 ms |
|      GetSuperTrend |   4.179 ms |  0.058 ms |   4.163 ms |
