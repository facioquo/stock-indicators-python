---
title: Balance of Power (BOP)
description: Balance of Power (BOP) / Balance of Market Power
permalink: /indicators/Bop/
type: price-characteristic
layout: indicator
---

# {{ page.title }}

<hr>

## **get_bop**(*quotes, smooth_periods=14*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `smooth_periods` | int, *default 14* | Number of periods (`N`) for smoothing.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
BOPResults[BOPResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `BOPResults` is just a list of `BOPResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### BOPResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `bop` | float, Optional | Balance of Power

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

# Calculate 14-period BOP
results = indicators.get_bop(quotes, 14)
```

## About {{ page.title }}

Created by Igor Levshin, the [Balance of Power](https://school.stockcharts.com/doku.php?id=technical_indicators:balance_of_power) (aka Balance of Market Power) is a momentum oscillator that depicts the strength of buying and selling pressure.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/302 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Bop.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Bop/Bop.Series.cs)
- [Python wrapper]({{site.sourceurl}}/bop.py)
