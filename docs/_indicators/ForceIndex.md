---
title: Force Index
permalink: /indicators/ForceIndex/
type: volume-based
layout: indicator
---

# {{ page.title }}

<hr>

## **get_force_index**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Lookback window (`N`) for the EMA of Force Index.  Must be greater than 0 and is commonly 2 or 13 (shorter/longer view).

### Historical quotes requirements

You must have at least `N+100` for `2×N` periods of `quotes`, whichever is more, to cover the convergence periods.  Since this uses a smoothing technique for EMA, we recommend you use at least `N+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
ForceIndexResults[ForceIndexResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ForceIndexResults` is just a list of `ForceIndexResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods for will be `None` since they cannot be calculated.

> :hourglass: **Convergence warning**: The first `N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### ForceIndexResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `force_index` | float, Optional | Force Index

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

# Calculate ForceIndex(13)
results = indicators.get_force_index(quotes, 13)
```

## About {{ page.title }}

Created by Alexander Elder, the [Force Index](https://en.wikipedia.org/wiki/Force_index) depicts volume-based buying and selling pressure.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/382 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/ForceIndex.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/ForceIndex/ForceIndex.Series.cs)
- [Python wrapper]({{site.sourceurl}}/force_index.py)
