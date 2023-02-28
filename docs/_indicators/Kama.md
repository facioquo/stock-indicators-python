---
title: Kaufman's Adaptive Moving Average (KAMA)
permalink: /indicators/Kama/
type: moving-average
layout: indicator
---

# {{ page.title }}

<hr>

## **get_kama**(*quotes, er_periods=10, fast_periods=2, slow_periods=30*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `er_periods` | int, *default 10* | Number of Efficiency Ratio (volatility) periods (`E`).  Must be greater than 0.
| `fast_periods` | int, *default 2* | Number of Fast EMA periods.  Must be greater than 0.
| `slow_periods` | int, *default 30* | Number of Slow EMA periods.  Must be greater than `fast_periods`.

### Historical quotes requirements

You must have at least `6×E` or `E+100` periods of `quotes`, whichever is more, to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `10×E` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
KAMAResults[KAMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `KAMAResults` is just a list of `KAMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `10×E` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### KAMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `efficiency_ratio`   | float, Optional | Efficiency Ratio is the fractal efficiency of price changes
| `kama` | Decimal, Optional | Kaufman's adaptive moving average

More about Efficiency Ratio(ER): ER fluctuates between 0 and 1, but these extremes are the exception, not the norm. ER would be 1 if prices moved up or down consistently over the `er_periods` periods. ER would be zero if prices are unchanged over the `er_periods` periods.

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate KAMA(10,2,30)
results = indicators.get_kama(quotes, 10,2,30)
```

## About {{ page.title }}

Created by Perry Kaufman, [KAMA](https://school.stockcharts.com/doku.php?id=technical_indicators:kaufman_s_adaptive_moving_average) is an volatility adaptive moving average of Close price over configurable lookback periods.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/210 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Kama.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/Kama/Kama.Series.cs)
- [Python wrapper]({{site.sourceurl}}/kama.py)
