---
title: Standard Deviation (volatility)
description: Standard Deviation, Historical Volatility (HV)
permalink: /indicators/StdDev/
type: numerical-analysis
layout: indicator
---

# {{ page.title }}

<hr>

## **get_stdev**(*quotes, lookback_periods, sma_periods=None*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) in the lookback period.  Must be greater than 1 to calculate; however we suggest a larger period for statistically appropriate sample size.
| `sma_periods` | int, Optional | Number of periods in the moving average of `Stdev`.  Must be greater than 0, if specified.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
StdevResults[StdevResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `StdevResults` is just a list of `StdevResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### StdevResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `stdev` | float, Optional | Standard Deviation of Close price over `N` lookback periods
| `mean` | float, Optional | Mean value of Close price over `N` lookback periods
| `z_score` | float, Optional | Z-Score of current Close price (number of standard deviations from mean)
| `stdev_sma` | float, Optional | Moving average (SMA) of STDDEV based on `sma_periods` periods, if specified

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

# Calculate 10-period Standard Deviation
results = indicators.get_stdev(quotes, 10)
```

## About {{ page.title }}

[Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation) of Close price over a rolling lookback window.  Also known as Historical Volatility (HV).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/239 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/StdDev.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/StdDev/StdDev.Series.cs)
- [Python wrapper]({{site.sourceurl}}/stdev.py)
