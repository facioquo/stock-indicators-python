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

## indicators

|             Method |        Mean |     Error |    StdDev |      Median |
|------------------- |------------:|----------:|----------:|------------:|
|             GetAdl |   142.97 μs |  0.497 μs |  0.388 μs |   142.94 μs |
|             GetAdx |   751.34 μs |  2.972 μs |  2.482 μs |   750.57 μs |
|       GetAlligator |   234.74 μs |  1.240 μs |  1.160 μs |   234.56 μs |
|            GetAlma |   215.96 μs |  1.546 μs |  1.370 μs |   215.42 μs |
|           GetAroon |   353.01 μs |  0.803 μs |  0.670 μs |   352.93 μs |
|             GetAtr |   159.49 μs |  1.414 μs |  1.254 μs |   159.12 μs |
|         GetAwesome |   330.95 μs |  1.490 μs |  1.321 μs |   331.14 μs |
|            GetBeta |   959.70 μs |  2.365 μs |  1.975 μs |   959.47 μs |
|  GetBollingerBands |   457.88 μs |  1.584 μs |  1.323 μs |   457.95 μs |
|             GetEma |   100.30 μs |  0.622 μs |  0.582 μs |   100.25 μs |
|         GetFractal |   104.33 μs |  0.469 μs |  0.392 μs |   104.32 μs |
|            GetMacd |   217.86 μs |  1.426 μs |  1.264 μs |   217.51 μs |
|             GetRsi |   340.61 μs |  1.052 μs |  0.821 μs |   340.70 μs |
|             GetSma |   107.26 μs |  0.363 μs |  0.303 μs |   107.21 μs |
|     GetSmaExtended |   942.89 μs |  5.649 μs |  5.284 μs |   940.02 μs |
|           GetStoch |   403.67 μs |  1.003 μs |  0.838 μs |   403.38 μs |
|        GetStochRsi |   708.34 μs |  2.750 μs |  2.296 μs |   707.45 μs |
|      GetSuperTrend |   301.10 μs |  0.886 μs |  0.692 μs |   301.20 μs |

<!-- ## quotes functions (mostly internal)

|          Method |         Mean |      Error |     StdDev |
|---------------- |-------------:|-----------:|-----------:|
|            Sort | 37,768.62 ns | 406.995 ns | 360.790 ns |
|        Validate | 40,457.78 ns | 301.177 ns | 266.985 ns |
|       Aggregate |     83.36 ns |   0.699 ns |   0.545 ns |
|  ConvertToBasic | 42,362.26 ns | 144.200 ns | 120.414 ns |
| ConvertToQuotes |  8,378.83 ns |  71.755 ns |  63.609 ns |

## math functions (internal)

| Method | Periods |        Mean |    Error |   StdDev |
|------- |-------- |------------:|---------:|---------:|
| StdDev |      20 |    36.84 ns | 0.194 ns | 0.172 ns |
| StdDev |      50 |    95.47 ns | 0.306 ns | 0.256 ns |
| StdDev |     250 |   530.23 ns | 1.303 ns | 1.088 ns |
| StdDev |    1000 | 2,142.94 ns | 5.994 ns | 5.313 ns | -->
