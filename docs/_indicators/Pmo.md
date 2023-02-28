---
title: Price Momentum Oscillator (PMO)
permalink: /indicators/Pmo/
type: price-characteristic
layout: indicator
---

# {{ page.title }}

<hr>

## **get_pmo**(*quotes, time_periods=35*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `time_periods` | int, *default 35* | Number of periods (`T`) for ROC EMA smoothing.  Must be greater than 1.

### Historical quotes requirements

You must have at least `N` periods of `quotes`, where `N` is the greater of `T+S`,`2×T`, or `T+100` to cover the convergence periods.  Since this uses multiple smoothing operations, we recommend you use at least `N+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
PMOResults[PMOResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `PMOResults` is just a list of `PMOResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `T+S-1` periods will have `None` values for PMO since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `T+S+250` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### PMOResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `pmo` | float, Optional | Price Momentum Oscillator
| `signal` | float, Optional | Signal line is EMA of PMO

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

# Calculate 20-period PMO
results = indicators.get_pmo(quotes, 35,20,10)
```

## About {{ page.title }}

Created by Carl Swenlin, the DecisionPoint [Price Momentum Oscillator](https://school.stockcharts.com/doku.php?id=technical_indicators:dppmo) is double-smoothed ROC based momentum indicator.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/244 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Pmo.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/Pmo/Pmo.Series.cs)
- [Python wrapper]({{site.sourceurl}}/pmo.py)
