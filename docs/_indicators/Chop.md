---
title: Choppiness Index
permalink: /indicators/Chop/
type: price-characteristic
layout: indicator
---

# {{ page.title }}

<hr>

## **get_chop**(*quotes, lookback_periods=14*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 14* | Number of periods (`N`) for the lookback evaluation.  Must be greater than 1.

### Historical quotes requirements

You must have at least `N+1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
ChopResults[ChopResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ChopResults` is just a list of `ChopResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` values since there's not enough data to calculate.

### ChopResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `chop` | float, Optional | Choppiness Index

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

# Calculate CHOP(14)
results = indicators.get_chop(quotes, 14)
```

## About {{ page.title }}

Created by E.W. Dreiss, the Choppiness Index measures the trendiness or choppiness on a scale of 0 to 100, to depict steady trends versus conditions of choppiness.  [[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/357 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Chop.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Chop/Chop.Series.cs)
- [Python wrapper]({{site.sourceurl}}/chop.py)
