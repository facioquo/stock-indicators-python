---
title: Ultimate Oscillator
permalink: /indicators/Ultimate/
type: oscillator
layout: indicator
---

# {{ page.title }}

<hr>

## **get_ultimate**(*quotes, short_periods=7, middle_periods=14, long_periods=28*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `short_periods` | int, *default 7* | Number of periods (`S`) in the short lookback.  Must be greater than 0.
| `middle_periods` | int, *default 14* | Number of periods (`M`) in the middle lookback.  Must be greater than `S`.
| `long_periods` | int, *default 28* | Number of periods (`L`) in the long lookback.  Must be greater than `M`.

### Historical quotes requirements

You must have at least `L+1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
UltimateResults[UltimateResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `UltimateResults` is just a list of `UltimateResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `L-1` periods will have `None` Ultimate values since there's not enough data to calculate.

### UltimateResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `ultimate` | float, Optional | Simple moving average

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

# calculate 20-period Ultimate
results = indicators.get_ultimate(quotes, 7, 14, 28)
```

## About {{ page.title }}

Created by Larry Williams, the [Ultimate Oscillator](https://en.wikipedia.org/wiki/Ultimate_oscillator) uses several lookback periods to weigh buying power against true range price to produce on oversold / overbought oscillator.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/231 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Ultimate.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Ultimate/Ultimate.Series.cs)
- [Python wrapper]({{site.sourceurl}}/ultimate.py)
