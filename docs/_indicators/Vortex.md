---
title: Vortex Indicator (VI)
permalink: /indicators/Vortex/
type: price-trend
layout: indicator
---

# {{ page.title }}

<hr>

## **get_vortex**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) to consider.  Must be greater than 1 and is usually between 14 and 30.

### Historical quotes requirements

You must have at least `N+1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
VortexResults[VortexResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `VortexResults` is just a list of `VortexResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` values for VI since there's not enough data to calculate.

### VortexResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `pvi` | float, Optional | Positive Vortex Indicator (VI+)
| `nvi` | float, Optional | Negative Vortex Indicator (VI-)

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

# Calculate 14-period VI
results = indicators.get_vortex(quotes, 14);
```

## About {{ page.title }}

Created by Etienne Botes and Douglas Siepman, the [Vortex Indicator](https://en.wikipedia.org/wiki/Vortex_indicator) is a measure of price directional movement.  It includes positive and negative indicators, and is often used to identify trends and reversals.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/339 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Vortex.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Vortex/Vortex.Series.cs)
- [Python wrapper]({{site.sourceurl}}/vortex.py)
