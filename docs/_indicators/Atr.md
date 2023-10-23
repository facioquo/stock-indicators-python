---
title: Average True Range (ATR)
permalink: /indicators/Atr/
type: price-characteristic
layout: indicator
---

# {{ page.title }}

<hr>

## **get_atr**(*quotes, lookback_periods=14*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 14* | Number of periods (`N`) to consider.  Must be greater than 1.

### Historical quotes requirements

You must have at least `N+100` periods of `quotes` to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `N+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
ATRResults[ATRResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ATRResults` is just a list of `ATRResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values for ATR since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### ATRResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `tr` | float, Optional  | True Range for current period
| `atr` | float, Optional  | Average True Range
| `atrp` | float, Optional  | Average True Range Percent is `(atr/Close Price)*100`.  This normalizes so it can be compared to other stocks.

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

# calculate 14-period ATR
results = indicators.get_atr(quotes, 14)
```

## About {{ page.title }}

Created by J. Welles Wilder, [Average True Range](https://en.wikipedia.org/wiki/Average_true_range) is a measure of volatility that captures gaps and limits between periods.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/269 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Atr.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Atr/Atr.Series.cs)
- [Python wrapper]({{site.sourceurl}}/atr.py)
