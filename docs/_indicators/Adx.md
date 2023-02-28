---
title: Average Directional Index (ADX)
permalink: /indicators/Adx/
type: price-trend
layout: indicator
---

# {{ page.title }}

<hr>

## **get_adx**(*quotes, lookback_periods=14*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 14* | Number of periods (`N`) for the lookback evaluation.  Must be greater than 0.

### Historical quotes requirements

You must have at least `2×N+100` periods of `quotes` to allow for smoothing convergence.  We generally recommend you use at least `2×N+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
ADXResults[ADXResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ADXResults` is just a list of `ADXResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `2×N-1` periods will have `None` values for `Adx` since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `2×N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### ADXResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `pdi` | float, Optional | Plus Directional Index (+DI)
| `mdi` | float, Optional | Minus Directional Index (-DI)
| `adx` | float, Optional | Average Directional Index (ADX)
| `adxr` | float, Optional | Average Directional Index Rating (ADXR)

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

# calculate 14-period ADX
results = indicators.get_adx(quotes, lookback_periods)
```

## About {{ page.title }}

Created by J. Welles Wilder, the [Average Directional Movement Index](https://en.wikipedia.org/wiki/Average_directional_movement_index) is a measure of price directional movement.  It includes upward and downward indicators, and is often used to measure strength of trend.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/270 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/AdIndex.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Adx/Adx.Series.cs)
- [Python wrapper]({{site.sourceurl}}/adx.py)
