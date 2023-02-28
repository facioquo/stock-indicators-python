---
title: MESA Adaptive Moving Average (MAMA)
permalink: /indicators/Mama/
type: moving-average
layout: indicator
---

# {{ page.title }}

<hr>

## **get_mama**(*quotes, fast_limit=0.5, slow_limit=0.05*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `fast_limit` | float, *default 0.5* | Fast limit threshold.  Must be greater than `slowLimit` and less than 1.
| `slow_limit` | float, *default 0.05* | Slow limit threshold.  Must be greater than 0.

### Historical quotes requirements

You must have at least `50` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
MAMAResults[MAMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `MAMAResults` is just a list of `MAMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `5` periods will have `None` values for `Mama` since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `50` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### MAMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `mama` | float, Optional | MESA adaptive moving average (MAMA)
| `fama` | float, Optional | Following adaptive moving average (FAMA)

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

# Calculate Mama(0.5,0.05)
results = indicators.get_mama(quotes, 0.5,0.05)
```

## About {{ page.title }}

Created by John Ehlers, the [MAMA](http://mesasoftware.com/papers/MAMA.pdf) indicator is a 5-period adaptive moving average of high/low price.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/211 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Mama.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/Mama/Mama.Series.cs)
- [Python wrapper]({{site.sourceurl}}/mama.py)
