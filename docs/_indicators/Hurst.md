---
title: Hurst Exponent
description: Hurst Exponent with Rescaled Range Analysis
permalink: /indicators/Hurst/
type: price-characteristic
layout: indicator
---

# {{ page.title }}

<hr>

## **get_hurst**(*quotes, lookback_periods=100*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 100* | Number of periods (`N`) in the Hurst Analysis.  Must be greater than 100.

### Historical quotes requirements

You must have at least `N+1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
HurstResults[HurstResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `HurstResults` is just a list of `HurstResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` values since there's not enough data to calculate.

### HurstResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `hurst_exponent` | float, Optional | Hurst Exponent (`H`)

### Utilities

- ~~[.to_quotes()]({{site.baseurl}}/utilities#convert-to-quotes)~~ <code style='color: #d32f2f; important'>[deprecated]</code>
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate 20-period Hurst
results = indicators.get_hurst(quotes, 20)
```

## About {{ page.title }}

The [Hurst Exponent](https://en.wikipedia.org/wiki/Hurst_exponent) is a [random-walk](https://en.wikipedia.org/wiki/Random_walk) path analysis that measures trending and mean-reverting tendencies of incremental return values.  When `H` is greater than 0.5 it depicts trending.  When `H` is less than 0.5 it is is more likely to revert to the mean.  When `H` is around 0.5 it represents a random walk.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/477 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Hurst.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/Hurst/Hurst.Series.cs)
- [Python wrapper]({{site.sourceurl}}/hurst.py)
