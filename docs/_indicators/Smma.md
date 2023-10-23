---
title: Smoothed Moving Average (SMMA)
description: Smoothed Moving Average (SMMA), Modified Moving Average (MMA), Running Moving Average (RMA)
permalink: /indicators/Smma/
type: moving-average
layout: indicator
---

# {{ page.title }}

<hr>

## **get_smma**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 0.

### Historical quotes requirements

You must have at least `2×N` or `N+100` periods of `quotes`, whichever is more, to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `N+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
SMMAResults[SMMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `SMMAResults` is just a list of `SMMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### SMMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `smma` | float, Optional | Smoothed moving average

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

# Calculate 20-period SMMA
results = indicators.get_smma(quotes, 20)
```

## About {{ page.title }}

[Smoothed Moving Average](https://en.wikipedia.org/wiki/Moving_average) is the average of Close price over a lookback window using a smoothing method.  SMMA is also known as modified moving average (MMA) and running moving average (RMA).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/375 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Smma.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Smma/Smma.Series.cs)
- [Python wrapper]({{site.sourceurl}}/smma.py)
