---
title: Awesome Oscillator (AO)
description: Awesome Oscillator (AO), also known as Super AO
permalink: /indicators/Awesome/
type: oscillator
layout: indicator
---

# {{ page.title }}

<hr>

## **get_awesome**(*quotes, fast_periods=5, slow_periods=34*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `fast_periods` | int, *default 5* | Number of periods (`F`) for the faster moving average.  Must be greater than 0.
| `slow_periods` | int, *default 34* | Number of periods (`S`) for the slower moving average.  Must be greater than `fast_periods`.

### Historical quotes requirements

You must have at least `S` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
AwesomeResults[AwesomeResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `AwesomeResults` is just a list of `AwesomeResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first period `S-1` periods will have `None` values since there's not enough data to calculate.

### AwesomeResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `oscillator` | float, Optional | Awesome Oscillator
| `normalized` | float, Optional | `100 × oscillator ÷ (median price)`

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

# calculate
results = indicators.get_awesome(quotes, 5, 34)
```

## About {{ page.title }}

Created by Bill Williams, the Awesome Oscillator (aka Super AO) is a measure of the gap between a fast and slow period modified moving average.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/282 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Awesome.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Awesome/Awesome.Series.cs)
- [Python wrapper]({{site.sourceurl}}/awesome.py)
