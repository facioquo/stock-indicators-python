---
title: Hull Moving Average (HMA)
permalink: /indicators/Hma/
type: moving-average
layout: indicator
---

# {{ page.title }}

<hr>

## **get_hma**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 1.

### Historical quotes requirements

You must have at least `N+(integer of SQRT(N))-1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
HMAResults[HMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `HMAResults` is just a list of `HMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N+(integer of SQRT(N))-1` periods will have `None` values since there's not enough data to calculate.

### HMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `hma` | float, Optional | Hull moving average

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

# Calculate 20-period HMA
results = indicators.get_hma(quotes, 20)
```

## About {{ page.title }}

Created by Alan Hull, the [Hull Moving Average](https://alanhull.com/hull-moving-average) is a modified weighted average of `close` price over `N` lookback periods that reduces lag.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/252 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Hma.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/Hma/Hma.Series.cs)
- [Python wrapper]({{site.sourceurl}}/hma.py)
