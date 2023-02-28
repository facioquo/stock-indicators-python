---
title: Volume Weighted Moving Average (VWMA)
permalink: /indicators/Vwma/
type: moving-average
layout: indicator
---

# {{ page.title }}

<hr>

## **get_vwma**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
VWMAResults[VWMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `VWMAResults` is just a list of `VWMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values for `Vwma` since there's not enough data to calculate.

### VWMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `vwma` | float, Optional | Volume Weighted Moving Average

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

# Calculate 10-period VWMA
results = indicators.get_vwma(quotes, 10)
```

## About {{ page.title }}

Volume Weighted Moving Average is the volume adjusted average price over a lookback window.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/657 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Vwma.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Vwma/Vwma.Series.cs)
- [Python wrapper]({{site.sourceurl}}/vwma.py)
