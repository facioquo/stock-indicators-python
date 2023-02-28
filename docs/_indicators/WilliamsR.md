---
title: Williams %R
permalink: /indicators/WilliamsR/
type: oscillator
layout: indicator
---

# {{ page.title }}

<hr>

## **get_williams_r**(*quotes, lookback_periods=14*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 14* | Number of periods (`N`) in the lookback period.  Must be greater than 0.  Default is 14.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
WilliamsResults[WilliamsResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `WilliamsResults` is just a list of `WilliamsResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` Oscillator values since there's not enough data to calculate.

### WilliamsResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `williams_r` | float, Optional | Oscillator over prior `N` lookback periods

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

# Calculate WilliamsR(14)
results = indicators.get_williams_r(quotes, 14)
```

## About {{ page.title }}

Created by Larry Williams, the [Williams %R](https://en.wikipedia.org/wiki/Williams_%25R) momentum indicator is a stochastic oscillator with scale of -100 to 0.  It is exactly the same as the Fast variant of [Stochastic Oscillator](../Stoch#content), but with a different scaling.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/229 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/WilliamsR.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/WilliamsR/WilliamsR.Series.cs)
- [Python wrapper]({{site.sourceurl}}/williams_r.py)
